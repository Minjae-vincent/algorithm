def main():
    input_list = []
    flag = True

    for _ in range(9):
        input_list.append(int(input()))


    result_list = input_list
    for i in range(9):
        for j in range(9):
            if not (i == j):
                if sum(input_list) - (input_list[i] + input_list[j]) == 100:
                    a, b = input_list[i], input_list[j]
                    result_list.remove(a)
                    result_list.remove(b)
                    flag = False
                    break
        if not flag: break

    result_list = d(result_list)


    for i in range(len(result_list)):
        print(result_list[i])




if __name__ == '__main__':
    main()