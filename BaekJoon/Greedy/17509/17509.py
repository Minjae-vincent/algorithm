def main():
    num_list = []
    for i in range(11):
        num_list.append(tuple(map(int, input().split())))
    num_list = sorted(num_list, key=lambda x: (x[0], x[1]))
    result = num_list[0][0] + 20*num_list[0][1]
    tmp = num_list[0][0]
    for a in num_list[1:]:
        tmp += a[0]
        result += tmp + 20*a[1]

    print(result)







if __name__ == '__main__':
    main()
