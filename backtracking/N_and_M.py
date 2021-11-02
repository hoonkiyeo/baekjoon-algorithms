import sys

N, M = map(int,input().split())

if M == 1:
    for i in range(1, N+1):
        print(i)
else:
    for i in range(1, N+1):
        for j in range(1, i+1):
            print(i, j)