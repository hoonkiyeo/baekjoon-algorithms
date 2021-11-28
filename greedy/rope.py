import sys

if __name__ == "__main__":
    n = int(input())  # number of ropes
    rope = []

    for _ in range(n):
        rope.append(int(sys.stdin.readline()))
    rope.sort(reverse=True)

    max_weight = 0
    for i in range(len(rope)):
        weight = rope[i] * (i+1)
        if weight > max_weight:
            max_weight = weight

    print(max_weight)

