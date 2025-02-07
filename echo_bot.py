import telebot

bot = telebot.TeleBot("API Key")


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Hello, send me something and I'll answered you")


@bot.message_handler(content_types=['text'])
def send_echo(message):
    bot.send_message(message.chat.id, message.text)


bot.polling(none_stop=True)
