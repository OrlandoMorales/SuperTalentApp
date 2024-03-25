import json
from src.infrastructure.file_system.file_service import FileService


class DemoApi:

    fileSer = FileService()


    def candidates_info(self, candidate_id: str):
        data = self.fileSer.read_file("DATA",f'candidate-{candidate_id}')
        return data


    def position_info(self, position_id: int):
        data = self.fileSer.read_file("DATA",f'position-{position_id}')
        return data

    def match_position(self, position_id: int):
        data = self.fileSer.read_file("DATA",f'match-position-{position_id}')
        return data