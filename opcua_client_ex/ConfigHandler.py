import json
#import os

class Config :

    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None
        self.u_IO_Config = None
    
    
    def get_data(self, data):
        json_string = json.dumps(data,indent=4)
        return json_string

    
    def create_config(self, config_data):
        json_string = self.get_data(config_data)
        #open file
        try :
            with open(self.file_path, "w") as file :
                file.write(json_string)
        except IOError:
            print("error writing to the file")


        return False
    def write_config(self):
        return False 
    
    def read_config(self):
        with open(self.file_path, "r") as file:
            file_data = json.load(file)
        return file_data
