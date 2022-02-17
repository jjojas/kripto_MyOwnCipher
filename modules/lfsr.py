'''
Linear Feedback Shift Register (LFSR)

Generate keystream 
'''

from modules.conversion_tool import textToBit, bitToByte, byteToText


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
	return bitToByte(generatedKey)