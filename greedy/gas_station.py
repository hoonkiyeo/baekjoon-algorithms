import sys
def min_cost(n, path, price):
    tot_price = 0
    start = price[0]

    for i in range(len(path)): #O(N)
        tot_price += start*path[i]
        if start > price[i+1]:
            start = price[i+1]
    return tot_price

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    path = list(map(int, sys.stdin.readline().split())) #distance between each gas station
    price = list(map(int, sys.stdin.readline().split())) #oil price per litter of each gas station
    print(min_cost(n,path,price))


