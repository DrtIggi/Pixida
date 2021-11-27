import telebot, openai, time
import os, sqlite3
from telebot import types
token = '2117240577:AAF1McmhAsPNTfrMh3BDeRojzDe_K50r4XY'
bot = telebot.TeleBot(token)


def registration(message):
    conn = sqlite3.connect("db.db")
    cursor = conn.cursor()
    cursor.execute(f"insert into main values ({message.chat.id}, 0, 0)")
    conn.commit()
    conn.close()

@bot.message_handler(commands=['start'])
def start(message):

    conn = sqlite3.connect("db.db")
    cursor = conn.cursor()
    res = cursor.execute("SELECT * FROM main WHERE chat_id = "+str(message.chat.id)).fetchone()
    conn.close()
    if res== None:
        registration(message)
    
    introduction(message)


def add_num(message):
    conn = sqlite3.connect('db.db')
    cursor = conn.cursor()
    res = cursor.execute(f"SELECT num FROM main WHERE chat_id = {str(message.chat.id)}").fetchone()
    count_result=0
    array = parser()
    for x in message.text.split(' '):
        if x.lower() in array:
            count_result+=array[x.lower()]


    if(res[0] == 10):
        cursor.execute(f"UPDATE main SET num = 0 WHERE chat_id = {str(message.chat.id)}")
        s = cursor.execute(f"SELECT count FROM main WHERE chat_id = {str(message.chat.id)}").fetchone()[0]
        cursor.execute(f"UPDATE main SET count = 0 WHERE chat_id = {str(message.chat.id)}")
        conn.commit()
        conn.close()
        return s+count_result
    else:
        cursor.execute(f"UPDATE main SET num = num + 1 WHERE chat_id = {str(message.chat.id)}")
        cursor.execute(f"UPDATE main SET count = count + {count_result} WHERE chat_id = {str(message.chat.id)}")
        conn.commit()
        conn.close()
        return None

@bot.message_handler(content_types=['text'])
def text(message):
    
    global chat_log
    answer = ask(message.text, session_prompt)
    # chat_log+=append_interaction_to_chat_log(message.text, answer, chat_log)
    bot.send_message(message.chat.id, answer)
    cou = add_num(message) 
    if cou != None:
        if cou >= 5:
            bot.send_message(message.chat.id, "I am so glad that i helped you!!!")
        elif cou <= 5:
            bot.send_message(message.chat.id, "If you are feeling unwell, you can visit this website.: https://....")

openai.api_key = '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'
completion = openai.Completion()
start_sequence = "\nDiyor:"
restart_sequence = "\n\nPerson:"
session_prompt = "Person: Hi\nDiyor: Hi there!\n\nPerson: How are you?\nDiyor: I am fine, thx\n\nPerson: How old are you?\nDiyor: i am 20 years old\n\nPerson: What is your favorite color?\nDiyor: blue\n\nPerson: Can you please help me?\nDiyor: Yes, of course!\n\nPerson: Do you like me?\nDiyor: Yeah!!!!\n\nPerson: I am tired\nDiyor: Can you tell me what's happened?\n\nPerson: Did u play mario??\nDiyor: Yeah, i did\n\nPerson: What time is it?\nDiyor: It is 12:00\n\nPerson: Nice to meet u!!\nDiyor: Me too!!\n\nPerson: I need a help!\nDiyor: here is the link:..."

def ask(question, chat_log=None):
 prompt_text = f'{session_prompt}{restart_sequence}{question}{start_sequence}'
 response = openai.Completion.create(
 engine="ada",
  prompt=prompt_text,
  temperature=0.5,
  max_tokens=64,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0,
 stop=["\n"],
 )
 story = response['choices'][0]['text']
 return str(story)

def append_interaction_to_chat_log(question, answer, chat_log=None):
    if chat_log == '': 
        chat_log = session_prompt 
    return f'{chat_log}{restart_sequence} {question}{start_sequence}{answer}'

def parser():
    array = {}
    with open('AFINN-165.txt', 'r') as f:
        for x in f.readlines():
            array[x.strip('\n').split('\t')[0]] = int(x.strip('\n').split('\t')[1])
        # array.append(x.strip('\n').split('\t'))
    return array

