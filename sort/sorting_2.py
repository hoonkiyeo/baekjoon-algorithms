import sys

# time complexity of O(NlogN)
n = int(input()) #1 ≤ n ≤ 1,000,000

num_list = []
for i in range(n):
    num_list.append(int(sys.stdin.readline()))

for num in sorted(num_list):
    print(num)
