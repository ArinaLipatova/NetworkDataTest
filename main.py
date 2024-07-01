from tkinter import *
import socket
from speedtest import Speedtest
import bs4, requests

#ФУКНКЦИИ, ЗАДАЮЩИЕ КНОПКИ

def name_test():
    global name
    name = socket.gethostname()
    name_label.config(text='Имя компьютера:\n'+str(name), bg = '#cdfad4')

def IP_test():
    s = requests.get('https://2ip.ua/ru/')
    b = bs4.BeautifulSoup(s.text, "html.parser")

    IP = b.select(" .ipblockgradient .ip")[0].getText()
    #name1 = socket.gethostname()
    #IP = socket.gethostbyname(name1)
    IP_label.config(text='IP-адрес:\n' + (IP), bg='#cdfad4')
    IP_label.grid(row=5, column=1)

def d_test ():
    download = Speedtest().download()
    download_speed = round(download /(10**6),2)
    download_label.config(text='Скорость скачивания:\n'+str(download_speed)+'Mb/s', bg = '#cdfad4')

def up_test ():
    upload = Speedtest().upload()
    upload_speed = round(upload / (10 ** 6), 2)
    upload_label.config(text='Скорость отдачи:\n' + str(upload_speed) + 'Mb/s', bg='#cdfad4')

def p_test():
    ping = Speedtest().upload()
    ping_time = round(ping/1000000, 2)
    ping_label.config(text='Пинг:\n' + str(ping_time) + 'ms', bg='#cdfad4')

root = Tk()

root.title('Speedtest')
root.geometry('1000x600')

#root.configure(fg='red')
root['bg']='white'
#root.configure(bg='blue')

#ЯЧЕЙКИ
download_label = Label(root, text = 'Скорость скачивания: \n', font=('Roboto', 20), bg='white')
#download_label.pack(pady=(40,10))
download_label.grid(row=1, column=1, pady=12, padx=20, ipady=10, ipadx=10)


upload_label= Label(root, text = 'Скорость отдачи: \n', font=('Roboto', 20), bg='white')
#upload_label.pack(pady=(10,0))
upload_label.grid(row=2, column=1, pady=12, padx=20, ipady=10, ipadx=10)


ping_label= Label(root, text = 'Пинг: \n', font=('Roboto', 20), bg='white')
#ping_label.pack(pady=(10,10))
ping_label.grid(row=3, column=1, pady=12, padx=20, ipady=10, ipadx=10)


name_label= Label(root, text = 'Имя компьютера: \n', font=('Roboto', 20), bg='white')
#name_label.pack(pady=(10,10))
name_label.grid(row=4, column=1, pady=12, padx=20, ipady=10, ipadx=10)


IP_label= Label(root, text = 'IP адрес: \n', font=('Roboto', 20), bg='white')
#IP_label.pack(pady=(10,10))
IP_label.grid(row=5, column=1, pady=12, padx=20, ipady=10, ipadx=10)



#КНОПКИ

d_button =Button(root, text ='Download speed', font=('Roboto', 25), command= d_test)
#d_button.pack(padx=(30))
d_button.grid(row=1, column=0, pady=12, padx=20, ipady=10, ipadx=10)

up_button =Button(root, text ='Upload speed', font=('Roboto', 25), command= up_test)
#up_button.pack(padx=(30))
up_button.grid(row=2, column=0, pady=10, padx=20, ipady=10, ipadx=10)

p_button = Button(root, text ='Ping', font=('Roboto', 25), command= p_test)
#p_button.pack(padx=(30))
p_button.grid(row=3, column=0, pady=10, padx=20, ipady=10, ipadx=10)

name_button = Button(root, text ='Name', font=('Roboto', 25), command= name_test)
#name_button.pack(padx=(30))
name_button.grid(row=4, column=0, pady=10, padx=20, ipady=10, ipadx=10)

IP_button = Button(root, text ='IP adress', font=('Roboto', 25), command= IP_test)
#IP_button.pack(padx=(30))
IP_button.grid(row=5, column=0, pady=10, padx=20, ipady=10, ipadx=10)

root.mainloop()