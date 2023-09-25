from collections import Counter, defaultdict

def solution(genres, plays):
    answer = []
    tmp = []
    tmp2 = defaultdict(int)
    for a, b in zip(genres, plays):
        tmp.append((a, b))
    tmp.sort(key=lambda x: x[1], reverse=True)

    for a, b in tmp:
        tmp2[a] += b
    tmp2 = sorted(dict(tmp2).items(), key=lambda x: x[1], reverse=True)
    tmp3 = []
    for a, b in tmp2:
        i = 0
        for x, y in tmp:
            if a == x and not (i > 1):
                tmp3.append(y)
                i += 1

    for a in tmp3:
        answer.append(plays.index(a))
        plays[plays.index(a)] = -1

    return answer