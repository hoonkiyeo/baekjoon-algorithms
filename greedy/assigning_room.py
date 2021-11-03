import sys

n = int(sys.stdin.readline())
time_list = []
cnt = 1

for i in range(n):
    start, end = map(int,sys.stdin.readline().split())
    time_list.append((start,end))

time_list.sort(key = lambda x: (x[1], x[0]))

standard = time_list[0][1]
for i in range(1, n):
    if time_list[i][0] >= standard:
        cnt += 1
        standard = time_list[i][1]

print(cnt)

