from itertools import permutations


def solution(k, dungeons):
    answer = 0
    for candidate in list(permutations(dungeons)):
        a_tmp = 0
        tmp_k = k
        for tmp in candidate:
            if tmp_k >= tmp[0]:
                tmp_k -= tmp[1]
                a_tmp += 1
            else:
                break
        if a_tmp >= answer: answer = a_tmp

    return answer