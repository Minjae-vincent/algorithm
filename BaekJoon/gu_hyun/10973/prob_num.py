import sys
from itertools import permutations

def main():
    n = int(sys.stdin.readline())
    tmp_list = list(map(int, sys.stdin.readline().strip().split()))
    for i in range(n-1, 0, -1):
        if tmp_list[i-1]> tmp_list[i]:
            for j in range(n-1, 0, -1):
                if tmp_list[i-1] > tmp_list[j]:
                    tmp_list[i-1], tmp_list[j] = tmp_list[j], tmp_list[i-1]
                    tmp_list = tmp_list[:i] + sorted(tmp_list[i:], reverse=True)
                    print(*tmp_list)
                    exit()

    print(-1)



if __name__ == '__main__':
    main()
