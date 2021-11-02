### Sorting Algorithms (with time complexity)

- There are 10 algorithm problems in step12
- Algorithms dealing with sorting and time complexity
- Algorithms dealing with sorting coordinates
---
### Most challenging algorithm

- Counting sort algorithm was the most challenging in this step.
```python
import sys

def counting_sort(N):
    #1
    cnt_arr = [0] * 10001
    for i in range(N):
        num = int(sys.stdin.readline())
        #2
        cnt_arr[num] += 1
    #3
    for i in range(10001):
        if cnt_arr[i] != 0:
            for j in range(cnt_arr[i]):
                print(i)

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    counting_sort(N)
```


