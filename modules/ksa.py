
def init(arr):
    for i in range(256):
        arr.append(i)

def swap(a,b):
    return(b,a)

def permute(arr,key):
    j = 0
    for i in range(256):
        j = (j + arr[i] + ord(key[i%len(key)]))%256
        arr[i],arr[j] = swap(arr[i],arr[j])

def getSchedule(key):
    s = []
    init(s)
    permute(s,key)
    return s

if __name__ == "__main__":
    print(getSchedule("!"))
    