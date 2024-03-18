
#asunc opcua client example

#import libraries
import asyncio
import logging

from asyncua import Client
from plc import UA_Plc


async def connect_plc(ip_add, portID):

	return ""


async def main():
	my_plc = UA_Plc(IPV4="169.254.70.100", port="4840",is_secure=False,id="CODESYS")
	if my_plc.is_connected():
		print("plc( {}: {} ) connected \n".format(my_plc.id, my_plc.IPV4))

	url =  "opc.tcp://192.168.2.136:4840"
	async with Client(url=my_plc.url) as client:
		await client.connect()

		print("Connected .....getting root node\n")
		root = client.get_root_node()
		print("Root Node ID : ", root, "\n") 
		



if __name__ == "__main__":
	asyncio.run(main())

	

