from itertools import combinations

def main():
    tri_list = [int(n*(n+1)/2) for n in range (1,46)]
    answer_sheet = []
    for i in tri_list:
        for j in tri_list:
            for k in tri_list:
                answer_sheet.append(i+j+k)

    size = int(input())
    for q in range(size):
        input_num = int(input())
        if input_num in answer_sheet: print('1')
        else: print('0')

if __name__ == '__main__':
    main()