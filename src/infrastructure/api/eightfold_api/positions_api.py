import json
import os
from typing import List
from pydantic import parse_obj_as
from src.infrastructure.api.eightfold_api.api_client import ApiClient
from src.common.configuration.app_configuration import AppConfiguration
from src.common.configuration.api_configuration import ApiConfiguration
from src.common.log.messages_util import MessagesUtilities
from src.infrastructure.api.eightfold_api.rest_client import RestClient


class PositionApi:
    
    apiConfig = ApiConfiguration()
    appConfig = AppConfiguration()
    messageUtil = MessagesUtilities()

    rest_client = RestClient(apiConfig.BASE_EIGHTFOLD_API_ADDRESS, appConfig.TOKEN_BEARER)


    def position_match(self, positionId: int, limit:int):
        data, status_code = self.rest_client.get(self.apiConfig.MATCH_CANDIDATE.format(positionId, f'limit={limit}'))
        return data["data"] 


    def position_details(self, positionId: int):
        data, status_code = self.rest_client.get(self.apiConfig.POSITION_DETAILS.format(positionId))
        return data      
       