from itertools import permutations

def main():
    num_list = list(permutations(['1', '2', '3', '4', '5', '6', '7', '8', '9'], 3))
    iter_num = int(input())

    for _ in range (iter_num):
        guess_num, strike, ball = map(int, input().split())
        guess_num = list(str(guess_num))
        reset_num = 0
        for i in range(len(num_list)):
            strike_num, ball_num = 0, 0
            i -= reset_num
            for j in range(3):
                if num_list[i][j] == guess_num[j]: strike_num += 1
                elif guess_num[j] in num_list[i]: ball_num += 1
            if (strike != strike_num) or (ball != ball_num):
                num_list.remove(num_list[i])
                reset_num += 1

    print(len(num_list))





if __name__ == '__main__':
    main()