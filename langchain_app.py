from langchain.llms import OpenAI
import dotenv
import os

# Load environment variables from .env file
dotenv.load_dotenv()
API_KEY = os.getenv("OPENAI_API_KEY")

class Agent:
    def __init__(self, key, temperature,model="gpt-3.5-turbo"):
        self.llm = OpenAI(openai_api_key=key, temperature=temperature)

    def generate_response(self,  mesages = [] ):# , model="gpt-3.5-turbo", temperature=0.7, max_tokens=150):
        response = self.llm.predict(mesages)
        return response

#llm = OpenAI(openai_api_key=API_KEY, temperature=0.9)
#llm = OpenAI(temperature=0.9)



a = Agent(API_KEY, 0.9)

ans = a.generate_response("What would be a good company name for a company that makes colorful socks?")

print(ans)