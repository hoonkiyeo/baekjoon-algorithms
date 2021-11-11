import sys

def find_num_by_divisor(n, div_list):
    min_div = min(div_list)
    max_div = max(div_list)
    target_num = min_div*max_div
    return target_num

if __name__ == "__main__":
    n = int(sys.stdin.readline())  # the number of divisors
    div_list = list(map(int, sys.stdin.readline().split()))  # divisors
    print(find_num_by_divisor(n, div_list))