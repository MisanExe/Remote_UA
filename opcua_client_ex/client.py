
#asunc opcua client example

#import libraries
import asyncio
import logging
import tracemalloc

from asyncua import Client
from plc import UA_Plc


async def connect_plc(ip_add, portID):

	return ""

async def get_node(client, root_node, name_pattern):


	for node in await root_node.get_child("0:Objects"):
		print("Node {}, name {}", node, node.read_display_name())
		if await node.read_variable_type is not None:
			if name_pattern in await node.read_display_name():
				node_id = node.id
				value = await node.read_value()
				print("NodeID {} Value {}".format(node_id, value))

		if len(node.get_childeren()) > 0:
			await get_node(client, root_node, name_pattern)

async def print_child_display_names(client, root):
    # Get the children of the root node
    children = await root.get_children()

    # Print display names of the children
    for child in children:
        display_name = await child.read_display_name()
        print(f"Node ID: {child.nodeid}, Display Name: {display_name}")


async def main():
	# Enable tracemalloc
	tracemalloc.start()
	my_plc = UA_Plc(IPV4="169.254.70.100", port="4840",is_secure=False,id="CODESYS")
	if my_plc.is_connected():
		print("plc( {}: {} ) connected \n".format(my_plc.id, my_plc.IPV4))

	url =  "opc.tcp://192.168.2.136:4840"
	async with Client(url=my_plc.url) as client:
		await client.connect()

		print("Connected .....getting root node\n")
		root = client.get_root_node()
		print("Root Node ID : ", root, "\n") 
		await get_node(client, root, "UAReg1")
		#await print_child_display_names(client, root)
		



if __name__ == "__main__":
	asyncio.run(main())

	

