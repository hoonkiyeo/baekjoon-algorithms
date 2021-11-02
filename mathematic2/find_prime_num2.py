
M = int(input())
N = int(input())

min = 0
sum = 0
num_list = []

def is_prime(num):
    if num == 1:
        return False
    elif num == 2:
        return True
    for i in range(2,num):
        if num % i == 0:
            return False
    return True

for i in range(M,N+1):
    if is_prime(i):
        num_list.append(i)
        sum += i

if len(num_list) == 0:
    print(-1)
else:
    min = num_list[0]
    print(sum)
    print(min)

#input
'''
60
100
'''
#output
'''
620
61
'''
#input2
'''
64
65
'''
#output2
'''
-1
'''