

def main():
    consent_len, n = map(int, input().split())
    if consent_len >= n:
        print(0)
        exit()

    data_list = list(map(int,input().split()))
    consent = set()
    result = 0
    # for i in range(n):
    #     if len(consent) < consent_len:
    #         consent.append(data_list[i])
    #     elif data_list[i] in consent: continue
    #     else:
    #         result += 1
    #         tmp = data_list[i:]
    #         max_num = 0
    #         target = ''
    #         flag = False
    #         for a in consent:
    #             if a in tmp:
    #                 tmp.reverse()
    #                 max_num = max(max_num, len(tmp) - tmp.index(a))
    #                 if max_num == len(tmp) - tmp.index(a): target = a
    #             else:
    #                 flag = True
    #                 consent.remove(a)
    #                 consent.append(data_list[i])
    #                 break
    #         if not flag:
    #             if max_num == 0:
    #                 consent.remove(consent[0])
    #                 consent.append(data_list[i])
    #             else:
    #                 consent.remove(target)
    #                 consent.append(data_list[i])
    #
    # print(result)

    for idx, data in enumerate(data_list):
        # consent가 set 자료형이기 때문에 같은 게 넣어도 consent set의 개수에는 변화가 없음!
        consent.add(data)
        if len(consent) > consent_len:
            result += 1
            latest_used = find_latest(idx, data_list, consent, n)
            consent.discard(latest_used)

    print(result)



def find_latest(idx, data_list, consent, n):
    latest_idx = 0
    max_num = -1
    for num in consent:
        try:
            tmp = data_list[idx:]
            num_idx = tmp.index(num)
        except ValueError:
            num_idx = n
        if max_num < num_idx:
            latest_idx, max_num = num, num_idx

    return latest_idx





if __name__ == '__main__':
    main()