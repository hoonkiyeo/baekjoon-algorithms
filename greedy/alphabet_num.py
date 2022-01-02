import sys

n = int(input())
word_list = []
word_dic = {}
ans = 0

for _ in range(n):
    word_list.append(sys.stdin.readline().rstrip())

for words in word_list:
    size = len(words) - 1
    for alphabet in words:
        if not alphabet in word_dic:
            word_dic[alphabet] = (10 ** size)
        else:
            word_dic[alphabet] += (10**size)
        size -= 1

value_list = list(word_dic.values())
value_list.sort(reverse=True)

for i in range(len(value_list)):
    ans += (value_list[i] * (9 - i))

print(ans)