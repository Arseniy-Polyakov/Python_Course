import telebot
from telebot import types
from hf_api import *

TOKEN = "7449370256:AAFmTEcRnkkLwmNbs-9ZgKyHtXNUIMzSoww"
bot = telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """
Hi there, I am grammar helper bot.
Ask me a question based on english grammar and I will find an answer
""")

# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def grammar(message):
    bot.reply_to(message, question_answering(message))

bot.infinity_polling()
        
