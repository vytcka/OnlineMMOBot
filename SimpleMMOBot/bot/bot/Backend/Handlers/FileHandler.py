from Handlers.TextHandler import TextHandler
import os

class FileHandler:
    @staticmethod
    def read_from_file_lines(file_path):
        with open(file_path, 'r') as file:
            lines = file.readlines()
            return lines
        
    @staticmethod
    def get_array_from_file(file_path, delimiter):
        with open(file_path, 'r') as file:
            lines = file.readlines()
            array = TextHandler.split_lines_to_array(lines, delimiter)
            return array

    @staticmethod
    def write_into_file(file_path, data, append=False, append_type='new_line'):
        mode = 'a' if append else 'w'
        with open(file_path, mode) as file:
            if not append:
                file.truncate(0)
            if append and append_type == 'new_line' and os.path.getsize(file_path) > 0:
                file.write('\n')
            file.write(data)