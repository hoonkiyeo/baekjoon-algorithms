### Algorithms dealing with combinatorics and number theory
---

---
### Most challenging algorithm: find_integer.py
```python
# runtime error code
def check_integer(lst, n):
    rem_list = []
    for N in lst:
        remainder = N % n
        rem_list.append(remainder)
    rem_list = list(set(rem_list))
    if len(rem_list) == 1:
        return True
    return False

n = int(sys.stdin.readline())
num_list = []
final_list = []

for i in range(n):
    num = int(sys.stdin.readline())
    num_list.append(num)

for i in range(2, max(num_list)):
    if check_integer(num_list, i):
        final_list.append(i)

for ans in final_list:
    print(ans, end=" ")
```
- Need to overcome runtime error
- Need to come up with various number theories (gcd, lcm, divisor, ...) and apply these at the same time

### Final version
```python
import sys
import math

def get_gcd(a,b):
    if b == 0:
        return a
    else:
        return get_gcd(b, a%b)

def div(x):
    div_list = [x]
    for i in range(2, int(x**(1/2) + 1)):
        if x % i == 0:
            div_list.append(i)
            if x//i != i:
                div_list.append(x//i)
    div_list.sort()
    return div_list

n = int(sys.stdin.readline())
num_list = []
for _ in range(n):
    num_list.append(int(sys.stdin.readline()))
num_list.sort(reverse=True)

diff_list = []
for i in range(len(num_list)-1):
    diff_list.append(num_list[i] - num_list[i+1])

gcd = 0
if len(diff_list) == 1:
    gcd = diff_list[0]
elif len(diff_list) == 2:
    gcd = get_gcd(diff_list[0], diff_list[1])
else:
    gcd = diff_list[0]
    for i in range(1, len(diff_list)):
        gcd = get_gcd(gcd, diff_list[i])

for i in div(gcd):
    print(i, end=" ")
```

