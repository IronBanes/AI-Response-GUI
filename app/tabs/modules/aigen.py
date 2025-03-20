from openai import OpenAI
import dotenv
import os
import platform
from mistralai import Mistral

dotenv.load_dotenv()

client = OpenAI(api_key=os.getenv('OPENAI-KEY'))

class AiGenerate:
    def __init__(self):
        # Check if the system is Windows or macOS
        if platform.system() == "Windows" or platform.system() == "Darwin":
            current_dir = os.path.dirname(os.path.realpath(__file__))
            self.instructions1 = os.path.join(current_dir, "memory", "instructions.txt")
            self.instructions2 = os.path.join(current_dir, "memory", "instructions1.txt")
            self.instructions3 = os.path.join(current_dir, "memory", "instructions2.txt")
            self.filtered_words_path = os.path.join(current_dir, "memory", "filtered_words.txt")
            self.chat_log = os.path.join(current_dir, "memory", "chat_log.txt")
            self.ai_temperature = 0.5
        elif platform.system() == "Linux":
            self.instructions1 = "app/tabs/modules/memory/instructions.txt"
            self.instructions2 = "app/tabs/modules/memory/instructions1.txt"
            self.instructions3 = "app/tabs/modules/memory/instructions2.txt"
            self.filtered_words_path = "app/tabs/modules/memory/filtered_words.txt"
            self.chat_log = "app/tabs/modules/memory/chat_log.txt"
            self.ai_temperature = 0.5
        else:
            print(f"Unsupported platform: {platform.system()}")

    def get_instructions_from_file(self, value):
        if value == 1:
            with open(self.instructions1, 'r') as file:
                return file.read()
        elif value == 2:
            with open(self.instructions2, 'r') as file:
                return file.read()
        elif value == 3:
            with open(self.instructions3, 'r') as file:
                return file.read()

    def generate_response(self, prompt, value, gptversion):
        instructions = self.get_instructions_from_file(value)
        print(prompt)
        print(gptversion)
        if gptversion == "mistral":
            print("THIS IS MISTAL, POGGIES")
            api_key = os.environ["MISTRAL-KEY"]
            model = "mistral-large-latest"
            client = Mistral(api_key=api_key)

            chat_response = client.chat.complete(
                model = model,
                messages = [
                    {"role": "system", "content": "Below this line are your instructions to strictly follow.",},
                    {"role": "system", "content": instructions},
                    {"role": "system", "content": "Below this line is the prompt that you are formatting."},
                    {"role": "user", "content": prompt},
                    {"role": "user", "content": ""}
                ]
            )
            ai_response = chat_response.choices[0].message.content
            return ai_response
        else:
            response = client.chat.completions.create(model=gptversion,
            messages=[
                {"role": "system", "content": "Below this line are your instructions to strictly follow."},
                {"role": "system", "content": instructions},
                {"role": "system", "content": "Below this line is the prompt that you are formatting."},
                {"role": "user", "content": prompt},
                {"role": "user", "content": ""}
            ],
            temperature=self.ai_temperature)
            ai_response = response.choices[0].message.content
            return ai_response