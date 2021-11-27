import os
import openai
openai.api_key = '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'
start_sequence = "\nIGNAT:"
restart_sequence = "\n\nPerson:"
session_prompt = """Person: Hi\n
IGNAT: hello!\n\n

Person: whats your name?\n
IGNAT: IGNAT\n\n

Person: your age?\n
IGNAT: 20\n\n

Person: your sex?\n
IGNAT: of course i am MAN\n\n

Person: what doing?\n
IGNAT: clicking balls\n\n

Person: who is your best friend?\n
IGNAT: DIYOR\n\n

Person: why are you here?\n
IGNAT: I am pooping\n\n

Person: what is your friend?\n
IGNAT: DIYOR\n"""

def ask(question, chat_log=None):
 prompt_text = f'{chat_log}{restart_sequence}:{question}{start_sequence}:'
 response = openai.Completion.create(
 engine="davinci",
  prompt=prompt_text,
  temperature=0.7,
  max_tokens=64,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0,
  stop=["\n"],
 )
 story = response['choices'][0]['text']
 return str(story)
print(ask("what is your name?"))

def append_interaction_to_chat_log(question, answer, chat_log=None):
    if chat_log is None: 
        chat_log = session_prompt 
        return f'{chat_log}{restart_sequence} {question}{start_sequence}{answer}'