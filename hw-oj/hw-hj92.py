import string
while True:
    try:
        chars = input()
        pre = ''
        res = [[]]
        for i, c in enumerate(chars):
            if c in string.digits:
               res[-1].append(c)
            else:
                if len(res[-1]) != 0:
                    res.append([])

        length = [len(x) for x in res]
        maxLen = max(length)
        result = []
        for i, l in enumerate(length):
            if l == maxLen:
                result.append(''.join(res[i]))

        output = ''.join(result)
        output = ','.join([output, str(maxLen)])
        print(output)

    except :
        break