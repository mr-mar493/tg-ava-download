from telethon import TelegramClient, events, sync, utils
from os import system,mkdir
from pathlib import Path
from sys import platform
import random

def clear():
	if platform == "linux" or platform == "linux2" or platform == "unix":
		system("clear")
	elif platform == "win32":
		system("cls")
	else:
		system("clear")

def banner():
    print("""
╔════╗╔═══╗     ╔═══╗╔╗──╔╗╔═══╗     ╔═══╗╔═══╗──────╔═╗─╔╗╔╗───╔═══╗╔═══╗╔═══╗
║╔╗╔╗║║╔═╗║     ║╔═╗║║╚╗╔╝║║╔═╗║     ╚╗╔╗║║╔═╗║──────║║╚╗║║║║───║╔═╗║║╔═╗║╚╗╔╗║
╚╝║║╚╝║║─╚╝     ║║─║║╚╗║║╔╝║║─║║     ─║║║║║║─║║╔╗╔╗╔╗║╔╗╚╝║║║───║║─║║║║─║║─║║║║
──║║──║║╔═╗     ║╚═╝║─║╚╝║─║╚═╝║     ─║║║║║║─║║║╚╝╚╝║║║╚╗║║║║─╔╗║║─║║║╚═╝║─║║║║
──║║──║╚╩═║     ║╔═╗║─╚╗╔╝─║╔═╗║     ╔╝╚╝║║╚═╝║╚╗╔╗╔╝║║─║║║║╚═╝║║╚═╝║║╔═╗║╔╝╚╝║
──╚╝──╚═══╝     ╚╝─╚╝──╚╝──╚╝─╚╝     ╚═══╝╚═══╝─╚╝╚╝─╚╝─╚═╝╚═══╝╚═══╝╚╝─╚╝╚═══╝

====================================
YouTube Channel: youtube.com/c/HZFYT
Telegram Channel: t.me/hzfnews
VK: vk.com/hzforum1
====================================
""")

key = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
for n in range(1):
	b=''
	for i in range(5):
		b += (random.choice(key))
		h='@'+b

clear()
banner()
id = input("Ваш api_id: ")
apiez = input("Ваш api_hash: ")
api_id = id
api_hash = apiez
client = TelegramClient('an', api_id, api_hash)
client.start()
try:
    client.download_profile_photo(h, file=h)
    client.send_message('@get_any_telegram_id_bot', h)
    if platform == "linux" or platform == "linux2" or platform == "unix":
        Path("output").mkdir(parents=True, exist_ok=True)
        str(system( "mv " + h[1: ] + ".jpg output"))
        system("mv output ..")
        clear()
        print("Аватарка " + h[1: ] + ".jpg была успешно сохранена в папку output\n\nНажмите ENTER что-бы вернуться в главное меню")
        input()
    elif platform == "win32":
        path = "output"
        mkdir(path)
        str(system("move " + h[1: ] + ".jpg output"))
        system("move output ..")
        clear()
        print("Аватарка " + h[1: ] + ".jpg была успешно сохранена в папку output\n\nНажмите ENTER что-бы вернуться в главное меню")
        input()
except:
    print('500')  
