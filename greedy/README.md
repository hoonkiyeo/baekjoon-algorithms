### Greedy Algorithms

---
- Greedy algorithm indicates any simple, intuitive algorithm that is used in optimization problems.
- The greedy algorithm makes the optimal result at each single step as it attempts to find the overall optimal way to solve the problem.

---
### Most challenging problem
```python
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
```
- The above algorithm was the most challening for me, especially when it comes to dealing with indexing