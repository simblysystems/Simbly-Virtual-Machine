from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    AI_API_KEY = os.getenv("AI_API_KEY")
    MODEL = os.getenv("MODEL")