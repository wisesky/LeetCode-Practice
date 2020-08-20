from collections import OrderedDict
def delMin(chars):
    d = OrderedDict()
    for c in chars:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1

    minv = min(d.values())
    r = []
    for c in chars:
        if d[c] > minv:
            r.append(c)
    
    res = ''.join(r)
    return res

while True:
    try:
        chars = input()
        res = delMin(chars)
        print(res)
    except:
        break