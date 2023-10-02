import math


def solution(progresses, speeds):
    answer = []
    tmp = []
    for a, b in zip(progresses, speeds):
        tmp.append(math.ceil((100 - a) / b))

    first = tmp[0]
    answer.append(1)
    num = 0

    print(tmp)

    for aa in tmp[1:]:
        if first >= aa:
            answer[num] += 1
        else:
            first = aa
            num += 1
            answer.append(1)

    return answer