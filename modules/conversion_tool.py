import sys
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
	# return byte.decode(encoding="utf-8",errors="myreplace")
    text = ''
    for i, intByte in enumerate(byte):
        try:
            if intByte<=31 or (intByte>=127 and intByte<=160):
                raise UnicodeDecodeError('ISO-8859–1', byte, i, i+1, 'Unprintable Character')
            else:
                char = intByte.to_bytes(1, sys.byteorder).decode(encoding="utf-8")
                if intByte==92: char='\\' + char
                text+=char
        except UnicodeDecodeError:
            text+='\\x{:02x}'.format(intByte)

    return text