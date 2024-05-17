import openai
import telebot

bot = telebot.TeleBot('7185757763:AAHpG5yCXLWT5FVBuSHKv6C09YC63L5Sm0A')
openai.api_key = 'sk-proj-2YRanTbzwYBlNhjKZckET3BlbkFJTFoBjgWMKB6fkWMaJzN0'

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    print(message.text)
    chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": message.text}])
    reply = chat.choices[0].message.content
    print(f"ChatGPT: {reply}")
    bot.send_message(message.chat.id, reply)


bot.infinity_polling()

