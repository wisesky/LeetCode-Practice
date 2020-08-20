import sys

lines = []
for line in sys.stdin:
    lines.append(line.strip())

def split8(row):
    lrow = len(row)
    res = []
    r = []
    for i, c in enumerate(row):
        if (i % 8 == 0 and i!=0) or i == lrow:
            res.append(''.join(r))
            r = []
        r.append(c)
    
    while len(r) != 8:
        r.append('0')
    res.append(''.join(r))

    return res

def split8_new(row):
    lrow = len(row)
    n = lrow // 8
    r = []
    for i in range(0,lrow, 8):
        r.append(row[i:i+8])

    last = r[-1]
    while len(last) < 8:
        last += '0'
    r[-1] = last
    return r

i = 0
l = len(lines)


while i < l:
    n = int(lines[i])
    for j in range(n):
        row = lines[i+j+1]
        res = split8_new(row)
        # res = split8(row)
        for r in res:
            print(r)

    i = i + n + 1