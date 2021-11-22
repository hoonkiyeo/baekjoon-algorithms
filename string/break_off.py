import sys


input_str = str(sys.stdin.readline())


for i in range(0, len(input_str), 10):
    print(input_str[i:i+10])