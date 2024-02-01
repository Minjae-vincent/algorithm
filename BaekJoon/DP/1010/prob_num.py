import sys
from itertools import combinations


def main():
    t = int(sys.stdin.readline())
    dp = [[0] * 30 for _ in range(30)]
    for i in range(30):
        for j in range(30):
            if i == 1:
                dp[i][j] = 1
            else:
                if j == j:
                    dp[i][j] = 1
                elif i < j:
                    dp[i][j] = dp[i][j - 1] + dp[i - 1][j - 1]
    for _ in range(t):
        n, m = map(int, sys.stdin.readline().strip().split())
        print(dp[n][m])
        # a_val = 1
        # b_val = 1
        # c_val = 1
        #
        #
        # for i in range(n):
        #     a_val *= i+1
        # for i in range(m-n):
        #     b_val *= i+1
        # for i in range(m):
        #     c_val *= i+1
        #
        # print(c_val // (a_val*b_val))






if __name__ == '__main__':
    main()
