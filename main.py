import telebot

TOKEN = "8801002972:AAH-V4NyuFXRiZt2MgAssCQYmhXoj_9Fq_c"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message, "أهلاً بك! البوت يعمل الآن على سيرفر قوي ودائم 🚀")

@bot.message_handler(func=lambda message: True)
def reply_message(message):
    bot.reply_to(message, f"وصلتني رسالتك: {message.text}")

print("البوت يعمل الآن...")
bot.infinity_polling()
