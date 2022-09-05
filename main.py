from telethon import TelegramClient, events, sync
from os import system
from sys import platform
import random

def clear():
	if platform == "linux" or platform == "linux2" or platform == "unix":
		system("clear")
	elif platform == "win32":
		system("cls")
	else:
		system("clear")
key = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
a = '@'
for n in range(1):
	b=''
	for i in range(5):
		b += (random.choice(key))
		c=a+b
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
api_id = СЮДА ВСТАВЛЯТЬ АПИ ИД
api_hash = СЮДА ВСТАВЛЯТЬ АПИ ХЭШ
client = TelegramClient('an', api_id, api_hash)
client.start()
try:
    client.download_profile_photo(c)
    client.send_message('@get_any_telegram_id_bot', c)
except:
    print('500')
