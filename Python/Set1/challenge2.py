import binascii
import base64

def fixedXOR(s1, s2):
    b1 = bytearray.fromhex(s1)
    b2 = bytearray.fromhex(s2)
    b = bytearray([b_1 ^ b_2 for (b_1, b_2) in zip(b1, b2)])
    return b


test_string1 = "1c0111001f010100061a024b53535009181c"
test_string2 = "686974207468652062756c6c277320657965"
expected = b'746865206b696420646f6e277420706c6179'
b = fixedXOR(test_string1, test_string2)
ret = binascii.hexlify(b)
assert(ret == expected)
