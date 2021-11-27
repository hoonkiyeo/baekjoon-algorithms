import sys

n = int(input())

for i in range(n):
    size = int(sys.stdin.readline())
    score_list = []
    cnt = 1
    for j in range(size):
        a,b = map(int, sys.stdin.readline().split())
        score_list.append((a,b))
    score_list.sort(key = lambda x: x[0])
    mx = score_list[0][1]
    for k in range(1, len(score_list)):
        if score_list[k][1] < mx:
            cnt += 1
            mx = score_list[k][1]
    print(cnt)