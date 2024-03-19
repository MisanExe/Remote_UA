'''
-------------------------------------------------------------------------------
File: plc.py
Author: Misan
Date: March 17, 2024
Description:
	 Defines a plc object and it's attributes
 	 PLC object is used to establish connection via UA.
 	 PLC object configuration is stored in <Device_Config/PLC_Config.json>
   
Additional notes or disclaimers can go here.

Dependencies:
  - Ping3 
  - ConfigHandler - <ConfigHandler.py>
  - RemoteIO - <RemoteIO.py>

Usage:
  - How to run the script or use the functions/classes in this file.

History:
  - YYYY-MM-DD: Version 1.0 - Initial release

License: This code is released under the MIT License.
-------------------------------------------------------------------------------
'''
import ping3
from ConfigHandler import Config
from Remote_IO import IO

class UA_Plc :
	def __init__(self,id,IPV4,port,is_secure):
		self.IPV4 = IPV4
		self.IO = IO()
		self.is_secure = is_secure
		self.port = port
		self.is_config = False
		self.id = id
		self.config = Config("Device_Config/PLC_Config.json")
		self.url = "opc.tcp://"+IPV4+":"+port


		stored_data = self.config.read_config()
		#print(stored_data)
		if "is_config" in stored_data:
			value = stored_data.get("is_config")
			if value is True:
				self.is_config = True
		else :
			print("not configured")


		#create configuration
		if not self.is_config:
			self.is_config = True
			#generate data 
			config_dict = {}
			config_dict["PLC_Name"] = self.id
			config_dict["IPV4_ADDRS"] = self.IPV4
			config_dict["IN1"] = self.IO.IN1
			config_dict["IN2"] = self.IO.IN2
			config_dict["OUT1"] = self.IO.OUT1
			config_dict["OUT2"] = self.IO.OUT2
			config_dict["port"] = self.port
			config_dict["is_config"] = self.is_config
			print(config_dict)
			#JSONify data 
			self.config.create_config(config_dict)
			




	def is_configured(self):
		return False
	

	def is_connected(self):
		timeout = 0.1
		ping3.EXCEPTIONS = True

		#send icmp echo request to the ip address
		try :
			response = ping3.ping(self.IPV4, timeout=timeout)
		except ping3.errors.HostUnknown:
			print("Cannot resolve: Unknown host. (Host = {})".format(self.IPV4))
			return False
		except ping3.errors.PingError:
			print("cannot ping device on network")
			return False
		
		#return true if connected
		if(response is not None):
			return True
			
