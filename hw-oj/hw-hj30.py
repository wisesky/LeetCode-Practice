def reverse(c):
    try:
        it = int(c, base=16)
    except:
        return c
    binary = bin(it)[2: ]
    fills = 4 - len(binary)
    binary = '0'*fills + binary
    # binary.zfill(4)
    r_binary = ''.join(list(reversed(binary)))
    r_int = int(r_binary, base=2)
    r_hex = hex(r_int)[2: ]
    r_hex_upper = r_hex.upper()
    return r_hex_upper

while True:
    try:
        doubleS = input().split()
        # doubleS = 'DKSq8qykpgKIZxiRKmQ9QkZt909PffE6Gyfc57dBx7p20D42bWJRzKqGGCzzQ4p7Z32Dsx2Cf8G2841lPuAZNb K0fHodOVFlbl220ov260TPOrmZ328d1E89OatcL88EXr622RdklXtXazO7wMoc6DEKU45eQ5VBUy2YFjgJX'.split()
        s = ''.join(doubleS)
        # s = sorted(s)
        even = []
        odd = []
        for i,c in enumerate(s):
            if i%2 == 0:
                even.append(c)
            else:
                odd.append(c)
        
        even = sorted(even)
        odd = sorted(odd)
        news = [0]*len(s)
        for i,c in enumerate(even):
            news[2*i] = c
        for j,c in enumerate(odd):
            news[2*j+1] = c
        
        res = []
        for c in news:
            r = reverse(c)
            res.append(r)
            # print(c, r)

        result = ''.join(res)
        print(result)

    except :
        break