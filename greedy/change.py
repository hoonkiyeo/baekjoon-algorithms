
import sys

n = int(sys.stdin.readline())
price = 1000-n
cnt = 0
change_list = [500, 100, 50, 10, 5, 1]

for c in change_list:
    if price >= c:
        cnt += price // c
        price -= ((price // c) * c)
        if price == 0:
            break
    continue

print(cnt)
