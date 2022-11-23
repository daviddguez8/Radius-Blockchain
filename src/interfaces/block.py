import json
class ProfileBlock:

    def __init__(self, id, timestamp, signature, public_data,protected_data, private_data):
        self.id = id
        self.timestamp = timestamp
        #This will be the way of verifying this block comes from whoever claims to come from
        self.signature = signature
        #Publicly visible data
        self.public_data = public_data
        #Data should be symmetrical encrypted
        self.protected_data = protected_data
        #Data should be assymetrically encripted
        self.private_data = private_data 
    