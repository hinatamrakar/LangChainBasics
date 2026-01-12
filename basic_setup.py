import os
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Set API key

# Initialize model
llm = ChatOpenAI(temperature=0.7, model="gpt-4o-mini")

response = llm.invoke("explain python in one sentence")

print(response.content)