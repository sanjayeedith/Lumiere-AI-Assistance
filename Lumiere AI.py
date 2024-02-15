
import os
import time
import pyaudio
import speech_recognition as sr
import pyttsx3
import playsound
from gtts import gTTS
import openai
import uuid

api_key = 'Your_API_KEY'
lang = 'en'

openai.api_key = api_key

guy = ""


def speak(text):
    tts = gTTS(text=text, lang=lang, slow=False, tld="com.au")
    temp_name = str(uuid.uuid4())
    tts.save(temp_name + ".mp3")
    playsound.playsound(temp_name + ".mp3", True)
    os.remove(temp_name + ".mp3")


def get_audio():
    global guy
    r = sr.Recognizer()
    with sr.Microphone(device_index=1) as source:
        try:
            print("Listening...")
            audio = r.listen(source, timeout=5)  # Adjust timeout as needed
            print("Processing...")
            said = r.recognize_google(audio)
            print(said)
            guy = said

            if "Jack" in said:
                new_string = said.replace("Jack", "")
                new_string = new_string.strip()
                completion = openai.Completion.create(
                    engine="text-davinci-003",
                    prompt=new_string,
                    max_tokens=100  # Adjust max_tokens as needed
                )
                engine = pyttsx3.init()
                engine.say(completion.choices[0].text)
                engine.runAndWait()

        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print(f"Error with the speech recognition service; {e}")

    return said


while True:
    if "stop" in guy:
        break

    get_audio()




# from openai import OpenAI


# api_key = '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'

# client = OpenAI()

# response = client.chat.completions.create(
#   model="gpt-3.5-turbo",
#   messages=[
#     {"role": "system", "content": "You are a helpful assistant."},
#     {"role": "user", "content": "Who won the world series in 2020?"},
#     {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
#     {"role": "user", "content": "Where was it played?"}
#   ]
# )

# print(response['choices'][0]['message']['content'])