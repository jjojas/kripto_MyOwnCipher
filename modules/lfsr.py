'''
Linear Feedback Shift Register (LFSR)

Generate keystream 
'''

from modules.conversion_tool import textToBit, bitToByte, byteToText
# from conversion_tool import textToBit, bitToByte, byteToText


def registerShift(bitKey, addBit):
	'''
    Right-shift bitKey and add new bit at bitKey[0]
    INPUT: bitKey and addBit
    OUTPUT: bitKey and lastBit
    '''
	lastBit = bitKey[-1]
	bitKey = bitKey[:-1]
	bitKey = str(addBit) + bitKey
	return bitKey,lastBit

def feedBack(bitKey):
	'''
    Xor two selected bit of bitKey
    INPUT: bitKey
    OUTPUT: xor result (string)
    '''
	a = bitKey[0]
	b = bitKey[-1]

	return str(int(a) ^ int(b))

def generateByteKey(plainKey, bitLength):
	'''
    Generate a bitLength key (byte)
    INPUT: Plaintext and bitLength
    OUTPUT: key (byte)
    '''
	bitKey = textToBit(plainKey)
	generatedKey = ''
	for i in range (bitLength):
		addBit = feedBack(bitKey)
		bitKey,tempRes = registerShift(bitKey, addBit)
		generatedKey+=tempRes
	# print(generatedKey)
	# print(len(generatedKey))
	# print(bitToByte(generatedKey))
	# ASCII_values = list(bitToByte(generatedKey))
	# print(ASCII_values)
	# print("".join([chr(value) for value in ASCII_values]))
	return bitToByte(generatedKey)

# generateByteKey("Let's grab a 🍕!",160)
# # print(textToBit("halo slmt pagi!"))
# print(byteToText(bitToByte('10011000110010101110100001001110111001100100000011001110111001001100001011000100010000001100001001000001111000010011111100011011001010100100001')))
# k = b"Let's grab a \xf0\x9f\x8d\x95!"
# print(k.decode('unicode-escape').encode('latin1').decode('utf8'))