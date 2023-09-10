def main():
    n = int(input())
    cnt = 0
    for _ in range(n):
        word = input()
        if is_group_word(word):
            cnt += 1
    print(cnt)

def is_group_word(word):
    word_set = set()
    prev = ''
    for c in word:
        if c not in word_set:
            word_set.add(c)
            prev = c
        elif prev == c:
            continue
        else:
            return False
    return True


if __name__ == '__main__':
    main()