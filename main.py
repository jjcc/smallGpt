import openai
import dotenv
import os

# Load environment variables from .env file
dotenv.load_dotenv()
API_KEY = os.getenv("OPENAI_API_KEY")

openai.api_key = API_KEY 

def generate_response(  mesages = [], model="gpt-3.5-turbo", temperature=0.7, max_tokens=150):
    
    
    response = openai.ChatCompletion.create(
        model=model,
        messages = mesages
        #prompt=prompt,
        #temperature=temperature,
        #max_tokens=max_tokens,
        #n=1,
        #stop=None,
        #echo=False,
    )

    message = response #.choices[0].text.strip()
    return message

# Example usage:
#input_text = "Tell me a joke."
input_messages = [
  { "role": "system",    "content": "You are a Python developer." },
  { "role": "user",      "content": "How to use OpenAI API ?", },
  { "role": "assistant", "content": "The openAI  library for python.", },
  { "role": "user",      "content": "How to send an openai api request" },
]

generated = generate_response(input_messages)
for choice in generated.get("choices", []):
    message = choice.get("message", "")
    print("role: ", message.get("role", ""))
    print("content: ", message.get("content", ""))