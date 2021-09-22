N = int(input()) # N <= 100
cnt = 0
num_list = list(map(int,input().split()))

def is_prime(num):
    if num == 2 or num == 3:
        return True
    if num % 2 == 0 or num == 1:
        return False
    for i in range(3, int(num**1/2)+1, 2):
        if num % i == 0:
            return False
    return True
for num in num_list:
    if is_prime(num):
        cnt += 1
print(cnt)

#input
'''
4
1 3 5 7
'''
#output
'''
3
'''