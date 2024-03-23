import os
from slack_sdk import WebClient
from src.common.configuration.app_configuration import AppConfiguration

class SlackClient:
        
    app_config = AppConfiguration()

    def post_message(self, message:str):
        slackCli = WebClient(token=self.app_config.SLACK_TOKEN)
        response = slackCli.chat_postMessage(
            channel=self.app_config.SLACK_BOT,
            text=message
        )

        if response["ok"]:
            print("Message Sent!")
        else:
            print("Error::", response["error"])



    def post_message_block(self, message:str, blocks):
        slackCli = WebClient(token=self.app_config.SLACK_TOKEN)
        response = slackCli.chat_postMessage(
            channel=self.app_config.SLACK_BOT,
            text=message,
            blocks = blocks
        )

        if response["ok"]:
            print("Message Sent!")
        else:
            print("Error::", response["error"])
