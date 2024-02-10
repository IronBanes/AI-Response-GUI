# created by DW for original project:
import openai
import dotenv
import os

dotenv.load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI-KEY')

openai.api_key = OPENAI_API_KEY


instructions1 = "./memory/instructions.txt"
instructions2 = "./memory/instructions1.txt"
instructions3 = "./memory/instructions2.txt"
filtered_words_path = "./memory/filtered_words.txt"
chat_log = "./memory/chat_log.txt"
ai_temperature = 0.5

def get_instructions_from_file(value):
    if value == 1:
        with open(instructions1, 'r') as file:
            return file.read()
    elif value == 2:
        with open(instructions2, 'r') as file:
            return file.read()
    elif value == 3:
        with open(instructions3, 'r') as file:
            return file.read()

def generate_response(prompt, value):
    instructions = get_instructions_from_file(value)
    print(prompt)
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-1106",
        messages=[
            {"role": "system", "content": "Below this line are your instructions to strictly follow."},
            {"role": "system", "content": instructions},
            {"role": "system", "content": "Below this line is the prompt that you are formatting."},
            {"role": "user", "content": prompt},
            {"role": "user", "content": ""}
        ],
        temperature=ai_temperature
    )
    ai_response = response['choices'][0]['message']['content']
    return ai_response