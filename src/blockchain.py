# For timestamp
import datetime
# Calculating the hash
# in order to add digital
# fingerprints to the blocks
import hashlib
# To store data
# in our blockchain
import json as JSON
import socket
import sys
import time


from .interfaces.block import Block
from .interfaces.block_request import BlockRequest

# Python program to create Blockchain
class Blockchain:
   
    # This function is created
    # to create the very first
    # block and set its hash to "0"
    def __init__(self):
        self.chain = []
        self.create_block(BlockRequest(0,'0', {}, {}, {}))
        self.lake_list = [
            ('127.0.0.1', 65432),
        ]
        self.ip='1.2.3.4'
 
    # This function is created
    # to add further blocks
    # into the chain it:
    #   Validates block correctness
    #   Adds block to current blockchain
    #   Broadcasts the new block to other lakenodes
    def create_block(self, data: BlockRequest):
        block = {
                'id': data.id,
                'timestamp': time.time(),
                'signature': data.signature,
                'public_data': data.public_data,
                'protected_data': data.protected_data,
                'private_data': data.private_data
        }
        
        #add to current blockchain
        self.chain.append(block)

        #broadcast_to_network
        #self.broadcast_to_network(block)
        return block['id']
       
    def hash(self, block):
        encoded_block = JSON.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()
 
    def get_block(self, id):
        for block in self.chain:
            if block['id'] == id:
                return block
        return {'id': 'NOT_FOUND'}

   
    def broadcast_to_network(self):
        for bundle in self.lake_list:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((bundle[0], bundle[1]))
                message = str(self.chain)
                s.sendall(bytes(message, 'utf-8'))
                data = s.recv(1024)
                print("received", data)
            

        return
    
    def collect_from_network():
        #From every lake collect its chain

        #Resolve conflicts accross different chains (merging?)

        #Update self chain by resolving conflicts
        pass
