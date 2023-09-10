def main():
    score_dict = {"A+": 4.5, "A0": 4.0, "B+": 3.5, "B0": 3.0, "C+": 2.5, "C0": 2.0, "D+": 1.5, "D0": 1.0, "F": 0.0}
    sum_total = 0
    b = 0

    for _ in range(20):
        q, p, r = input().split()
        if r == "P": continue
        sum_total += (float(p)*float(score_dict.get(r)))
        b += float(p)
    print(round((sum_total/b), 6))

if __name__ == '__main__':
    main()