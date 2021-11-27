import sys

num = int(sys.stdin.readline())
result = ""
sum = 0
for i in str(num):
    sum += int(i)

if '0' not in str(num) or sum % 3 != 0:
    print(-1)
else:
    lst = sorted(str(num), reverse=True)
    for i in lst:
        result += i
    print(int(result))