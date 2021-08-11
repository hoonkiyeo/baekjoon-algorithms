
# denominator - 1  2 1  1 2 3  4 3 2 1  1 2 3 4 5  6 5 4 3 2 1
# numerator -   1  1 2  3 2 1  1 2 3 4  5 4 3 2 1  1 2 3 4 5 6


x = int(input())
line = 1

while x > line:
    x -= line
    line += 1

if line % 2 == 0:
    denom = line - x + 1
    numer = x
else:
    denom = x
    numer = line - x + 1

print(numer, "/", denom, sep="")

#input
'''
14
'''
#output
'''
2/4
'''



