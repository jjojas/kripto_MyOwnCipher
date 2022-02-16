from modules.prga import prga
from modules import lfsr
from modules.conversion_tool import byteToText

# from prga import prga
# import lfsr
# from conversion_tool import byteToText

def encryptDecryptText(text,key):
    '''
    Encrypt or decrypt given text with Modified RC4
    INPUT: text and RC4 key
    OUTPUT: encrypted/decrypted text
    '''
    byteKey = lfsr.generateByteKey(key, 8*len(text)*len(key))
    cipherText = prga(text, byteKey)
    return byteToText(cipherText)

def encryptBinaryFile(filedir,key):
    '''
    Encrypt given binary file with Modified RC4
    INPUT: file directory and RC4 key
    OUTPUT: encrypted file at "cipher/files/encrypted.(extension)"
    '''
    ext = filedir.split("/")[-1]
    f = open(filedir,"rb")
    s = f.read()
    decodeBinary = s.decode("ISO-8859-1")
    byteKey = lfsr.generateByteKey(key, 8*len(decodeBinary))
    # cipherText = byteToText(prga(decodeBinary, byteKey))
    g = open(f"cipher/files/encrypted_{ext}","wb")
    g.write(prga(decodeBinary, byteKey))
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
    decodeBinary = s.decode("ISO-8859-1")
    byteKey = lfsr.generateByteKey(key, 8*len(decodeBinary))
    # cipherText = byteToText(prga(decodeBinary, byteKey))
    g = open(f"cipher/files/decrypted_{ext}","wb")
    g.write(prga(decodeBinary, byteKey))
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

if __name__ == "__main__":
    print(encryptBinaryFile("C:/Users/Asus/Downloads/1645007389929.jpg","A"))