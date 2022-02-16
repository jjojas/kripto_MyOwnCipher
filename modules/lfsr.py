import binascii

def textToBit(text):
    bits = bin(int(binascii.hexlify(text.encode('utf-8')), 16))
    return bits[2:].zfill(8*len(text))

def bitToByte(bits):
    base10 = int(bits, 2)
    hexStr = '%x' % base10
    length = len(hexStr)
    byte = binascii.unhexlify(hexStr.zfill(length + (length & 1)))
    return byte

def byteToText(byte):
	ASCII_values = list(byte)
	return "".join([chr(value) for value in ASCII_values])


def registerShift(bitKey, addBit):
	lastBit = bitKey[-1]
	bitKey = bitKey[:-1]
	bitKey = str(addBit) + bitKey
	return bitKey,lastBit

def feedBack(bitKey):
	a = bitKey[0]
	b = bitKey[-1]

	return str(int(a) ^ int(b))

def generateByteKey(plainKey, bitLength):
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

generateByteKey("Let's grab a 🍕!",160)
# print(textToBit("halo slmt pagi!"))
print(byteToUTF8Text(bitToByte('10011000110010101110100001001110111001100100000011001110111001001100001011000100010000001100001001000001111000010011111100011011001010100100001')))