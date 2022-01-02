import heapq
import sys


n = int(input())
deck = []

for _ in range(n):
    deck.append(int(sys.stdin.readline()))

heapq.heapify(deck)
ans = 0

if len(deck) == 1:
    print(0)
else:
    while True:
        a = heapq.heappop(deck)
        b = heapq.heappop(deck)
        ans += a+b
        heapq.heappush(deck, a+b)
        if len(deck) == 1:
            break
    print(ans)

