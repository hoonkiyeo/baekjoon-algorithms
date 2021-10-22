num = int(input()) #target number (find generator of this num)
result = 0

for i in range(1, num+1):
    digit_sum = sum(list(map(int, str(i)))) #if the number is 256, then the digit_sum is 13
    tot_sum = i + digit_sum
    if tot_sum == num:
        result = i
        break

print(result)

