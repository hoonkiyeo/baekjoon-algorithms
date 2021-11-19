import sys

n,m = map(int,sys.stdin.readline().split())


def count_div(k,n):
    result = 0
    while k != 0:
        k = k // n
        result += k
    return result


print(min(count_div(n,2)-count_div(m,2)-count_div(n-m,2), count_div(n,5)-count_div(m,5)-count_div(n-m,5)))