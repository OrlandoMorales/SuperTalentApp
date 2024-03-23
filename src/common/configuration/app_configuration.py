from dotenv import load_dotenv, dotenv_values 
from pydantic import BaseModel
import os

load_dotenv()

class AppConfiguration(BaseModel):
    USERNAME: str = os.environ.get("USERNAME")
    PASSWORD: str = os.environ.get("PASSWORD")
    AUTHORIZATION_BASIC: str = os.environ.get("AUTHORIZATION_BASIC")
    AUTHORIZATION_BEARER: str = os.environ.get("AUTHORIZATION_BEARER")
    TOKEN_BEARER: str = os.environ.get("TOKEN_BEARER")
    MESSAGES_SEND_INTERVAL : str = os.environ.get("MESSAGES_SEND_INTERVAL")
    SLACK_TOKEN: str = os.environ.get("SLACK_TOKEN")
    SLACK_BOT: str = os.environ.get("SLACK_BOT")
    
    