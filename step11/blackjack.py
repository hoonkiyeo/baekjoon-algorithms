
N, M = map(int, input().split())#N refers to the number of cards and M refers to the number that we must not exceed.

a = list(map(int, input().split())) #five cards

sum = 0

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if a[i] + a[j] + a[k] > M:
                continue
            else:
                sum = max(sum, a[i] + a[j] + a[k])



print(sum)


