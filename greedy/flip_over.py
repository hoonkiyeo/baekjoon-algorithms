s = input()
cnt = 0

for i in range(1, len(s)):
    if s[i] != s[i-1]:
        cnt += 1

if cnt == 0:
    print(0)
elif cnt == 1:
    print(1)
elif cnt == 2:
    print(1)
elif cnt % 2 == 0:
    print(cnt // 2)
else:
    print((cnt // 2) + 1)