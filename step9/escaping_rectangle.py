
x,y,w,h = map(int,input().split())
# x = x-coordinate
# y = y-coordinate
# w = width of rectangle
# h = height of rectangle
# 1 ≤ w, h ≤ 1,000
# 1 ≤ x ≤ w-1
# 1 ≤ y ≤ h-1

width_diff = w-x
height_diff = h-y

min_distance = min(x,y,width_diff, height_diff)
print(min_distance)

#input
'''
6 2 10 3
'''
#output
'''
1
'''