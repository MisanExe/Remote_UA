
#asunc opcua client example

#import libraries
import asyncio
import logging
import tracemalloc
import re

from asyncua import Client , Node
from plc import UA_Plc
from ConfigHandler import Config

async def browse_node_recursive(root, name_pattern) -> Node:
    children = await root.get_children()
    
    for child in children:
        node_display_name = await child.read_display_name()
        match = node_display_name.Text
        print(match)
        
        if match == name_pattern:
            return child  
        
        if len(await child.get_children()) > 0:
            # Recursive call to continue searching
            found_child = await browse_node_recursive(child, name_pattern)
            if found_child is not None:
                return found_child  

    return None


def write_val(value, node) -> bool :
    '''
        Writes a value to UA node
    '''
    return False

def read_val(value, node) -> bool :
    '''
        Reads value from a node
    '''
    


def Read_configuration(config_path) -> UA_Plc:
    '''
        Read stored configuration 
    '''
    config = Config(config_path)
    stored_data = config.read_config()
    print(stored_data, type(stored_data))
    if "is_config" in stored_data:
        if stored_data["is_config"] == True :
            config_dict = {}
            config_dict = stored_data
            #get plc values 
            config_plc = UA_Plc()
            config_plc.id = config_dict['PLC_Name']
            config_plc.IPV4 = config_dict["IPV4_ADDRS"]
            config_plc.IO.IN1_Conf = config_dict["IN1_Conf"]
            config_plc.IO.IN2_Conf = config_dict["IN2_Conf"]
            config_plc.IO.OUT1_Conf = config_dict["OUT1_Conf"]
            config_plc.IO.OUT2_Conf = config_dict["OUT2_Conf"]
            config_plc.port = config_dict["port_Conf"]
            config_plc.is_config = config_dict["is_config"]
            config_plc.url = "opc.tcp://"+config_plc.IPV4+":"+config_plc.port
            return config_plc
    
    print("No configuration found")
    return None


async def main():

    my_plc = Read_configuration("Device_Config/PLC_Config.json")

    #check if configuration complete
    if my_plc == None:
        return None
    
    if my_plc.is_connected():
        print("plc( {}: {} ) connected \n".format(my_plc.id, my_plc.IPV4))

    async with Client(url=my_plc.url) as client :
        await client.connect()

        print("Connected .....getting root node\n")
        root = client.get_root_node()
        print("Root Node ID : ", root, "\n") 
        nsidx = root.nodeid.NamespaceIndex

        print("Namespace index of Root Node : {}".format(nsidx))
        Start = await browse_node_recursive(client.get_root_node(), "Start")
        await Start.set_value(True)
        var = await browse_node_recursive(client.get_root_node(), "NAME")
        print(await var.read_value())

		



if __name__ == "__main__":
	asyncio.run(main())

	

