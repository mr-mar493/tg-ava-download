from telethon import TelegramClient, events, sync
from os import system
from sys import platform
from random import choice

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

def main():
	key = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
	a = '@'
	for n in range(1):
		b=''
		for i in range(5):
			b += (choice(key))
			c=a+b

	clear()
	banner()
	id = input("Ваш api_id: ")
	apiez = input("Ваш api_hash: ")
	api_id = id
	api_hash = '{apiez}'
	client = TelegramClient('an', api_id, api_hash)
	client.start()
	try:
		client.download_profile_photo(c)
		client.send_message('@get_any_telegram_id_bot', c)
	except:
		print('500')
	main()

main()