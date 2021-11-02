import sys

N,K = map(int, input().split())
#N: the number of coins needed to make target amount
#K: target amount

c_list = []
cnt = 0
for i in range(N):
    amount = int(sys.stdin.readline())
    if amount <= K:
        c_list.append(amount)

for num in c_list[::-1]:
    if K // num == 0:
        continue
    cnt += K // num
    K -= (num * (K // num))
    if K == 0:
        break

print(cnt)

