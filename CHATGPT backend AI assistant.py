

import pyttsx3 as p
import speech_recognition as sr
import openai
import cv2

# Initialize text-to-speech engine
engine = p.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# Set up OpenAI API
openai.api_key = input("Enter the key")



# Function to interact with ChatGPT
def chat_with_model(prompt):
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=50
    )
    return response.choices[0].text.strip()

# Function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Initialize speech recognition
r = sr.Recognizer()
flag = 1

# Main loop for speech interaction
while True:
    print("Enter option: \n")
    print("1. Continue 2. Quit")
    n = int(input("Enter your option: "))
    if(n==2):
        flag =0
        break
    
    print("I'm listening...")
    
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        
        try:
            instruction = r.recognize_google(audio)
            print("Instruction:", instruction)
            
            if instruction.lower() == "stop":
                break
            
            response = chat_with_model("User: " + instruction)
            print("ChatGPT:", response)
            
            speak(response)
            
        except sr.UnknownValueError:
            print("Sorry, I didn't catch that. Can you please repeat?")
        except sr.RequestError as e:
            print("An error occurred. Please check your internet connection.")
        if cv2.waitKey(1) & 0xFF == ord('q'):
           print ("stopping")
           break


# End of speech interaction

# Text-based interaction loop
if flag ==1:
    user_input = input("User: ")

    while user_input.lower() != 'stop':
        response = chat_with_model("User: " + user_input)
        print("ChatGPT: " + response)
        speak(response)
        user_input = input("User: ")
        

