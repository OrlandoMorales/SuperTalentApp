from termcolor import colored, cprint
import datetime


class MessagesUtilities:
    
    def print_error_message(self, errorTitle:str, method:str, errorMessage:str):
        print(colored(f'ERROR::{errorTitle}::METHOD::{method}::MESSAGE::{errorMessage}::TIMESTAMP::{datetime.datetime.now()}','red', attrs=["bold"]))

    def print_log_message(self, logTitle:str, method:str, logMessage:str):
        print(colored(f'LOG::{logTitle}::METHOD::{method}::MESSAGE::{logMessage}::TIMESTAMP::{datetime.datetime.now()}','yellow', attrs=["bold"]))

    def print_info_message(self, infoTitle:str, method:str, infoMessage:str):
        print(colored(f'INFO::{infoTitle}::METHOD::{method}::MESSAGE::{infoMessage}::TIMESTAMP::{datetime.datetime.now()}','green', attrs=["bold"]))

    def print_info_message(self, infoTitle:str, infoMessage:str):
        print(colored(f'INFO::{infoTitle}::MESSAGE::{infoMessage}::TIMESTAMP::{datetime.datetime.now()}','green', attrs=["bold"]))
    
    def print_log_message(self, infoTitle:str, infoMessage:str):
        print(colored(f'INFO::{infoTitle}::MESSAGE::{infoMessage}::TIMESTAMP::{datetime.datetime.now()}','yellow', attrs=["bold"]))

