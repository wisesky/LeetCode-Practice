from collections import OrderedDict

while True:
    try:
        n, flag = int(input()), input()
        d = []
        for _ in range(n):
            name, score = input().split()
            d.append((name, int(score)))

        isReverse = flag == '0'
        rd = sorted(d, key= lambda x: x[1],reverse=isReverse)
        for r in rd:
            print(' '.join([str(x) for x in r]))

    except :
        break