from telethon import TelegramClient, events, sync
api_id =  
api_hash = ''
client = TelegramClient('an', api_id, api_hash)
client.start()
from t import c
try:
    client.download_profile_photo(c)
    client.send_message('@get_any_telegram_id_bot', c)
except:
    print('500')
