from watchdog.events import FileSystemEventHandler
from threading import Timer
from time import sleep
from src.common.log.messages_util import MessagesUtilities
from src.infrastructure.slack.slack_client import SlackClient
from src.infrastructure.file_system.file_service import FileService
from src.infrastructure.api.eightfold_api.demo_api import DemoApi
from src.infrastructure.api.eightfold_api.positions_api import PositionApi
from src.infrastructure.api.eightfold_api.profiles_api import ProfilesApi
from src.common.utilities.slack_message_format import SlackMessageFormater
from src.infrastructure.api.eightfold_api.authentication_api import AuthenticationApi
from src.common.configuration.app_configuration import AppConfiguration

class ProcessPositions(FileSystemEventHandler):

    app_config = AppConfiguration()
    file_service = FileService()
    msg_util = MessagesUtilities()
    auth_api = AuthenticationApi()
    position_api = PositionApi()
    profile_api = ProfilesApi()
    slack_client = SlackClient()
    demo_api = DemoApi()
    message_formater = SlackMessageFormater()
    positions = {}

    def on_created(self, event):
        try:
            self.msg_util.print_log_message("FILE CREATED",event.src_path)
            self.positions = self.file_service.read_file(event.src_path)
            if(len(self.positions['positions']) > 0):
                for position_id in self.positions["positions"]:
                    self.msg_util.print_log_message("POSITION-ID",f"{position_id}")
                    match_candidates = self.position_api.position_match(position_id,2)
            
                    for match in match_candidates:
                        profile = self.profile_api.profile_info(match["profileId"])
                        position = self.position_api.position_details(position_id)
                        
                        message_template = self.message_formater.message_template_one(profile, position, match)

                        self.slack_client.post_message_block("Hiring Process -- Positions", 
                                                message_template["blocks"])
                        
                        sleep(int(self.app_config.MESSAGES_SEND_INTERVAL))
            else:
                self.file_service.move_file_error(event.src_path)
        except Exception as err:
            self.msg_util.print_error_message("PROCESS POSITIONS","on_created",err)
            self.msg_util.print_info_message("PROCESS POSITIONS","File Moved to Error Folder, Please check..")
            self.file_service.move_file_error(event.src_path)
        finally:
            if len(self.positions['positions']) > 0:
                self.file_service.move_file(event.src_path) 



