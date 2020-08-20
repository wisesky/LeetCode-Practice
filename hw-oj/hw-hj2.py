

while True:
    try:
        chars = input()
        tgt = input()

        d = {}
        for c in chars:
            cl = c.lower()
            if cl in d:
                d[cl] += 1
            else:
                d[cl] = 1

        tgtl = tgt.lower()
        r = d.get(tgtl, 0)
        print(r)

    except:
        break