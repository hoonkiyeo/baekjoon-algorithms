import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
arr2 = sorted(list(set(arr)))

# for num in arr:
#     print(x.index(num), end=" ") (Time complexity of O(N^2))

#Time complexity of O(N)
dic = {}
for i in range(len(arr2)):
    dic[arr2[i]] = i
for num in arr:
    print(dic[num], end=" ")






