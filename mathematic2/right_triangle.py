import sys


while True:
    nums = list(map(int, sys.stdin.readline().split()))

    if nums[0] == 0 and nums[1] == 0 and nums[2] == 0:
        break
    max_num = max(nums)
    nums.remove(max_num)
    if nums[0]**2 + nums[1]**2 == max_num**2:
        print("right")
    else:
        print("wrong")

#input
'''
6 8 10
25 52 60
5 12 13
0 0 0
'''
#output
'''
right
wrong
right
'''
