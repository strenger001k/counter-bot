from bot import bot

@bot.message_handler(commands=['start'])
def send_welcome(message):
    # username = message.from_user.username
    bot.reply_to(message, "hi!!!")
    # bot.send_message(message, "hi!!!")
