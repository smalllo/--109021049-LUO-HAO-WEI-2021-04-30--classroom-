import sys
d = {
    "q":"w","w":"e","e":"r","r":"t"
}

if __name__ == "__main__":
    if len (sys.argv) >1:
        data = list (sys.argv[1])
        for i in range(len(data)):
            data[i] = d[data[i]]
        print(''.join(data))