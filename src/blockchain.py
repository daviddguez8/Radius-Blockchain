import socket
# Python program to create Blockchain
 
# For timestamp
import datetime
 
# Calculating the hash
# in order to add digital
# fingerprints to the blocks
import hashlib
 
# To store data
# in our blockchain
import json as JSON
 
 
class Blockchain:
   
    # This function is created
    # to create the very first
    # block and set its hash to "0"
    def __init__(self):
        self.chain = []
        self.create_block(proof=1, previous_hash='0')
        self.lake_list = [
            ('0.0.0.0', 8080),
        ]
        self.ip='1.2.3.4'
 
    # This function is created
    # to add further blocks
    # into the chain
    def create_block(self, proof, previous_hash):
        #validate block
        #add to current blockchain
        #broadcast_to_network()
        block = {'index': len(self.chain) + 1,
                 'timestamp': str(datetime.datetime.now()),
                 'proof': proof,
                 'previous_hash': previous_hash,
                 'longitude': 0.0,
                 'latitude': 0.0}
        self.chain.append(block)
        return block
       
    # This function is created
    # to display the previous block
    def print_previous_block(self):
        return self.chain[-1]
       
    # This is the function for proof of work
    # and used to successfully mine the block
    def proof_of_work(self, previous_proof):
        new_proof = 1
        check_proof = False
         
        while check_proof is False:
            hash_operation = hashlib.sha256(
                str(new_proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:5] == '00000':
                check_proof = True
            else:
                new_proof += 1
                 
        return new_proof
 
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
        HOST = '172.20.44.19'
        PORT = 8080  # The port used by the server

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            
            message = str(self.chain)
            s.sendall(bytes(message, 'utf-8'))
            data = s.recv(1024)
            print("recieved", data)

        return
    
    def collect_from_network():

        pass
