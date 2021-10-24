# time complexity of O(N^2)
n = int(input())
num_list = []
for i in range(n):  # O(N)
    num_list.append(int(input()))
num_list = sorted(num_list)
for i in range(len(num_list)):  # O(N)
    print(num_list[i])
