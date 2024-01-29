def main():
    num = int(input())
    bucket = [[0]*num for _ in range(num)]
    result = 0
    for i in range(num):
        input_list = list(input())
        for j in range(len(input_list)):
            bucket[i][j] = input_list[j]

    for i in range(num):
        for j in range(num):
            if (not j == 0) and (not (bucket[i][j] == bucket[i][j-1])):
                bucket[i][j-1], bucket[i][j] = bucket[i][j], bucket[i][j-1]
                result = check_max(num, bucket, result)
                result = check_max(num, list(zip(*bucket)), result)
                bucket[i][j - 1], bucket[i][j] = bucket[i][j], bucket[i][j - 1]
            if (not i == 0) and (not (bucket[i][j] == bucket[i-1][j])):
                bucket[i-1][j], bucket[i][j] = bucket[i][j], bucket[i-1][j]
                result = check_max(num, bucket, result)
                result = check_max(num, list(zip(*bucket)), result)
                bucket[i-1][j], bucket[i][j] = bucket[i][j], bucket[i-1][j]

    print(result)

def check_max(num, target_list, result):
    for i in range(num):
        row_max = 1
        for j in range(num):
            if j != 0:
                if target_list[i][j] == target_list[i][j-1]:
                    row_max += 1
                    result = max(result, row_max)
                else:
                    row_max = 1
    return result





if __name__ == '__main__':
    main()