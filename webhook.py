from http.server import BasedHTTPRequestHandler
import os
import json
import asyncio
import requests
import datetime
from telebot.async_telebot import AsyncTeleBot
from telebot import types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
BOT_TOKEN = os.environ.get('BOT_TOKEN')
bot = AsyncTeleBot(BOT_TOKEN)

def generate_start_keyboard():
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton("Open TestCoin APP", web_app=WebAppInfo(url="https://react-6meevm.chbk.app/")))
    return keyboard

    @bot.message_handler(commands=['start'])
    async def start(message):
        user_id = str(message.from_user.id)
        user_first_name = str(message.from_user.first_name)
        user_last_name = message.from_user.last_name
        user_username = message.from_user.username
        user_language_code = str(message.from_user.language_code)
        is_premium = message.from_user.is_premium
        text = message.text.split()
        welcome_message = (
            f"hi,{user_first_name}"
            f"welcome"
        )


       user_data = {
        'first_name': user_first_name,
        'last_name': user_last_name,
        'username': user_username,
        'languageCode': user_language_code,
        'isPremium': is_premium,
        'referrals':{},
        'balance':0,
        'mineRate': 0.001,
        'isMining': False,
       }

       keyboard = generate_start_keyboard()
       await bot.reply_to(message,welcome_message,reply_markup=keyboard)
       except Exception as e:
        error_message = "Error.Try again"
        await bot.reply_to(message,error_message)
        print(f"Error:{str(e)}")

        class Handler(BasedHTTPRequestHandler):
            def do_POST(self):
                content_length = int(self.headers['Content-Length'])
                post_data = self.rfile.read(content_length)
                update_dict = json.loads(post_data.decode('utf-8'))

                asyncio.run(self.process_update(update_dict))

                self.send_response(200)
                self.end_headers()

                async def process_update(self, update_dict):
                    update = types.Update.de_json(update_dict)
                    await bot.process_new_updates([update])
                    
                    def do_GET(self):
                        self.send_response(200)
                        self.end_headers()
                        self.wfile.write("Bot is running".encode())
                        