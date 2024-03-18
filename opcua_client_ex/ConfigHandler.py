import json
#import os

class Config :

    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None
        self.u_IO_Config = None
    
    
    def get_data(self, config_data):
        self.data = json.dumps(config_data, indent=None)
        return True

    
    def create_conifg(self, config_data):
        self.get_data(config_data)
        #open file
        try :
            with open(self.file_path, "w") as file :
                json.dump(self.data, file, indent=None)
        except IOError:
            print("error writing to the file")


        return False
    def write_config(self):
        return False 
    
    def read_config(self):
        with open(self.file_path, "r") as file:
            file_data = json.load(file)
            file_data = json.loads(file_data)
        return file_data
