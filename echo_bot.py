import telebot

bot = telebot.TeleBot("975266287:AAEA1OUtbyPTCtjX8YvanxbjOSEG6HJN-Hk")


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Hello, send me something and i'll answered you")


@bot.message_handler(content_types=['text'])
def send_echo(message):
    bot.send_message(message.chat.id, message.text)


bot.polling(none_stop=True)
