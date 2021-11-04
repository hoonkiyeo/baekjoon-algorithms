import sys

n = int(sys.stdin.readline())
time_list = []
cnt = 1
for i in range(n):
    start, end = map(int,sys.stdin.readline().split())
    time_list.append((start,end))

time_list.sort(key = lambda x: (x[1], x[0]))
meeting_time = time_list[0]
for i in range(1, len(time_list)):
    if time_list[i][0] >= meeting_time[1]:
        cnt += 1
        meeting_time = time_list[i]

if __name__ == "__main__":
    print(cnt)
