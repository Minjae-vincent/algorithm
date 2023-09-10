def main():
    num = int(input())
    list_tuple = []
    for _ in range(num):
        tmp_input = input().split()
        list_tuple.append(tuple(int(item) for item in tmp_input))
    result = sorted(list_tuple, key=lambda x: (x[0], x[1]))
    for i in range(len(result)):
        print(result[i][0], result[i][1])


if __name__ == '__main__':
    main()