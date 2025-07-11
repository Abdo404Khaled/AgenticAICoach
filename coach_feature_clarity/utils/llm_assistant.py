import os
from dotenv import load_dotenv
from crewai import LLM

# Load .env file
load_dotenv()

# Initialize the LLM
llm = LLM(
    model="openai/gpt-3.5-turbo",
    api_key=os.getenv("OPENAI_API_KEY"),
    temperature=0.5)
