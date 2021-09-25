N = int(input())

while True:
    for i in range(2, N+1):
        if N % i == 0:
            print(i)
            N = N // i
            break
    if N <= 1:
        break

#input
'''
72
'''
#output
'''
2
2
2
3
3
'''