import sys

def counting_sort(N):
    cnt_arr = [0] * 10001
    for i in range(N):
        num = int(sys.stdin.readline())
        cnt_arr[num] += 1

    for i in range(10001):
        if cnt_arr[i] != 0:
            for j in range(cnt_arr[i]):
                print(i)

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    counting_sort(N)


