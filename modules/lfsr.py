import binascii

def textToBit(text):
    bits = bin(int(binascii.hexlify(text.encode('utf-8')), 16))
    return bits[2:].zfill(8*len(text))

def bitToText(bits):
    base10 = int(bits, 2)
    hexStr = '%x' % base10
    length = len(hexStr)
    text = binascii.unhexlify(hexStr.zfill(length + (length & 1)))
    return text
# import sys
# int.from_bytes(b'\x11', byteorder=sys.byteorder)

def integerToByte(i):
    hex_string = '%x' % i
    n = len(hex_string)
    return binascii.unhexlify(hex_string.zfill(n + (n & 1)))

def registerShift(bitKey, addBit):
	lastBit = bitKey[-1]
	bitKey = bitKey[:-1]
	bitKey = str(addBit) + bitKey
	return bitKey,lastBit

def feedBack(bitKey):
	a = bitKey[0]
	b = bitKey[-1]

	return str(int(a) ^ int(b))

def generateKey(plainKey, length):
	bitKey = textToBit(plainKey)
	generatedKey = ''
	for i in range (length):
		addBit = feedBack(bitKey)
		bitKey,tempRes = registerShift(bitKey, addBit)
		generatedKey+=tempRes
	print(generatedKey)
	print(bitToText(generatedKey))

generateKey('halo itb!',99)
# print(textToBit("halo slmt pagi!"))
# print(bitToText('011010000110000101101100011011110010000001110011011011000110110101110100001000000111000001100001011001110110100100100001'))

