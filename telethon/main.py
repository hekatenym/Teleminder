from telethon import TelegramClient,events
import datetime
# import logging
# logging.basicConfig(format='%(asctime)s %(message)s')

api_id = 
api_hash = 

client = TelegramClient('test', api_id, api_hash, proxy=("socks5", '127.0.0.1', 7890))

# 消息监控，保活
@client.on(events.NewMessage(incoming=True,chats=[]))
async def handler(event):
    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " " +str(event.message.peer_id)+" "+str(event.message.from_id)+" "+str(event.message.message))

# 消息提醒
@client.on(events.NewMessage(incoming=True,from_users=[]))
async def forward_to_me(event):
    await client.send_message('me', str(event.message.peer_id)+" "+str(event.message.from_id)+" "+str(event.message.message))
    print("消息转发成功")

client.start()
client.run_until_disconnected()