def scramble(s, d):
    if len(s) == 1:
        return s
    if s in d.keys():
        return d[s]
    r = []
    for i in range(1,len(s)):
        s1 = s[ :i]
        s2 = s[i: ]
        r1 = scramble(s1, d)
        r2 = scramble(s2, d)
        
        for e1 in r1:
            for e2 in r2:
                res = [e1+e2, e2+e1]
                r.extend(res)
    d[s] = set(r)
    return d[s]

if __name__ == "__main__":
    d = {}
    # s = 'great'
    s = "abcdefghijklmn"
    result = scramble(s, d)
    # print("efghijklmncadb" in result)
    print(result)