'''
Conversion Tool 

Collection function to convert bit, byte, and text 
'''

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
    text = ''
    for intByte in byte:
        text+=chr(intByte)

    return text