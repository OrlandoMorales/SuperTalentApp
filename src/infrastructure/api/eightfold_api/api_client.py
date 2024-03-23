import http.client
import json

from src.common.log.messages_util import MessagesUtilities
from src.common.configuration.app_configuration import AppConfiguration


class ApiClient:
   
    appConfig = AppConfiguration()
    msmUtility = MessagesUtilities()
    
    def get_headers_bearer(self):
        return { 
                'Authorization':  self.appConfig.AUTHORIZATION_BEARER,
                'Content-Type': 'application/json',
                'Connection': 'close'
            }
    
    
    def get_auth_headers_basic(self):
        basic_headers = {
                'Authorization': self.appConfig.AUTHORIZATION_BASIC,
                'Content-Type': 'application/json',
                'Connection': 'close'
        }
        return basic_headers


    def send_request(self,  method:str, baseAddress:str, headers:str, url:str, payload:str):
        try:
            client = http.client.HTTPSConnection(baseAddress)
            client.request(method, url, payload, headers)
            res = client.getresponse()
            data = res.read()
            client.close()
            return json.loads(data.decode("utf-8"))
        except Exception as ex:
            self.msmUtility.print_error_message('SEND_REQUEST',f"{url}",ex)


    def send_get_request(self,  method:str, baseAddress:str, headers:str, url:str, payload:str):
        try:
            print(baseAddress)
            print(url)
            print(headers)
            print(method)

            client = http.client.HTTPSConnection(baseAddress)
            client.request(method=method, url=url, headers=headers)
            res = client.getresponse()
            data = res.read()
            client.close()
            return json.loads(data.decode("utf-8"))
        except Exception as ex:
            self.msmUtility.print_error_message('SEND_REQUEST',f"{url}",ex)    
