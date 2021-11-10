import sys

def count_coins(n, target):
    c_list = []
    cnt = 0
    for i in range(n):
        amount = int(sys.stdin.readline())
        if amount <= target:
            c_list.append(amount)
    for num in c_list[::-1]:
        cnt += target // num
        target -= (num * (target // num))
        if target == 0:
            break
    return cnt

if __name__ == "__main__":
    n, target = map(int, sys.stdin.readline().split())
    # N: the number of coins needed to make target amount
    # K: target amount
    print(count_coins(n,target))
