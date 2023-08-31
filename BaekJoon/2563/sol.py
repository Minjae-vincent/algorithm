def main():
    num = input()
    draw_back = [[0]*100 for i in range(100)]
    for _ in range(int(num)):
        x, y = map(int, input().split())
        for i in range(10):
            for j in range(10):
                draw_back[x+i][y+j] = 1
    print(sum(sum(draw_back,[])))




if __name__ == '__main__':
    main()