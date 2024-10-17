from pyrogram import Client,filters
from pyrogram.handlers import MessageHandler
import time

# api_id = 
# api_hash = ""
# proxy = {
#      "scheme": "socks5",  # "socks4", "socks5" and "http" are supported
#      "hostname": "127.0.0.1",
#      "port": 7890,
#  }

app = Client("my_account", proxy=proxy, api_id=api_id, api_hash=api_hash)

# async def main():
    # async with app:
        # 获取聊天记录列表
        # async for dialog in app.get_dialogs(limit=20):
            # print( "ID:" + str(dialog.chat.id) + " 名字：" + str(dialog.chat.first_name or dialog.chat.title))
        
        # 获取今天发送的所有聊天记录
        # chat_list = []
        # for id in chat_list:
        #     async for message in app.get_chat_history(chat_id=id,offset_date=datetime.datetime.today()):
        #         if message.from_user.is_self == 1:
        #             print(message.text)

        

@app.on_message()
async def send_to_me(client, message):
    print("1")
    print(str(message.chat.id) + " " + str(message.from_user.id) + " " + str(message.from_user.username)  + " " + str(message.text))
    # 消息白名单
    # white_list = []
    # if message.from_user.username in white_list:
        # await app.send_message("me", str(message.from_user.id) + " " + str(message.from_user.username)  + " " + str(message.text))
        
app.run()


