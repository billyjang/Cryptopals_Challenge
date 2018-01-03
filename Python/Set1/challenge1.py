#challenge 1 -- Convert hex to base 64
import binascii
import base64

def hexToBase64(s):
    return base64.base64encode(binascii.unhexlify(s));