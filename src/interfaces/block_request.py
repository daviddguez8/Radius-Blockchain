#This is the interface that needs to be passed on in order to add a block
class BlockRequest:

    def __init__(self, id, signature, public_data, protected_data, private_data):
        self.id = id
        self.signature = signature
        self.public_data = public_data
        self.protected_data = protected_data
        self.private_data = private_data

