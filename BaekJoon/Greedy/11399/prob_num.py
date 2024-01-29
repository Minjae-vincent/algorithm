import sys


def main():
    n = int(sys.stdin.readline())
    wait_list = list(map(int, sys.stdin.readline().split()))
    wait_list.sort()

    ans = wait_list[0]
    tmp = wait_list[0]

    for a in wait_list[1:]:
        tmp = tmp + a
        ans = ans + tmp

    print(ans)






if __name__ == '__main__':
    main()
