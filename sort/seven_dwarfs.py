import sys

if __name__ == "__main__":
    n = 9
    heights = [int(sys.stdin.readline()) for _ in range(n)]
    tot = sum(heights)

    for i in range(n):
        for j in range(i+1, n):
            if tot - (heights[i]+heights[j]) == 100:
                dwarf1 = heights[i]
                dwarf2 = heights[j]
                break

    heights.remove(dwarf1)
    heights.remove(dwarf2)
    heights.sort()

    for h in heights:
        print(h)