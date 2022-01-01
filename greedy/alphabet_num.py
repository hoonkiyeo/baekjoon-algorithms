import sys

n = int(input())
word_list = []
dic = {}
ans = 0

for _ in range(n):
    word_list.append(sys.stdin.readline().rstrip())

for words in word_list:
    size = len(words)
    for word in words:
        if word not in dic:
            dic[word] = (10**(size-1))
        else:
            dic[word] += (10**(size-1))
        size -= 1

value_list = list(dic.values())
value_list.sort(reverse=True)

num = 9
for value in value_list:
    ans += value * num
    num -= 1

print(ans)