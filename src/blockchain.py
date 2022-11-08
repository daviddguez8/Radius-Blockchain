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
            ('0.0.0.0', 8080),
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
 
    def chain_valid(self, chain):
        previous_block = chain[0]
        block_index = 1
         
        while block_index < len(chain):
            block = chain[block_index]
            if block['previous_hash'] != self.hash(previous_block):
                return False
               
            previous_proof = previous_block['proof']
            proof = block['proof']
            hash_operation = hashlib.sha256(
                str(proof**2 - previous_proof**2).encode()).hexdigest()
             
            if hash_operation[:5] != '00000':
                return False
            previous_block = block
            block_index += 1
         
        return True
    
    def broadcast_to_network(self):
        HOST = '127.0.0.1'
        PORT = 65432  # The port used by the server

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
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
