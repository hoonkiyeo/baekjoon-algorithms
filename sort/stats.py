import statistics
import sys
from collections import Counter

n = int(sys.stdin.readline())
num_list = []
for i in range(n):
    num_list.append(int(sys.stdin.readline()))
num_list = sorted(num_list)

duplicates = Counter(num_list).most_common() #count the number of occurences of each element in the list (in ascending order)
if len(duplicates) > 1 and duplicates[0][1] == duplicates[1][1]:
    mode = duplicates[1][0]
else:
    mode = duplicates[0][0]

mean = round(statistics.mean(num_list))
median = statistics.median(num_list)
rng = max(num_list) - min(num_list)
print(mean, median, mode, rng, sep="\n")