import sys

def main():
    length, stop_point_num, r_f, r_b = map(int, input().split())
    stop_point = []
    point, result = 0, 0
    for _ in range(stop_point_num):
        stop_point.append(tuple(map(int, sys.stdin.readline().strip().split())))

    stop_point.sort(key= lambda x: x[1], reverse=True)

    for a, b in stop_point:
        if point < a:
            result += (abs(r_b - r_f)) * (abs(point - a)) * b
            point = a
    #
    # tmp1 = stop_point[0]
    # stop_point = list(filter(lambda x: x[0] > tmp1[0], stop_point))
    # stop_point.append(tmp1)
    # stop_point.sort(key=lambda x: x[1], reverse=True)
    #
    # while True:
    #     result += (abs(r_b - r_f))*(abs(point - stop_point[0][0])) * stop_point[0][1]
    #
    #     point = stop_point[0][0]
    #
    #     stop_point = stop_point[1:]
    #     if len(stop_point) == 0: break
    #     tmp1 = stop_point[0]
    #     stop_point = list(filter(lambda x: x[0] > tmp1[0], stop_point))
    #     stop_point.append(tmp1)
    #     stop_point.sort(key=lambda x: x[1], reverse=True)


    print(result)


if __name__ == '__main__':
    main()
