#challenge 1 -- Convert hex to base 64
import binascii
import base64

def hexToBase64(s):
    raw_bytes = binascii.unhexlify(s)
    return base64.b64encode(raw_bytes)

s = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
assert(hexToBase64(s) == b"SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t")