from collections import Counter
import sys
from collections import defaultdict

def main():
    # 내 풀이..
    # tree_list = []
    # result_list = []
    #
    # while True:
    #     input_tree = sys.stdin.readline().rstrip()
    #     if input_tree == '': break
    #     tree_list.append(input_tree)
    #
    # tree_list = Counter(tree_list)
    # total = sum(tree_list.values())
    #
    # for a, b in zip(tree_list.keys(), tree_list.values()):
    #     result_list.append((a, b))
    #
    # for a, b in result_list:
    #     per = b/total*100
    #     print("%s, %.4f" %(a, per))

    tree_dict = defaultdict(int)
    total = 0
    while True:
        tree = sys.stdin.readline().rstrip()
        if not tree: break
        tree_dict[tree] += 1
        total += 1

    tree_list = list(tree_dict.keys())
    tree_list.sort()

    for a in tree_list:
        print('%s %.4f' %(a, tree_dict[a] / total * 100))


if __name__ == '__main__':
    main()
