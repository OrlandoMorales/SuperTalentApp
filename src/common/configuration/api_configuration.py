from dotenv import load_dotenv, dotenv_values 
from src.common.configuration.app_configuration import AppConfiguration
from pydantic import BaseModel
import os

load_dotenv()

class ApiConfiguration(BaseModel):
    POST:str = "POST"
    GET:str = "GET"
    BASE_EIGHTFOLD_API_ADDRESS: str = os.environ.get("BASE_EIGHTFOLD_API_ADDRESS")
    AUTHENTICATE: str = "/oauth/v1/authenticate"
    MATCH_CANDIDATE: str = "/api/v2/core/positions/{0}/matched-candidates?{1}"
    PROFILE_DETAILS: str = "/api/v2/core/profiles/{0}"
    POSITION_DETAILS: str = "/api/v2/core/positions/{0}"
    

