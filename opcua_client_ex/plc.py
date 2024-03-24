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
from asyncua import Client , Node
import asyncio



async def browse_node_recursive(root, name_pattern) -> Node:
    children = await root.get_children()
    
    for child in children:
        node_display_name = await child.read_display_name()
        match = node_display_name.Text
        #print(match)
        
        if match == name_pattern:
            return child  
        
        if len(await child.get_children()) > 0:
            # Recursive call to continue searching
            found_child = await browse_node_recursive(child, name_pattern)
            if found_child is not None:
                return found_child  

    return None


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
		self.root = None

		self.Node_OUT1 = None
		self.Node_OUT2 = None
		self.Node_IN1 = None
		self.Node_IN2 = None

		#system defined
		self.Node_Diagnostics = None
		self.Node_Connected = None
		self.Node_Fault = None

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
	
	async def get_nodes(self):
		OUT1 = self.config["OUT1_Conf"]
		OUT2 = self.config["OUT1_Conf"]
		IN1 = self.config["IN1_Conf"]
		IN2 = self.config["IN2_Conf"]
		#write code to handle none in Tag Name
		

		#print(type(OUT1[1]["TagName"]), OUT1[1]["TagName"])

		

		#user defined
		#self.Node_OUT1 = await browse_node_recursive(self.root, OUT1[1]["TagName"])
		task1 = asyncio.create_task(browse_node_recursive(self.root, OUT1[1]["TagName"]))
		task2 = asyncio.create_task(browse_node_recursive(self.root, OUT2[1]["TagName"]))
		task3 = asyncio.create_task(browse_node_recursive(self.root, IN1[1]["TagName"]))
		task4 = asyncio.create_task(browse_node_recursive(self.root, IN2[1]["TagName"]))
		task5 = asyncio.create_task(browse_node_recursive(self.root, "UA_Diagnostics"))
		task6 = asyncio.create_task(browse_node_recursive(self.root, "UA_Connected"))
		task7 = asyncio.create_task(browse_node_recursive(self.root, "UA_FAULT"))

		#user defined
		self.Node_OUT1 = await task1
		self.Node_OUT2 = await task2
		self.Node_IN1 =  await task3
		self.Node_IN2 = await task4
		

		#system defined
		self.Node_Diagnostics = await task5
		self.Node_Connected =  await task6
		self.Node_Fault = await task7
		
		

	
	
	def printNodes(self):
		print("OUT1 : ",self.Node_OUT1, "\n")
		print("OUT2 : ",self.Node_OUT2, "\n")
		print("IN1 : ",self.Node_IN1, "\n")
		print("IN2 : ",self.Node_IN1, "\n")

		print("Diagnostics : ",self.Node_Diagnostics, "\n")
		print("Fault : ",self.Node_Fault, "\n")
		print("Connected : ",self.Node_Connected, "\n")
		
			
