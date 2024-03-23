import datetime
import json
import os
import time
from src.common.log.messages_util import MessagesUtilities


class FileService:

    PATH = str(os.getcwd()) + '/'
    FILES = f'{PATH}files/'
    PROCESSED_FOLDER = "Processed"
    ERROR_FOLDER = "Error"
    
    msg_util = MessagesUtilities()

    def read_file(self, file:str):
        with open(file,'r') as f:
            try:
                file_content = f.read()
                if len(file_content):
                    data = json.loads(file_content)
                    return data
                else:
                    return {'positions': []}
            except Exception as err:
                self.msg_util.print_error_message("READ FILE","reading",err)
                self.msg_util.print_info_message("READ FILE ERROR","File Moved to Error Folder, Please check..")
                self.move_file_error(file)
               


    def move_file(self, file:str):
         os.replace(file, f'{self.FILES}{self.PROCESSED_FOLDER}/{self.get_file_name(file)}')
        
         
    def move_file_error(self, file:str):
         os.replace(file, f'{self.FILES}{self.ERROR_FOLDER}/{self.get_file_name(file)}')


    def get_file_name(self, file):
        file_name_split = str(file.split("/")[6]).split(".")
        file_name = str(file_name_split[0])
        file_type = str(file_name_split[1])

        if len(file_name_split) > 0:
            return f'{file_name}-Processsed-{datetime.datetime.now()}.{file_type}'
        else:
            raise Exception("The File name has some errors, Please check")
    
