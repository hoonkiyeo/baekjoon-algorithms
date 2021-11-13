import sys

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

