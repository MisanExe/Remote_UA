
#asunc opcua client example

#import libraries
import asyncio
import logging
import tracemalloc

from asyncua import Client , Node
from plc import UA_Plc
from ConfigHandler import Config
import json
import ast




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
            config_plc.config = config_dict
            return config_plc
    
    print("No configuration found")
    return None


async def write_value(node, value):
    try :
        await node.set_value(value)
    except Exception as e:
        print("unable to write value : ", e)
    finally :
        print("exit")


 


async def main():

    '''
        UA_STATE = "DEVICE_ON_NETWORK"
        UA_STATE = "DEVICE_NOT_ON_NETWORK"
        UA_STATE = "CONNECTED : SERVER"
        UA_STATE = "NOT_CONNECTED : SERVER"
    '''
    UA_STATE = " "

    my_plc = Read_configuration("Device_Config/PLC_Config.json")

    #check if configuration complete
    if my_plc == None:
        return None
    try :
        if my_plc.is_connected():
            print("plc( {}: {} ) connected \n".format(my_plc.id, my_plc.IPV4))
            UA_STATE = "DEVICE_ON_NETWORK"
    except Exception as e :
        UA_STATE = "DEVICE_NOT_ON_NETWORK"
        print("Unable to connect")
    


    async with Client(url=my_plc.url) as client :
        try :
            await client.connect()
        except ConnectionRefusedError :
            UA_STATE = "NOT_CONNECTED : SERVER"
            print("unable to connect")
        
        print("Connected .....getting root node\n")
        my_plc.root = client.get_root_node()
        await my_plc.get_nodes()
        my_plc.printNodes()
   

        '''print("Namespace index of Root Node : {}".format(nsidx))
        Start = await browse_node_recursive(client.get_root_node(), "Start")
        await Start.set_value(True)
        var = await browse_node_recursive(client.get_root_node(), "NAME")
        print(await var.read_value())'''
 
      
        #var = str(await browse_node_recursive(client.get_root_node(), "NAME"))
        #print(type(var))

        #await my_plc.Node_OUT1.set_value(True)
        await write_value(my_plc.Node_Diagnostics, "Hello from adele")
        await write_value(my_plc.Node_Connected, True)

        


		



if __name__ == "__main__":
	asyncio.run(main())

	

