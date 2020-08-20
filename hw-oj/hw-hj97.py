while True:
    try:
        n = int(input())
        # nums = input.split()
        nums = map(int, input().split())
        count = 0
        pos = []
        # for i in range(n):
        for num in nums:
            # num = int(num)
            if num < 0:
                count += 1
            elif num > 0:
                pos.append(num)

        print(count, ' ', round(sum(pos)/len(pos), 1))
                # print(str(neg)+" 0" if not pos else str(neg)+" "+"{0:.1f}".format(sum(pos)/len(pos)))
    except:
        break