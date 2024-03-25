import json
import os
from typing import List
from pydantic import parse_obj_as
from src.infrastructure.api.eightfold_api.api_client import ApiClient
from src.common.configuration.app_configuration import AppConfiguration
from src.common.configuration.api_configuration import ApiConfiguration
from src.common.log.messages_util import MessagesUtilities
from src.infrastructure.api.eightfold_api.rest_client import RestClient


class ProfilesApi:

    api_config = ApiConfiguration()
    app_config = AppConfiguration()
    message_util = MessagesUtilities()

    rest_client = RestClient(api_config.BASE_EIGHTFOLD_API_ADDRESS, app_config.TOKEN_BEARER)


    def profile_info(self, profile_id: str):
        data, status_code = self.rest_client.get(self.api_config.PROFILE_DETAILS.format(profile_id))
        return data