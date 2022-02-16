'''
Pseudo-random generation algorithm (PRGA)

Generate keystream then 
xor keystream chars with plaintext chars"
'''

from modules.ksa import getSchedule,swap
from modules import conversion_tool

def prga(plaintext,key):
    '''
    Execute PRG Algorithm
    INPUT: Plaintext and RC4 Key
    OUTPUT: Ciphertext
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

# print(conversion_tool.byteToText(prga("halo aku di bandung Lho !! ","hahahihi")))
# print(conversion_tool.byteToText(prga("UX\x92È+\x86è~±\x04d¬yåOuV¹\x13al\x8d\x8cBL\x8c$","hahahihi")))
# print(conversion_tool.byteToText(prga('Let"s grab a pizza!',"hahahihi")))
# print(conversion_tool.byteToText(prga("q\\\x8a\x85xÇäyð\x02-í;Ñ\x00","hahahihi")))
# print(conversion_tool.byteToText(prga("\x99\x1c\xb9\xedr","hahahihi")))
# # print(prga("UXÈ","hahahihi"))
# # "UX\x92\xc8+\x86\xe8~\xb1\x04d\xacy\xe5OuV\xb9\x13al\x8d\x8cBL\x8c$"

# print(prga("UX\x92\xc8","hahahihi").decode(encoding="ascii",errors="backslashreplace"))
