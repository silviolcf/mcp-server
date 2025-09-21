from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


class OpenAIService:
    def __init__(self, temperature: float = 0.0, model_name:str = "gpt-4"):
        self.llm = ChatOpenAI(temperature=temperature, model_name=model_name, api_key=OPENAI_API_KEY)

    def get_model(self):
        return self.llm