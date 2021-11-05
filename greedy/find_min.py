import sys

def find_min(equation):
    result = 0
    for num in equation[0].split("+"):
        result += int(num)
    for i in equation[1:]:
        for j in i.split("+"):
            result -= int(j)
    return result

if __name__ == "__main__":
    equation = sys.stdin.readline().split("-")
    print(find_min(equation))