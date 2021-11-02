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


num_list = list(range(2,246912))
prime_list = []

for num in num_list:
    if isPrime(num):
        prime_list.append(num)

while True:
    n = int(sys.stdin.readline())
    cnt = 0
    if n == 0:
        break
    for num in prime_list:
        if n < num <= 2*n
            cnt += 1
    print(cnt)

#input
'''
1
10
13
100
1000
10000
100000
0
'''
#output
'''
1
4
3
21
135
1033
8392
'''