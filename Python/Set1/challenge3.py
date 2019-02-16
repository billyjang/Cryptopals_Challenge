import math

character_frequencies = [8.12,1.49,2.71,4.32,12.02,2.3,2.03,5.92,
7.31,0.1,0.69,3.98,2.61,6.95,7.68,1.82,0.11,6.02,6.28,9.1,
2.88,1.11,2.09,0.17, 2.11, 0.07]
#character_frequencies_byte = bytearray(character_frequencies)
#implement maybe naive approach first?

def euclidean_distance(b1, b2):
    dist = 0.0
    #print("b1: ", b1)
    #print("b2: ", b2)
    for b_1, b_2 in zip(b1, b2):
        dist += (b_1 - b_2)**2
    return dist

def manhattan_distance(b1, b2):
    dist = 0.0
    for b_1, b_2 in zip(b1, b2):
        dist += math.fabs(b_1-b_2)
    return dist

def create_str(b2):
    return b2.decode("ASCII")

def get_score(s):
    blank_zeros = [0.0]*26
    count = 0.0
    letter_factor = 0.0
    spaces = 0.0
    for i in range(len(s)):
        count += 1.0
        char_s = s[i]
        num = ord(char_s)
        if(num == 32):
            spaces += 20.0
        if (num <= 90 and num >= 65) or (num <= 122 and num >= 97):
            upper = chr(num).upper()
            #print(upper)
            upper_num = ord(upper) - 65
            blank_zeros[upper_num] += 1.0
        else:
            letter_factor += 20.0
    if count != 0:
        for i in range(len(blank_zeros)):
            blank_zeros[i] = (blank_zeros[i] / count) * 100.0
    else:
        blank_zeros = [0.0]*26
    score = euclidean_distance(blank_zeros, character_frequencies) + letter_factor - spaces
    return score



def single_byte_xor(s):
    b1 = bytearray.fromhex(s)
    min_index = 0;
    min_value = 10000;
    for i in range(128):
        b2 = bytearray([byte ^ i for byte in b1])
        s = create_str(b2)
        score = get_score(s)
        #dist = euclidean_distance(freq, character_frequencies)
        #dist = manhattan_distance(freq, character_frequencies)
        if score < min_value:
            min_value = score
            min_index = i
        #print("i: ", i)
        #print("score: ", score)
        #print("str: ", create_str(b2))
    #print("min_index: ", min_index)
    return bytearray([byte ^ min_index for byte in b1])

s = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"      
ret = single_byte_xor(s)
print(create_str(ret))