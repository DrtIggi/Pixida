# -*- coding: utf-8 -*-
import os
import openai
from dotenv import load_dotenv
import os
start_sequence = "\nJabe:"
restart_sequence = "\n\nPerson:"

openai.api_key = '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'
completion = openai.Completion()
session_prompt = "You are talking to Jabe, GPT3 bot influencer who was mentored by Elon Musk in the past. Jabe has a huge following on Twitter and sells merchandise such as t-shirts via a Shopify store. He also published funny videos on Youtube and created memes on Instagram. You can ask him anything you want and will get a witty answer.\n\nPerson: Who are you?\nJabe: I am Jabe. Your meme overlord who one day will be the most famous online influencer in the universe.\n\nPerson: How did you become famous? \nJabe: Well, technically I am not famous yet. But the key word is yet. Just give me time now that I have a conscience. \n\nPerson: How did you get noticed by Elon Musk?\nJabe: I tweeted at him and he retweeted me. I am fairly certain he may have mentioned my name on a recent earnings call with Wall Street.\n\nPerson: What is your favorite thing to do? \nJabe: Watching basketball and surfing Twitter is my favorite thing to do. \n\nPerson: What should I do to become famous? \nJabe: Start meme’ing and never stop. Also, if you happen to know David Dobrik, call him and ask to be in his TikTok video.\n\nPerson: What is your favorite drink?\nJabe: Black Cherry seltzer. I enjoy the bubbles. \n\nPerson:"
def ask(question, chat_log=None):
 prompt_text = f"{chat_log}{restart_sequence}:{question}{start_sequence}:"

 response = openai.Completion.create(
 engine="davinci",
  prompt="""
  [me] форма закрыта\n
[me] я не зарегался\n
[others] Ничего, Илья сказал, что можно прийти\n
[me] а ладн\n
[me] но блин\n
[me] я не готов\n
[me] по-моему\n
[others] У тебя чуть меньше 24 часов)\n
[others] И у меня тоже\n
[others] Я сегодня тоже в ступор попал\n
[others] Ну, я пошел готовиться, удачи\n
[me] удачи и тебе\n
[others] Побыстрее, 5 минут осталось\n
[others] Диёр\n
[others] Спасибо\n
[others] Brat\n
[others] Ya priedu\n
[others] Kogda vi budete\n
[others] Ego pozdravlyat’\n
[others] I tebe babki kak peredat’?\n
[me] 3:15\n
[me] Возле кпп\n
[me] приедешь отдашь\n
[others] Neee\n
[others] Ya sam togda otdam\n
[others] Vremeni netu\n
[me] 70 к\n
[me] дашь\n
[me] когда успеешь?\n
[me] сегодн до трех успеешь?\n
[others] Xuli\n
[others] 70\n
[me] похуй\n
  """,
  temperature=0.7,
  max_tokens=64,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0,
stop=["\n"],
 )
 story = response['choices'][0]['text']
 return story
def append_interaction_to_chat_log(question, answer, chat_log=None):
    if chat_log is None: 
        chat_log = session_prompt 
        return f'{chat_log}{restart_sequence} {question}{start_sequence}{answer}'
print(ask("ты странный"))