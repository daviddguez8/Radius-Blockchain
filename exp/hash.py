import hashlib
import json

block = {
    'hello': 'this is my block',
    'another': 2
}
print(block)

encoded_block = json.dumps(block, sort_keys=True).encode()
print(encoded_block)

print(hashlib.sha256(b'2').hexdigest())
 