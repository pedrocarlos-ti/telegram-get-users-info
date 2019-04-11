from telethon import TelegramClient, sync

api_id = 'YOUR_TELEGRAM_ID'
api_hash = 'YOUR_TELEGRAM_HASH'
client = TelegramClient('YOUR_PHONE_NUMBER', api_id, api_hash)
client.start()

with client:
    # Set USER_ID or GROUP_ID or CHANNEL_ID above
    results = client.get_participants('@username', aggressive=True)
    print(str(len(results)) + ' found users')

    users = []
    
    for result in results:
      print (str(result.id) + ' - ' + result.first_name)