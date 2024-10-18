import telebot
import os
from random import choice
import random

coins = 0
bot_coins = 0

API_TOKEN = ''

bot = telebot.TeleBot(API_TOKEN)

# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am EchoBot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
""")
    
@bot.message_handler(commands=['coins'])
def send_message(message):
    coins = random.randint(3, 18)
    bot_coins = random.randint(3, 18)
    if coins  > bot_coins:
        bot.reply_to(message, f"You have {coins} coins! You have more than me, {bot_coins} coins!")
        bot.reply_to(message,  "You win!")
    elif coins < bot_coins:
        bot.reply_to(message, f"You have {coins} coins! I have more than you, {bot_coins} coins!")
        bot.reply_to(message,  "You lose!")
    else:
        bot.reply_to(message, f"You have {coins} coins! We have the same amount of coins, {bot_coins}!")
        bot.reply_to(message,  "It's a tie!")

@bot.message_handler(commands=['mem'])
def send_mem(message):
    with open(f'images/{choice(os.listdir("images"))}', 'rb') as f:  
        bot.send_photo(message.chat.id, f)  

# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)

bot.infinity_polling()