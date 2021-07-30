# Importing ChatterBot
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

# Import Google to text speech
import gtts
from playsound import playsound

# Create object from ChatBot Class
bot = ChatBot(
    "Pepper",
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///db.sqlite3',
    logic_adapters=[
        'chatterbot.logic.BestMatch',
        'chatterbot.logic.TimeLogicAdapter'
    ]
    )

# Creates an instance of the trainer    
lessons = ListTrainer(bot)
corpus = ChatterBotCorpusTrainer(bot)

# Simple statements to teach the bot
lessons.train([
    'Hi',
    'Hello',
    'Good Morning',
    'Good Morning',
    'What is your name',
    'My Name is pepper',
    'What is your name',
    'Ahh thats a nice name, what are you doing today?',
    'Im working and you',
    'Im a bot I do nothing but wait for you, can I help you with something?',
    'Can you tell me a joke',
    'What do you call a fish wearing a bowtie?" "Sofishticated',
    'Thank you',
])

corpus.train(
    "chatterbot.corpus.english.greetings",
    "chatterbot.corpus.english.conversations"
)

# Basic Check for a response from jarvis
#response = bot.get_response('I need to make a complaint')
#print('Bot Response:', response)

# Full app instance

# Vocal greeting
tts = gtts.gTTS("Hello, I'm Pepper! Please tell me your name? ")
tts.save('greeting.mp3')
playsound('greeting.mp3')

# Grab Users name
name=input("Hello, I'm Pepper! Please tell me your name? ")

#Personal Greeting
greeting = "Hello! " + name
tts = gtts.gTTS(str(greeting))
tts.save('personal.mp3')
playsound('personal.mp3')


# Check if user requires speech
tts = gtts.gTTS("Do you need to hear me? Yes or no?")
tts.save('speech.mp3')
playsound('speech.mp3')

#Get Speech input
speech=input("Do you need to hear me? Yes or no?")
speech = speech.lower()

#Start Questions
if speech == 'yes':
        tts = gtts.gTTS("What is it I can help you with today " + str(name) +" ?")
        tts.save('text.mp3')
        playsound('text.mp3')
print("What is it I can help you with today " + name +" ?")

while True:
    request=input(name+': ')
    if request == 'Bye' or request == 'bye':
        if speech == 'yes':
            tts = gtts.gTTS("Good bye")
            tts.save('text.mp3')
            playsound('text.mp3')
        print('Pepper: Bye')
        break
    else: 
        response=bot.get_response(request)
        print('Pepper: ', response) 

        if speech == 'yes':
            tts = gtts.gTTS(str(response))
            tts.save('text.mp3')
            playsound('text.mp3')