import sys

n = int(input())
word_list = []

for i in range(n):
    word = sys.stdin.readline().strip()
    word_list.append(word)

word_list = list(dict.fromkeys(word_list)) #remove duplicates
word_list.sort()
word_list.sort(key = len)

for word in word_list:
    print(word)
