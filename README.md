# Lumiere-AI-Assistance

## Project Description ## 

lumiere is a voice-activated virtual assistant powered by OpenAI's powerful language models. It listens for commands or questions preceded by the wake word "Lumiere", processes them with OpenAI, and provides informative text-to-speech responses.

## Features ##

Voice Recognition: Transcribes voice commands into text.
OpenAI Integration: Leverages OpenAI's capabilities for question answering, summarization, and various text generation tasks.
Text-to-Speech: Delivers AI-generated responses in a natural voice.
Customizable Wake Word: Responds to the word "Lumiere" (can be changed in the code).

**Prerequisites**

* Python 3.x
* List the required Python libraries:
* pyaudio
* speech_recognition
* pyttsx3
* playsound
* gtts
* openai
* uuid
* 
 ## Install dependencies: ##
 
**Bash**

* pip install -r requirements.txt
Use code with caution. Learn more

**Obtain an OpenAI API Key**

* Sign up for a free OpenAI account at https://beta.openai.com/signup/.
* Go to your API keys: https://beta.openai.com/account/api-keys.
Create a new secret key and copy it.

**Usage**

* In the Python script, replace the placeholder api_key variable with your actual OpenAI API key.
Run the project:

 ## Bash ##

* python Lumiere.py
* Use code with caution. Learn more
Say "Lumiere" followed by your question or command. The assistant will process your request and provide a spoken response.