def introduction(message):
    text_1 = "Hello, I am a digital Pflegeberater. I am not a HUMAN but I am HUMANIZED and try to be EMPATHETIC."
    text_2 = "I can help in ypur situation. I can provide information on Pflegeversicherung. *You can choose a theme or just write me a message!*"
    keyboard = types.InlineKeyboardMarkup()
    button_bloodtest = types.InlineKeyboardButton(text='I need nursing care', callback_data='need_care')
    keyboard.add(button_bloodtest)
    button_events = types.InlineKeyboardButton(text='Nursing care degree increased', callback_data='degrees_increased')
    keyboard.add(button_events)
    button_medicaments = types.InlineKeyboardButton(text='Benefits', callback_data='benefits')
    keyboard.add(button_medicaments)
    button_insurance = types.InlineKeyboardButton(text='Support amount', callback_data='sa')
    keyboard.add(button_insurance)
    bot.send_message(message.chat.id, text_1)
    bot.send_message(message.chat.id, text_2, reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_register(call):
    if call.data == 'need_care':
        need_care(call.message)
    elif call.data == 'degrees_increased':
        pass
    elif call.data == 'benefits':
        pass
    elif call.data == 'sa':
        pass
    elif call.data == 'Apply for care degree':
        pass
    elif call.data == 'Advise on care':
        advise_on_care(call.message)
    elif call.data == 'Need of care':
        need_care(call.message)
    elif call.data == 'Pflegegrad beantragen':
        pflegegrad_beantragen(call.message)
        
    
   


def need_care(message): 

    text_3 = "I know that new Pflegesituation brings many questions. The first important point is to fill in the application for the Pflegegrad."
    text_4 = "With the application you are able to acquire free Pflegeberatung. Pflegekasse will provide you a Pflegeberater"
    keyboard = types.InlineKeyboardMarkup()
    button_bloodtest = types.InlineKeyboardButton(text='Apply for care degree', callback_data='Apply for care degree')
    keyboard.add(button_bloodtest)
    button_events = types.InlineKeyboardButton(text='Advice on care', callback_data='Advise on care')
    keyboard.add(button_events)
    button_medicaments = types.InlineKeyboardButton(text='Need of care', callback_data='Need of care')
    keyboard.add(button_medicaments)
    
    bot.send_message(message.chat.id, text_3)
    bot.send_message(message.chat.id, text_4, reply_markup=keyboard)

def need_of_care(message):
    text_11 = "Persons are in need of nursing care when they cant be self-dependent due to health issues. Then they need help of other people"
    bot.send_message(message.chat.id, text_11)

def advise_on_care(message):
    text_6 = "Pflegekassen are obliged to provide advice on Pflege for insured people. You are always eligible to organise an individual appointment for advice"
    bot.send_message(message.chat.id, text_6)


def pflegegrad(message):
    text_7 = "Pflegegrad can be submited via e-mail, post, telephone, or online through Pflegekasse. Pflegekass will provide you further information and an appointment."
    text_8 = "Pflegegrad defines the degree of self-dependence."
    keyboard = types.InlineKeyboardMarkup()
    button_bloodtest = types.InlineKeyboardButton(text='Pflegegrad beantragen', callback_data='Pflegegrad beantragen')
    keyboard.add(button_bloodtest)
    bot.send_message(message.chat.id, text_7)
    bot.send_message(message.chat.id, text_8, reply_markup=keyboard)


def pflegegrad_beantragen(message):
    text_9 = "Pflegegrad 1 --------------------\n\nPflegegrad 2 --------------------\n\nPflegegrad 3 --------------------\n\nPflegegrad 4 --------------------\n\nPflegegrad 5 --------------------\n\n" 
    bot

    bot.send_message(message.chat.id, text_9)


def infinite_button(message):
    text_5 = "Just write me any message anytime. I will try to answer, because I am HUMANIZED"
    keyboard = types.ReplyKeyboardMarkup()
    button_settings = types.KeyboardButton(text_5)
    keyboard.add(button_settings)
    bot.send_message(message.chat.id, "", keyboard)
def polling():
    try:
        bot.polling(timeout=2)
    except Exception as f:
        time.sleep(5)
        print(f)
        polling()


if __name__ == '__main__':
    polling()
