def climing(a,b,v):
    cnt_day = (v-b) / (a-b)

    if a==b:
        print("cannot determine the number of days it needs to climb to the top")
        print("a and b must be different")

    if cnt_day == int(cnt_day):
        return int(cnt_day)
    else:
        return int(cnt_day) + 1

a,b,v = map(int,input().split())
result = climing(a,b,v)
print(result)


#input
'''
2 1 5
'''
#output
'''
4
'''