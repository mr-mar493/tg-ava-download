from telethon import TelegramClient, events, sync
from os import system
from sys import platform

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

clear()
banner()
id = input("Ваш api_id: ")
apiez = input("Ваш apiez: ")

api_id = id
api_hash = '{apiez}'
client = TelegramClient('an', api_id, api_hash)
client.start()
from ezload import c
try:
    client.download_profile_photo(c)
    client.send_message('@get_any_telegram_id_bot', c)
except:
    print('500')
