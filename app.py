# To store data
# in our blockchain
import json as JSON
import os
import socket

import requests
# Flask is for creating the web
# app and jsonify is for
# displaying the blockchain
from flask import Flask, jsonify

from src.blockchain import Blockchain

 
# Creating the Web
# App using flask
app = Flask(__name__)
 
# Create the object
# of the class blockchain
profile_chain = Blockchain()
messages_chain = Blockchain()
 
# Adding a profile block
@app.route('/add_profile_block', methods=['GET'])
def add_profile_block():
    #TODO: Implement

    response = ''
    return jsonify(response), 200

# Adding a message block
@app.route('/add_message_block', methods=['GET'])
def add_message_block():
    #TODO: Implement

    response = ''
    return jsonify(response), 200

 
# Sends blockchain in json format
@app.route('/get_profiles_chain', methods=['GET'])
def get_profiles_chain():
    response = {'chain': profile_chain.chain,
                'length': len(profile_chain.chain)}
    return jsonify(response), 200

# Display blockchain in json format
@app.route('/get_messages_chain', methods=['GET'])
def get_messages_chain():
    response = {'chain': messages_chain.chain,
                'length': len(profile_chain.chain)}
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
app.run(host=os.getenv('IP', '0.0.0.0'), 
            port=int(os.getenv('PORT', 8080)))
