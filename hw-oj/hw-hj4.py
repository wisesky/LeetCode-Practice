def cut8(chars):
    length = len(chars)
    if length < 8:
        fills = 8 - length
        r = chars + '0'*fills
        return [r]

    res = []
    for i in range(0,length, 8):
        c = chars[i:i+8]
        leth = len(c)
        if leth < 8:
            fills = 8 - leth
            r = c + '0'*fills
            res.append(r)
            continue
        # leth == 8
        res.append(c)

    return res
        

while True:
    try:
        chars = input()
        res = cut8(chars)
        result = '\n'.join(res)
        print(result)

    except:
        break