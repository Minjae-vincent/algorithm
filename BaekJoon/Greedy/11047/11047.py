def main():
    num, remained = map(int, input().split())
    money_list = []
    cnt = 0
    for _ in range(num):
        money_list.append(int(input()))
    while True:
        if remained == 0: break
        money_list = sorted(list(filter(lambda x: x <= remained, money_list)), reverse=True)

        cnt += int(remained // money_list[0])
        remained = int(remained % money_list[0])

    print(cnt)


if __name__ == '__main__':
    main()
