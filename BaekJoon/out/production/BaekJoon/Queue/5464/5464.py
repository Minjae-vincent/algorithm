from collections import deque

def check_is_ok(parking_list):
    for i in range(len(parking_list)):
        if parking_list[i][1] > 0: return True
    return False



def main():
    n, m = map(int, input().split())
    parking_list = []
    car_list = []
    waiting_queue = deque()
    result = 0
    for _ in range(n):
        tmp = int(input())
        parking_list.append((tmp, 0))

    for _ in range(m):
        tmp = int(input())
        car_list.append(tmp)

    print('parking list: ', parking_list)
    print('car list: ', car_list)

    locate_num = 2*m

    while locate_num > 0:
        car_num = int(input())
        # 주차장 입장
        if car_num > 0:
            target_car = car_list[car_num - 1]
            waiting_queue.append(target_car)
            if check_is_ok(parking_list):
                tmp = waiting_queue.popleft()
                for i in range(len(parking_list)):
                    if parking_list[i][1] == 0:
                        parking_list[i][1] = tmp
                result += tmp
        # 주차장 퇴장
        else:
            car_num *= -1
            target_car = car_list[car_num - 1]
            for i in range(len(parking_list)):
                if parking_list[i][1] == target_car:
                    parking_list[i][1] = 0
        locate_num -= 1

    print(result)



if __name__ == '__main__':
    main()
