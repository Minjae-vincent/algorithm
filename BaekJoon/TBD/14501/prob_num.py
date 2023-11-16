def main():
    n = int(input())
    day_list = []
    dp = [0 for _ in range(n+1)]
    for _ in range(n):
        t, p = map(int, input().split(" "))
        day_list.append([t, p])

    for i in range(n-1, -1, -1):
        if i + day_list[i][0] > n:
            dp[i] = dp[i+1]
        else:
            dp[i] = max(dp[i+1], dp[i+day_list[i][0]] + day_list[i][1])

    print(dp[0])









if __name__ == '__main__':
    main()
