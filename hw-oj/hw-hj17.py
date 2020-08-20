def move(movements):
    pos = [0,0]
    mts = movements.split(';')
    for m in mts:
        # flag = m.startswith('A') or m.startswith('D') or m.startswith('W') or m.startswith('S')
        # if not flag or len(m) < 2:
        if len(m) < 2:
            continue
        direct = m[ :1]
        distance = m[1: ]
        try:
            distance = int(distance)
        except:
            continue
        
        if m.startswith('A'):
            pos[0] = pos[0] - distance
        elif m.startswith('D'):
            pos[0] = pos[0] + distance
        elif m.startswith('W'):
            pos[1] = pos[1] + distance
        elif m.startswith('S'):
            pos[1] = pos[1] - distance
        else:
            continue

    return pos

while True:
    try:
        seqs = input()
        pos = move(seqs)
        str_pos = [str(x) for x in pos]
        res = ','.join(str_pos)
        print(res)

    except:
        break