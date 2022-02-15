from prga import prga

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
