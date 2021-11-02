N = int(input())
target = "666"
start = int(target)
cnt = 0

while True:
    if target in str(start):
        cnt += 1
    if cnt == N:
        print(start)
        break
    start += 1