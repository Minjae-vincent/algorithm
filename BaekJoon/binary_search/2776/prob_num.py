import sys


def binary_search(ans_list, val):
    start_idx = 0
    end_idx = len(ans_list) - 1
    while start_idx <= end_idx:
        mid = (start_idx + end_idx) // 2
        if ans_list[mid] == val:
            return True
        elif ans_list[mid] > val:
            end_idx = mid -1
        else:
            start_idx = mid + 1
    return False

def main():
    t = int(sys.stdin.readline())

    for _ in range(t):
        n = int(sys.stdin.readline())
        ans_list = list(map(int, sys.stdin.readline().split()))
        ans_list = sorted(ans_list, key=lambda x: x)
        m = int(sys.stdin.readline())
        response_list = list(map(int, sys.stdin.readline().split()))
        for i in range(m):
            if binary_search(ans_list, response_list[i]):
                print(1)
            else:
                print(0)


if __name__ == '__main__':
    main()
