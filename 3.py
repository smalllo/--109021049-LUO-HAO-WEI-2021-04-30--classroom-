import sys
import random as rand

def isPrime(x):
    flag = True
    i = 2
    while flag and (i <= x//2):
        if x %i == 0:
            flag = False
        i +=1
    return flag

if __name__ == "__main__":
    
    if len(sys.argv)>1:
        rand.seed(int(sys.argv[1]))
    i=1
    
    while i<=2:
        x = rand.randint(10,1000):
        if isPrime(x):
            (i,"-th prime",x)
            i+=1
