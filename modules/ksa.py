'''
Key-Scheduling Algorithm (KSA) 

Generate key schedule based on user key"
'''

def init(arr):
    '''
    Generate array
    '''
    for i in range(256):
        arr.append(i)

def swap(a,b):
    '''
    Swap value between two var
    '''
    return(b,a)

def permute(arr,key):
    '''
    Execute permutation in key
    INPUT: array of int[256] to permute and RC4 Key
    OUTPUT: given array are permuted
    '''
    j = 0
    for i in range(256):
        j = (j + arr[i] + ord(key[i%len(key)]))%256
        arr[i],arr[j] = swap(arr[i],arr[j])

def getSchedule(key):
    '''
    Generate Key Schedule
    INPUT: RC4 Key
    OUTPUT: Key Schedule
    '''
    s = []
    init(s)
    permute(s,key)
    return s

if __name__ == "__main__":
    print(getSchedule("!"))
    