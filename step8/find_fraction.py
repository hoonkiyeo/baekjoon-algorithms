

# denominator - 1  2 1  1 2 3  4 3 2 1  1 2 3 4 5  6 5 4 3 2 1
# numerator -   1  1 2  3 2 1  1 2 3 4  5 4 3 2 1  1 2 3 4 5 6


x = int(input())
line = 1

while x > line:
    x -= line
    line += 1

if line % 2 == 0:
    a = x
    b = line - x + 1
else:
    a = line - x + 1
    b = x


print(a, "/", b, sep='')




