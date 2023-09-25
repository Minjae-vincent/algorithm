def solution(arr):
    answer = []
    tmp = arr[0]
    answer.append(tmp)

    for a in arr[1:]:
        if tmp != a:
            answer.append(a)
            tmp = a
    return answer