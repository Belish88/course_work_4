import json


class File:
    def __init__(self, file_path):
        self.__data_file = file_path
        
    @property
    def data_file(self):
        return self.__data_file
    
    @data_file.setter
    def data_file(self, value):
        self.__data_file = value
        
    def insert(self, data):
        with open(self.__data_file, "r", encoding="utf-8") as file:
            file_data = json.load(file)
        with open(self.__data_file, "w", encoding="utf-8") as file:
            json.dump(file_data + data, file, indent=4, ensure_ascii=False)

    def select(self, query):
        with open(self.__data_file, "r", encoding="utf-8") as file:
            file_data = json.load(file)

        if not query:
            return file_data

        result = []
        for vac in file_data:
            if query in vac:
                result.append(vac)
        return result
