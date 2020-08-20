def combine(lr, li):
    rk2rv = {}
    for k,v in enumerate(lr):
        rk2rv[k] = v

    pre = float('inf')
    res = []
    for k,v in sorted(rk2rv.items(), key=lambda x: (x[1],x[0])):
        if v == pre:
            continue
        r = searchi(li, v)
        if len(r) > 0:
            res.append(v)
            res.append(len(r)//2)
            res.extend(r)

        pre = v

    length = len(res)
    return [length] + res

def searchi(li, v):
    str_v = str(v)
    r = []
    for j, iv in enumerate(li):
        str_iv = str(iv)
        if str_v in str_iv:
            r.append(j)
            r.append(iv)

    return r


while True:
    try:
        seqi = list(map(int, input().split()))
        seqr = list(map(int, input().split()))
        length_i, li = seqi[0], seqi[1: ]
        length_r, lr = seqr[0], seqr[1: ]

        res = combine(lr, li)
        str_res = [str(x) for x in res]
        print(' '.join(str_res))

    except:
        break