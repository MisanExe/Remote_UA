'''

'''
class IO:
    def __init__ (self) :
      self.OUT1 = [0,{"Enable":"false"},{"TagName":"None"}] #output1
      self.OUT2 = [0,{"Enable":"false"},{"TagName":"None"}] #output2
      self.IN1 = [0,{"Enable":"false"}, {"TagName":"None"}] #input1
      self.IN2 = [0,{"Enable":"false"}, {"TagName":"None"}] #input2
      self.Error = " " #error string
      self.Dignostics = " " #diagnostics string
      self.IO_disc = None
        #if not configured
        #default_IO_disc(self)


    def print_disc(self):
        return " "
    def default_IO_disc(self):
        self.IO_disc = {"INPUT_1" : "Unassigned", "INPUT_2" : "Unassigned", "OUTPUT_1" : "Unassigned", "OUTPUT_2" : "Unassigned"}
