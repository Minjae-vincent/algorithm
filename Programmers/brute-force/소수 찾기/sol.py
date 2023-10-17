from itertools import combinations
from itertools import permutations


def is_prime(num):
    if num == 1 or num == 0: return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def solution(numbers):
    answer = 0
    num_int = []
    integer_set = set()

    for idx, value in enumerate(list(numbers)):
        num_int.append(int(value))

    for i in range(1, len(num_int) + 1):
        tmp = list(combinations(num_int, i))
        for a in set(tmp):
            for b in permutations(a):
                integer_set.add(int(''.join(map(str, b))))

    for value in integer_set:
        if is_prime(value):
            print(value)
            answer += 1

    return answer