import math

#D(T1,T2) = |x1 - x2| + |y1 - y2|

radius = int(input())

euclidian = math.pi*(radius**2)
#We define π to be the ratio of the circumference of a circle to its diameter in taxicab geometry
taxicab = 2*(radius**2)

print(format(euclidian, ".6f"))
print(format(taxicab, ".6f"))


