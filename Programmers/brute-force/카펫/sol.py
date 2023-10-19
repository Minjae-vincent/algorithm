def solution(brown, yellow):
    answer = []
    for i in range(3, 5000):
        for j in range(1, i+1):
            if ((i-2)*(j-2) == yellow) and i*j == brown + yellow:
                answer.append(i)
                answer.append(j)
    return answer