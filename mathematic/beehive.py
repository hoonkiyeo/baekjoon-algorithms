
def beehive(n):
    cnt = 1
    distance = 1
    cnt_six = 6

    while n > cnt:
        distance += 1
        cnt += cnt_six
        cnt_six += 6

    return distance

n = int(input())
result = beehive(n)
print(result)



#input
'''
13
'''
#output
'''
3
'''