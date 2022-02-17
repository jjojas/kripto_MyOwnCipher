'''
Pseudo-random generation algorithm (PRGA)

Generate keystream then 
xor keystream chars with plaintext chars"
'''

from modules.ksa import getSchedule,swap

def prga(plaintext,key):
    '''
    Execute PRG Algorithm
    INPUT: Plaintext and RC4 Key
    OUTPUT: Cipher in byte form
    '''
    C = bytearray(b'')
    S = getSchedule(key)
    i = 0
    j = 0
    for idx in range (len(plaintext)):
        i = (i+1)%256
        j = (j+S[i])%256
        S[i],S[j] = swap(S[i],S[j])
        t = (S[i]+S[j])%256
        u = S[t]
        C.append((u ^ ord(plaintext[idx]))%256)
    return bytes(C)