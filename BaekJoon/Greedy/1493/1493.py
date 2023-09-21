import sys

def main():
    p, q, r = map(int, input().split())
    n = int(input())

    result, tmp = 0, 0

    cube_bucket = []
    for _ in range(n):
        cube_bucket.append(tuple(map(int, input().split())))

    cube_bucket.sort(reverse= True)

    goal_volume = p*q*r

    for b, num in cube_bucket:
        tmp *= 8
        a = 2 ** b
        limit = (q//a) * (p//a) * (r//a) - tmp
        limit_result = min(num, limit)

        result += limit_result
        tmp += limit_result

    if goal_volume == tmp:
        print(result)
    else:
        print(-1)


if __name__ == '__main__':
    main()
