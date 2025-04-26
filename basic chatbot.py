!pip install pyvirtualdisplay
!apt-get install -y xvfb
!python -m pip install tk
!pip install nltk

import nltk
from nltk.chat.util import Chat, reflections

nltk.download('punkt')
nltk.download('wordnet')

#define some patterns and responses
patterns = [
    (r'hi|hello|hey', ['Hello!', 'Hi there!', 'Hey!']),
    (r'how are you?', ['I\'m good, thank you!', 'I\'m doing well, thanks for asking.']),
    (r'what is your name?', ['You can call me ChatGPT.', 'I go by the name ChatGPT.']),
    (r'(.*) your name?', ['You can call me ChatGPT.', 'I go by the name ChatGPT.']),
    (r'can you recommend a book?|show me a book',['Is it ok with Deep Learning', 'shall I go with Gen AI','Can I show ANN']),
    (r'(.*) Go for a tea?', ['Ya Sure.', 'Not Now, May be Later.', 'With Pleasure'])

]

chatbot = Chat(patterns, reflections)

# start conversation
print("Hello! I'm Perry. How can I help you today?")
while True:
    user_input = input("You: ")
    response = chatbot.respond(user_input)
    print("Perry:", response)
