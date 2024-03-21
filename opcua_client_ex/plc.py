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
	def __init__(self):
		self.IPV4 = None
		self.IO = IO
		self.is_secure = False
		self.port = " "
		self.is_config = False
		self.id = " "
		self.config = None
		self.url = ""
	

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

	def get_node(slef):
		return ""
			
