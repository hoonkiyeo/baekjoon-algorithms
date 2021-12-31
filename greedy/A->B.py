a,b = map(int, input().split())
cnt = 1


if __name__ == "__main__":
    while True:
        if b == a:
            break
        elif a > b:
            cnt = -1
            break
        elif b % 10 == 1:
            b //= 10
            cnt += 1
        elif b % 2 == 0:
            b //= 2
            cnt += 1
        else:
            cnt = -1
            break
    print(cnt)

