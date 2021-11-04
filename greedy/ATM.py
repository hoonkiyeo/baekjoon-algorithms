import sys

def atm_line(n):
    tot = 0
    time_list = sorted(list(map(int, sys.stdin.readline().split())))

    for i in range(len(time_list)):
        tot += sum(time_list[:i+1])

    return tot

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    print(atm_line(n))
