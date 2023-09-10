def main():
    num = int(input())
    input_list = list(map(int, input().split(' ')))

    for i in range(1, num):
        input_list[i] = max(input_list[i], input_list[i] + input_list[i - 1])

    print(max(input_list))



if __name__ == '__main__':
    main()