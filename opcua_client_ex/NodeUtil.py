

import asyncio
from asyncua import Client , Node

class NodeUtil :

    def __init__(self, NodeNames):
        self.NodeNames = NodeNames
        self.NodeStatus = len(NodeNames)
        self.Nodes = []

        #init to false
        for x in range(0,len(self.NodeNames)):
            self.NodeStatus[x] = False

    async def browse_node_recursive(self, root):
        children = await root.get_children()

        for child in children :
            node_display_name = await child.read_display_name()
            match = node_display_name.Text

            if self._in_list(match):

        
        return None



    def update_status(self):
        return False

    def _in_list(self, x : str):
        if x in self.NodeNames :
            self.status -=1
            return True
        else :
            return False
    

    
async def browse_node_recursive(root, NodeLs : NodeUtil):
    children = await root.get_children()
    
    for child in children:
        node_display_name = await child.read_display_name()
        match = node_display_name.Text
        #print(match)
        
        if match 
            return child  
        
        if len(await child.get_children()) > 0:
            # Recursive call to continue searching
            found_child = await browse_node_recursive(child, name_pattern)
            if found_child is not None:
                return found_child  

    return None