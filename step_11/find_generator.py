num = int(input())


for i in range(1, num+1):
    digit_sum = sum(list(map(int, str(i))))
    result = i + digit_sum
    if result == num:
        print(i)
        break
    if i == num:
        print(0)


