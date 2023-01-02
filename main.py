import openai

from dotenv import load_dotenv
load_dotenv()

import os

openai.api_key = os.environ.get('OPENAI_API_KEY')

def generate_message():
    word = "seat"
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt=generate_prompt(word),
        temperature=0.6,
    )
    return response

def generate_prompt(word):
    return """Suggest three word and a marketing message.

Word: happy
Message: Act the way you want to feel, Do not Be Afraid To Be Happy, Happiness Goes Where Happiness Is
Word: tall
Message: Practice safety at a height, The height of quality, We go to great heights for you
Word: {}
Message:""".format(
        word.capitalize()
    )

result = generate_message()
text = result.choices[0]['text']

def write_to_file(filename, output):
    with open(filename, 'a') as file:
        file.write(output + '\n')

write_to_file('output.txt', text)
