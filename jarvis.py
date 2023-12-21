# Importing ChatterBot
from chatterbot import ChatBot

# Import Google to text speech
import gtts
from playsound import playsound
import collections.abc

collections.Hashable = collections.abc.Hashable
import speech_recognition as sr
import openai

r = sr.Recognizer()


# Create object from ChatBot Class
bot = ChatBot(
    "Pepper",
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    database_uri="sqlite:///db.sqlite3",
    logic_adapters=["chatterbot.logic.BestMatch", "chatterbot.logic.TimeLogicAdapter"],
)


api_key = "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"
openai.api_key = api_key

# Basic Check for a response from jarvis
# response = bot.get_response('I need to make a complaint')
# print('Bot Response:', response)

# Full app instance
print(r"""\
              _          _            _          _          _            
        /\ \       /\ \         /\ \       /\ \       / /\          
       /  \ \     /  \ \       /  \ \     /  \ \     / /  \         
      / /\ \ \   / /\ \ \     / /\ \ \   / /\ \ \   / / /\ \        
     / / /\ \_\ / / /\ \_\   / / /\ \_\ / / /\ \_\ / / /\ \ \       
    / / /_/ / // /_/_ \/_/  / / /_/ / // / /_/ / // / /  \ \ \      
   / / /__\/ // /____/\    / / /__\/ // / /__\/ // / /___/ /\ \     
  / / /_____// /\____\/   / / /_____// / /_____// / /_____/ /\ \    
 / / /      / / /______  / / /      / / /      / /_________/\ \ \   
/ / /      / / /_______\/ / /      / / /      / / /_       __\ \_\  
\/_/       \/__________/\/_/       \/_/       \_\___\     /____/_/  
                                                                    
      """)

# Vocal greeting
tts = gtts.gTTS("Hello, My name is Peppa! And who might you be? ")
tts.save("greeting.mp3")
playsound("greeting.mp3")


# Grab Users name
 # use the microphone as source for input.
with sr.Microphone() as source2:
    
    # wait for a second to let the recognizer
    # adjust the energy threshold based on
    # the surrounding noise level 
    r.adjust_for_ambient_noise(source2, duration=0.2)
    
    #listens for the user's input 
    audio2 = r.listen(source2)
    
    # Using google to recognize audio
    name = r.recognize_google(audio2)
    print("I just heard ", name)

# Personal Greeting
greeting = "Hello! " + name
tts = gtts.gTTS(str(greeting))
tts.save("personal.mp3")
playsound("personal.mp3")


# Check if user requires speech
tts = gtts.gTTS("Do you need to hear my voice? Yes or no?")
tts.save("speech.mp3")
playsound("speech.mp3")

# Get Speech input
with sr.Microphone() as source2:
    
    # wait for a second to let the recognizer
    # adjust the energy threshold based on
    # the surrounding noise level 
    r.adjust_for_ambient_noise(source2, duration=0.2)
    
    #listens for the user's input 
    audio2 = r.listen(source2)
    
    # Using google to recognize audio
    speech = r.recognize_google(audio2)
    print("I just heard ", speech)

# Start Questions
if speech == "yes":
    tts = gtts.gTTS("and what is it I can help you with" + str(name) + " ?")
    tts.save("text.mp3")
    playsound("text.mp3")
print("What is it I can help you with today " + name + " ?")

while True:
    while(1): 
        request = ""   
        try:
         
        # use the microphone as source for input.
            with sr.Microphone() as source2:
                
                # wait for a second to let the recognizer
                # adjust the energy threshold based on
                # the surrounding noise level 
                r.adjust_for_ambient_noise(source2, duration=0.2)
                
                #listens for the user's input 
                audio2 = r.listen(source2)
                
                # Using google to recognize audio
                request = r.recognize_google(audio2)
                
                print("I just heard ", request)

                if request == "Goodbye" or request == "goodbye":
                    if speech == "yes":
                        tts = gtts.gTTS("Good bye")
                        tts.save("text.mp3")
                        playsound("text.mp3")
                    print("Pepper: Bye")
                    exit()
                else:
                    # Define the question or prompt
                    question = request
                    # Call the OpenAI GPT-3 API to generate a response
                    response = openai.Completion.create(
                        engine="text-davinci-003",  # You can experiment with different engines
                        prompt=question,
                        max_tokens=150,  # Adjust as needed
                        n=1,  # Number of completions to generate
                        stop=None  # You can provide a list of strings to indicate stopping criteria
                    )

                    # Extract and print the generated response
                    generated_response = response["choices"][0]["text"]
                    print("Pepper: ", generated_response)

                    if speech == "yes":
                        tts = gtts.gTTS(str(generated_response))
                        tts.save("text.mp3")
                        playsound("text.mp3")
    
                
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
    
    
