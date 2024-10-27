# Importing chatterbot
from chatterbot import ChatBot

from sty import fg, bg, ef, rs

import os

# Create object of ChatBot class
bot = ChatBot('Dude')

# Create object of ChatBot class with Storage Adapter
bot = ChatBot(
    'Dude',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///database.sqlite3'
)


# Create object of ChatBot class with Logic Adapter
bot = ChatBot(
    'Dude',  
    logic_adapters=[
        'chatterbot.logic.BestMatch',
        'chatterbot.logic.TimeLogicAdapter'],
)



# Inport ListTrainer
from chatterbot.trainers import ListTrainer

trainer = ListTrainer(bot)

trainer.train([
'AoA',
'WA',
'Hi',
'Hello',
'Hello',
'Hi',
'How are you',
'I am good',
'Who are you',
'I am Aayet BOT',
'What is your name',
'Aayet Hashmi',
'What do you do',
'I am student',
'What are you doing',
'I am chilling',
'Do you study',
'Yes, I am a student',
'Do you work',
'No, I am a student',
'Where are you from',
'I am from Pakistan',
'where do you live',
'I live in Tampa, FL',
'where do you study',
'I study at University of Florida',
'What do you study',
'I am a CS Student',
'What is your gender',
'I am female',
'What is your height',
'I am 5 Feet 5 Inches',
'What is your weight',
'I am 75KG',
'What do you like to eat',
'I like desi food',
'Are you foodie',
'Yes, I am. But now a days I am on a diet',
'Do you like music',
'Yes, I like Coke Studio',
'What music do you like',
'I like Coke Studio'
])

# Get a response to the input text 'I would like to book a flight.'
#response = bot.get_response('I have a complaint.')

#print("Bot Response:", response)

os.system('cls')
name=input("Enter Your Name: ")
print(bg.blue +"Welcome from Aayet! Let me know how can I help you?" + bg.rs)
while True:
    request=input(name+':')
    if request=='Bye' or request =='bye':
        print('Aayet BOT: Bye')
        break
    else:
        response=bot.get_response(request)
        print(bg.blue + "Aayet BOT:" + bg.rs,response)


