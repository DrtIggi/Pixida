import telebot, sqlite3


token = '2117240577:AAF1McmhAsPNTfrMh3BDeRojzDe_K50r4XY'

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Hi!")

@bot.message_handler(content_types=['text'])
def text(message):
    bot.send_message(message.chat.id, message.text)

if __name__ == "__main__":
    bot.polling()
