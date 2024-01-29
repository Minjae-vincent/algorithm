def main():
    num = int(input())
    meeting_list = []
    result = 1
    for _ in range(num):
        meeting_list.append(tuple(map(int, input().split())))

    meeting_list = sorted(meeting_list, key=lambda x: x[0])
    meeting_list = sorted(meeting_list, key=lambda x: x[1])
    tmp_tuple = meeting_list[0]

    for a in meeting_list[1:]:
        if tmp_tuple[1] <= a[0]:
            result += 1
            tmp_tuple = a



    print(result)

if __name__ == '__main__':
    main()
