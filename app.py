# To store data
# in our blockchain
import json as JSON
import os
import socket
import uuid

import requests
# Flask is for creating the web
# app and jsonify is for
# displaying the blockchain
from flask import Flask, jsonify, request

from src.blockchain import Blockchain
from src.interfaces.block_request import BlockRequest

# Creating the Web
# App using flask
app = Flask(__name__)
 
# Create the object
# of the class blockchain
chains = {
    'profile': Blockchain(),
    'message': Blockchain()
}
profile_chain = Blockchain()
messages_chain = Blockchain()


#TODO: When connecting to frontend, finish adding all parameters 
# Adding a block to a chain
@app.route('/add_block/<chain_name>/<signature>', methods=['GET','POST'])
def add_profile_block(chain_name, signature):
    signature = signature
    public = {}
    protected = {}
    private = {}
    
    response = chains[chain_name].create_block(BlockRequest(uuid.uuid1(),signature, public, protected, private))

    return jsonify(response), 200
 
# Sends blockchain in json format
@app.route('/get_chain/<chain_name>', methods=['GET'])
def get_profiles_chain(chain_name):
    response = {'chain': chains[chain_name].chain,
                'length': len(chains[chain_name].chain)}
    return jsonify(response), 200

 
# Check validity of blockchain
@app.route('/valid', methods=['GET'])
def valid():
    valid = profile_chain.chain_valid(app.chain)
     
    if valid:
        response = {'message': 'The Blockchain is valid.'}
    else:
        response = {'message': 'The Blockchain is not valid.'}
    return jsonify(response), 200
 
 
'''
 Delete this method. 
 Broadcast should be a private responsibility of each chain, 
 part of the adding a block contract

@app.route('/broadcast_chain', methods=['GET'])
def broadcast_chain():
    response = profile_chain.broadcast_to_network()
    
    return jsonify(response),200
'''

# Run the flask server locally
app.run(
    host=os.getenv('IP', '0.0.0.0'),
    port=int(os.getenv('PORT', 8080)),
    debug=True
)
