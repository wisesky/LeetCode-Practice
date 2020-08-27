def cut8(chars):
    length = len(chars)
    if length < 8:
        fills = 8 - length
        r = chars + '0'*fills
        return [r]

    res = []
    for i in range(0,length,8):
        c = chars[i:i+8]
        if len(c) < 8:
            fills = 8 - len(c)
            r = c + '0'*fills
            res.append(r)
            continue

        res.append(c)

    return res


while True:
    try:
        n = int(input())
        
        result = []
        for _ in range(n):
            chars = input()
            res = cut8(chars)
            result.extend(res)

        for r in result:
            print(r)
    except:
        break