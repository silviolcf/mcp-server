from langchain_openai import ChatOpenAI

class OpenAIService:
    def __init__(self, temperature: float = 0.0, model_name:str = "gpt-4"):
        self.llm = ChatOpenAI(temperature=temperature, model_name=model_name)

    def get_model(self):
        return self.llm