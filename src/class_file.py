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
            new_file_data = file_data.copy()
            for vac_data in data:
                for vac_file_data in new_file_data:
                    if vac_data["id"] == vac_file_data["id"]:
                        file_data.remove(vac_file_data)
            json.dump(file_data + data, file, indent=4, ensure_ascii=False)

    def select(self, query):
        with open(self.__data_file, "r", encoding="utf-8") as file:
            file_data = json.load(file)

        if not query:
            return file_data

        result = []
        for vac in file_data:
            if query == vac["salary"]:
                result.append(vac)
        return result
