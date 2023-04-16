from telethon import TelegramClient, events
import asyncio

# Replace YOUR_API_ID and YOUR_API_HASH with the API ID and API hash that you got from the Telegram website
api_id = 1235658


api_hash = "api hash"


# Replace YOUR_PHONE_NUMBER with your phone number (including the country code)
phone_number = 'YOUR_PHONE_NUMBER'

async def my_function():
  
    # await client.connect()
    # :

# Create a new TelegramClient instance and connect to Telegram
    client = TelegramClient("my_session", api_id, api_hash)
    await client.connect()

# Check if you're already logged in (if not, it will send you an authorization code via SMS)
    if not await client.is_user_authorized():
        await client.send_code_request(phone_number)
        await client.sign_in(phone_number, input("Enter the code you received via SMS: "))

# Replace YOUR_MESSAGE_HERE with the message you want to send
    message = "Wishing you a joyful and serene Easter. May this blessed day bring your home and life renewed hope, prosperity, and love, all through the gift of God\'s grace. Happy Easter. Let the resurrection of Jesus Christ instill hope, love, and serenity in your heart❤️🎉"

# Loop through all your chats and send the message to your friends
    chats = await client.get_dialogs()
    # print(chats)
    for chat in chats:
        if  chat.is_user and not chat.entity.bot :
            deleted_username = 'deleted_username'

# Delete the deleted account from your contact list
            # result = client(client.contacts_delete_contacts([deleted_username]))
            # print(result)
            await client.send_message(chat, message)

             
            try:
                 user = await client.get_entity(chat.entity.id)
                 print(user)

            except ValueError:
        # user was deleted
                    print('User is deleted')
                    print(chat)
             

# call the function
asyncio.run(my_function())