import sys


def main():
    n, m = map(int, sys.stdin.readline().split())
    num_list = list(map(int, sys.stdin.readline().split()))

    cnt = 0
    right = 1
    left = 0
    sum = num_list[0]

    while True:
        if sum < m:
            if right < n:
                sum += num_list[right]
                right += 1
            else: break
        elif sum == m:
            cnt += + 1
            sum -= num_list[left]
            left += 1
        else:
            sum -= num_list[left]
            left += 1


    print(cnt)



if __name__ == '__main__':
    main()
