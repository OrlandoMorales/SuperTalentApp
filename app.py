import os
from stat import ST_CTIME
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from src.infrastructure.file_system.file_service import FileService
from src.application.process_positions import ProcessPositions
from src.common.log.messages_util import MessagesUtilities


PATH = str(os.getcwd()) + '/' 
FILES_DIRECTORY = f'{PATH}files/'

file_service = FileService()
msg_util = MessagesUtilities()

msg_util.print_info_message("Application Start","Processing Positions Files")

observer = Observer()
observer.schedule(ProcessPositions(), FILES_DIRECTORY, recursive=False)
observer.start()
try:
    while observer.is_alive():
        observer.join(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()