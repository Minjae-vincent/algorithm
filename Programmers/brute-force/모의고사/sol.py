def solution(answers):
    tmp_1 = [1, 2, 3, 4, 5]
    tmp_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    tmp_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    ans_1 = []
    ans_2 = []
    ans_3 = []
    answer = []

    tmp = [0, 0, 0]

    for _ in range(2000):
        ans_1.extend(tmp_1)

    for _ in range(1584):
        ans_2.extend(tmp_2)

    for _ in range(1000):
        ans_3.extend(tmp_3)

    for idx, value in enumerate(answers):
        if value == ans_1[idx]:
            tmp[0] += 1
        if value == ans_2[idx]:
            tmp[1] += 1
        if value == ans_3[idx]:
            tmp[2] += 1

    tmp_max = max(tmp)

    for idx, value in enumerate(tmp):
        if tmp_max == value:
            answer.append(idx + 1)

    return answer