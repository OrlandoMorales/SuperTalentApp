import json
import os
from src.infrastructure.api.eightfold_api.api_client import ApiClient
from src.common.configuration.app_configuration import AppConfiguration
from src.common.configuration.api_configuration import ApiConfiguration
from src.common.log.messages_util import MessagesUtilities


class AuthenticationApi:
    apiConfig = ApiConfiguration()
    appConfig = AppConfiguration()
    apiClient = ApiClient()
    messageUtil = MessagesUtilities()

    def authentication_body(self):
        return json.dumps({
            "grantType": "password",
            "username": self.appConfig.USERNAME,
            "password": self.appConfig.PASSWORD
        })
    
    def authenticate(self):
        auth_result = self.apiClient.send_request(
            self.apiConfig.POST,
            self.apiConfig.BASE_EIGHTFOLD_API_ADDRESS,
            self.apiClient.get_auth_headers_basic(),
            self.apiConfig.AUTHENTICATE,
            self.authentication_body()
        )
        os.environ["AUTHORIZATION_BEARER"] = f"{auth_result['data']['token_type']} {auth_result['data']['access_token']}"
        return auth_result





        