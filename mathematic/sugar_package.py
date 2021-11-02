sugar = int(input())#n killograms of sugar

bag = 0 #total packages

while sugar >= 0:
    if sugar % 5 == 0:
        bag += (sugar // 5)
        print(bag)
        break
    sugar -= 3
    bag += 1

else:
    print(-1)

#input
'''
18
'''
#output
'''
4
'''