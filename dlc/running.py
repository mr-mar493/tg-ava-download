from calendar import c
from telethon import TelegramClient, events, sync, utils
from os import system
from sys import platform
import random
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

def clear():
	if platform == "linux" or platform == "linux2" or platform == "unix":
		system("clear")
	elif platform == "win32":
		system("cls")
	else:
		system("clear")
banner()
api_id = своё значение
api_hash = 'своё значение'
client = TelegramClient('an', api_id, api_hash)
client.start()
m = random.randint(5,8)
key = 'abcdefghijklmnopqrstuvwxyz_ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
for n in range(1):
	b=''
	for i in range(m):
		b += (random.choice(key))
		h='@'+b
clear()
try:
	client.download_profile_photo(h, file=h)
	client.send_message('@get_any_telegram_id_bot', h)
	if platform == "linux" or platform == "linux2" or platform == "unix":
		system("mkdir output")
		str(system( "mv " + h + ".jpg output"))
		print("Аватарка была сохранена в каталог output")
	elif platform == "win32":
		mkdir("output")
		str(system("move " + h + ".jpg output"))
		print("Аватарка была сохранена в каталог output")
except:
	print('500')
