import math

N = int(input()) # 0<=N<=12

#solution_1 (library implementation)
answer = math.factorial(N)
print(answer)

#solution_2
answer2 = 1
for i in range(N,0,-1):
    answer2 *= i
print(answer2)

#input
'''
10
'''

#output
'''
3628800
3628800
'''