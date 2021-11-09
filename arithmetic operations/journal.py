import sys


a, b = map(int, sys.stdin.readline().split())
#a: number of articles you plan to publish
#b: impact factor the owners require

result = a * (b-1) + 1

print(result)