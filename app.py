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
from flask import Flask, jsonify, request, make_response
from flask_cors import CORS, cross_origin

from src.blockchain import Blockchain
from src.interfaces.block_request import BlockRequest


# Create the object
# of the class blockchain
chains = {
    'profiles': Blockchain(),
    'messages': Blockchain(),
    'interactions': Blockchain()
}


# Creating the Web
# App using flask
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


def _build_cors_preflight_response():
    response = make_response()
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', '*')
    response.headers.add('Access-Control-Allow-Methods', '*')
    return response

def _corsify_actual_response(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

#TODO: When connecting to frontend, finish adding all parameters 
# Adding a block to a chain
@app.route('/add_block/<chain_name>', methods=['GET','POST'])
def add_profile_block(chain_name):
    body = 0
    if(request.method == 'OPTIONS'):
        return _build_cors_preflight_response()

    if(chain_name == "messages"):
        try:
            body = request.get_json()
            id = body['id']
            sender = body['sender']
            recipient = body['recipient']
            timestamp = body['timestamp']
            private = body['private']
            
            response = chains[chain_name].create_block(BlockRequest(id,sender, recipient, timestamp, private))
            return jsonify(response), 200
        except:
            print('Request missing parameter', body)
            return jsonify({}), 400
    elif(chain_name == "profiles"):
        try:
            body = request.get_json()

            id = body['id']
            signature = body['signature']
            public = body['public']
            protected = body['protected']
            private = body['private']
            
            response = chains[chain_name].create_block(BlockRequest(id,signature, public, protected, private))
            return jsonify(response), 200
        except:
            print('Request missing parameter', body)
            return jsonify({}), 400
    else:
        print("Error in chain name decleration")
        return jsonify({}), 400

    
 
# Sends blockchain in json format
@app.route('/get_chain/<chain_name>', methods=['GET'])
def get_profiles_chain(chain_name):

    response = {'chain': chains[chain_name].chain,
                'length': len(chains[chain_name].chain)}
    return jsonify(response), 200

@app.route('/get_block/<chain_name>/<target_id>', methods = ['GET'])
def get_block(chain_name, target_id):
    print('get block hit')
    if request.method == 'OPTIONS':
        print('options???')
        return _build_cors_preflight_response()
    
    found_block = chains[chain_name].get_block(target_id)
    response = _corsify_actual_response(make_response(found_block))
    print('get_block returning')
    print(found_block)
    return response
 

#  Delete this method. 
#  Broadcast should be a private responsibility of each chain, 
#  part of the adding a block contract

@app.route('/broadcast_chain/<chain_name>', methods=['GET'])
def broadcast_chain(chain_name):
    response = chains[chain_name].broadcast_to_network()
    
    return jsonify(response),200


# Run the flask server locally
app.run(
    host=os.getenv('IP', '0.0.0.0'),
    port=int(os.getenv('PORT', 8080)),
    debug=True
)
