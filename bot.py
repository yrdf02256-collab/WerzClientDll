
import os
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

TOKEN = os.environ["TOKEN"]
SITE = "https://yrdf02256-collab.github.io/WerzClientDll/"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    markup = InlineKeyboardMarkup()
    button = InlineKeyboardButton(
        "🚀 Открыть WerzClientDLL",
        web_app=WebAppInfo(url=SITE)
    )
    markup.add(button)

    bot.send_message(
        message.chat.id,
        "👋 Добро пожаловать в WerzClientDLL!\n\n"
        "Нажми кнопку ниже, чтобы открыть приложение.",
        reply_markup=markup
    )

bot.infinity_polling()
