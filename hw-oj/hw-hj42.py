while True:
    try:
        chars = input()
        # nums = int(chars)
        level0 = ['zero']
        level1 = ['','one','two','three','four','five','six', 'seven',' eight','nine', 'ten']
        level1_1= ['','eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixten', 'seventeen', 'eighteen', 'nineteen']
        level2 = ['','','twenty','thirty', 'forty', 'fifty','sixty',' seventy', 'eighty', 'ninety']
        high = ['','thousand','million','billion']
        levelAnd = ['and']

        def threeNumTran(num3):
            if len(num3) == 0:
                return  ''
            out = []
            length = len(num3)
            one = int(num3[-1])
            two = int(num3[-2]) if length >1 else 0
            three = int(num3[-3]) if length >2 else 0

            if two == 1:
                out.append(level1_1[one])
            else:
                out.extend([level2[two]  ,level1[one]])
            
            if three != 0:
                out = [level1[three] , 'hundred' , 'and'] + out
            # print(out)
            return ' '.join([x for x in out if len(x)!=0])

        # def high2Val(numThousand):
        #     n = int(num123
        # Thousand // 3)
        #     left = numThousand % 3

        #     return [high[left]] + ['billion' for _ in range(n)]

        def pos2Unit(pos):
            # assert pos % 3 == 0
            numThousand = int( (pos-1) // 3)

            n = int(numThousand // 3)
            left = numThousand % 3
            r = [high[left]] + ['billion' for _ in range(n)]
            r = [x for x in r if len(x)!=0]
            return ' '.join(r)

        def pos2Unit_dfs(pos):
            if pos < 3:
                if pos == 0:
                    return []
                if pos == 1:
                    return ['thousand']
                if pos == 2:
                    return ['million']

            return pos2Unit_dfs(pos-3) + ['billion']


        length = len(chars)
        parts = []
        units = []
        for i in range(length, -1,-3):
            ed = i
            st = i-3 if i-3>0 else 0
            num3 = chars[st:ed]
            if len(num3) != 0:
                part = threeNumTran(num3)
                
                pos = length - st
                unit = pos2Unit(pos)

                parts.append(part)
                units.append(unit)

        res = []
        for k,v in zip(parts, units):
            # print(k,v)
            # if len(k)!=0:
            #     r = [k,v]
            res.append(' '.join([k,v]))

        output = ' '.join(reversed(res))
        print(output)

    except :
        break