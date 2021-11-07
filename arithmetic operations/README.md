### Arithmetic operations

---
- There are basic algorithms in this folder, especially basic algorithms using python built-in arithmetic operations such as [+, -, *, //, %, /]


### Representative algorithm
```python
import sys

h, m = map(int,sys.stdin.readline().split())
oven_time = int(sys.stdin.readline())

m += oven_time

if m > 59:
    h += (m // 60)
    m -= (m // 60) * 60
if h > 23:
    h = h % 24

print(h, m)
```