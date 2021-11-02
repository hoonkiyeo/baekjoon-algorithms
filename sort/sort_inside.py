import sys

def sort_inside(num):
    digit_list = []
    for letter in str(num):
        digit_list.append(int(letter))
    for n in sorted(digit_list, reverse = True):
        print(n,end="")

if __name__ == "__main__":
    num = int(sys.stdin.readline())
    sort_inside(num)


