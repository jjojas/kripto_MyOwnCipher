from ksa import getSchedule,swap

def encrypt(plaintext,key):
    C = ""
    S = getSchedule(key)
    i = 0
    j = 0
    for idx in range (len(plaintext)):
        i = (i+1)%256
        j = (j+S[i])%256
        S[i],S[j] = swap(S[i],S[j])
        t = (S[i]+S[j])%256
        u = S[t]
        C+=(chr(u ^ ord(plaintext[idx])%256))
    return C

