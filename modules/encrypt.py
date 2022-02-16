from modules.prga import prga
from modules import lfsr
from modules.conversion_tool import byteToText

def encryptText(plaintext,key):
    '''
    Encrypt given text with Modified RC4
    INPUT: plain text and RC4 key
    OUTPUT: encrypted text
    '''
    byteKey = lfsr.generateByteKey(key, 8*len(plaintext))
    cipherText = prga(plaintext, byteKey)
    return byteToText(cipherText)

def decryptText(plaintext,key):
    return ""

def encryptBinaryFile(filedir,key):
    '''
    Encrypt given binary file with Modified RC4
    INPUT: file directory and RC4 key
    OUTPUT: encrypted file at "cipher/files/encrypted.(extension)"
    '''
    ext = filedir.split("/")[-1]
    f = open(filedir,"rb")
    s = f.read()
    nf = prga(s.decode("ISO-8859-1") ,key)
    g = open(f"cipher/files/encrypted_{ext}","wb")
    g.write(bytes(nf,'ISO-8859-1'))
    g.close()

def decryptBinaryFile(filedir,key):
    '''
    Decrypt given binary file with Modified RC4
    INPUT: file directory and RC4 key
    OUTPUT: decrypted file at "cipher/files/decrypted.(extension)"
    '''
    ext = filedir.split("/")[-1]
    f = open(filedir,"rb")
    s = f.read()
    nf = prga(s.decode("ISO-8859-1") ,key)
    g = open(f"cipher/files/decrypted_{ext}","wb")
    g.write(bytes(nf,'ISO-8859-1'))
    g.close()

def saveCipherToTextfile(content,filename):
    '''
    Save ciphertext to text file
    INPUT: string
    OUTPUT: splitted string
    '''
    f = open(f"cipher/text/{filename}.txt","w+")
    f.write(content)
    f.close()