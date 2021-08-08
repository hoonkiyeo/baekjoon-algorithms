def climing(a,b,v):

    cnt_day = (v-b) / (a-b)

    if cnt_day == int(cnt_day):
        return int(cnt_day)
    else:
        return int(cnt_day) + 1
a,b,v = map(int,input().split())
result = climing(a,b,v)
print(result)