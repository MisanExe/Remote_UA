
#asunc opcua client example

#import libraries
import asyncio
import logging
import tracemalloc
import re

from asyncua import Client , Node
from plc import UA_Plc

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
		
		
async def main():

	my_plc = UA_Plc(IPV4="169.254.70.100", port="4840",is_secure=False,id="CODESYS")
	if my_plc.is_connected():
		print("plc( {}: {} ) connected \n".format(my_plc.id, my_plc.IPV4))

	async with Client(url=my_plc.url) as client:
		await client.connect()

		print("Connected .....getting root node\n")
		root = client.get_root_node()
		print("Root Node ID : ", root, "\n") 
		nsidx = root.nodeid.NamespaceIndex

		print("Namespace index of Root Node : {}".format(nsidx))

		var = await browse_node_recursive(client.get_root_node(), "UA_REG2")
		print(var)
		
		



if __name__ == "__main__":
	asyncio.run(main())

	

