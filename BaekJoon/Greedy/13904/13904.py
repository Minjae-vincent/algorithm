
def main():
    n = int(input())
    homework_list = []
    check_list = [False]* 1001
    result = 0

    for _ in range(n):
        homework_list.append(tuple(map(int, input().split())))

    homework_list = sorted(homework_list, key=lambda x: x[1], reverse=True)

    for day, score in homework_list:
        i = day
        while i > 0 and check_list[i]:
            i -= 1
        if i == 0: continue
        else:
            check_list[i] = True
            result += score

    print(result)





if __name__ == '__main__':
    main()
