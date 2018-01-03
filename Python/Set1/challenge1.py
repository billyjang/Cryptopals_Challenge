#challenge 1 -- Convert hex to base 64
import binascii
import base64

def hexToBase64(s):
    raw_bytes = binascii.unhexlify(s)
    return base64.b64encode(raw_bytes)