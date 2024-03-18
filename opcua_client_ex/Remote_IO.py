'''

'''
class IO:
    def __init__ (self) :
        self.OUT = [0,0] #inputs
        self.IN = [0,0] #outputs
        self.Error = " " #error string
        self.Dignostics = " " #diagnostics string
        self.IO_disc = None
        #if not configured
        #default_IO_disc(self)


    def print_disc(self):
        return " "
    def default_IO_disc(self):
        self.IO_disc = {"INPUT_1" : "Unassigned", "INPUT_2" : "Unassigned", "OUTPUT_1" : "Unassigned", "OUTPUT_2" : "Unassigned"}