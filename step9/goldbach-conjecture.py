import sys
import math

def isPrime(num):
    a = int(math.sqrt(num))
    if num == 1:
        return False
    else:
        for i in range(2, a+1):
            if num % i == 0:
                return False
        return True


rep = int(input())
prime_list = []

for i in range(rep):
    n = int(sys.stdin.readline())
    for i in range(2, n):
        if isPrime(i):
            prime_list.append(i)

    for idx in range(len(prime_list)):
        if n % prime_list[idx] == 0:
            print(idx,idx,sep=" ")
        else:
            num = n % prime_list[idx]
            print(idx,num,sep=" ")

    prime_list.clear()





