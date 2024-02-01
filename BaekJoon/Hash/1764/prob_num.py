import sys
from collections import Counter


def main():
    n, m = map(int, sys.stdin.readline().split())
    tmp_list = []
    result_list = []
    for _ in range(n):
        tmp_list.append(sys.stdin.readline().strip())

    for _ in range(m):
        tmp_list.append(sys.stdin.readline().strip())

    aa = dict(Counter(tmp_list))

    for key, value in aa.items():
        if value > 1: result_list.append(key)

    print(len(result_list))
    for a in sorted(result_list):
        print(a)


if __name__ == '__main__':
    main()
