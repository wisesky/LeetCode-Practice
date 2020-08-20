def longestBP(s):
    news = '_'.join(list(s))
    maxr = 0
    for i, c in enumerate(news):
        r = centerbp(news, i)
        maxr = max(maxr, r)
    
    return maxr
    
def centerbp(s, i):
    length = len(s)
    count = 0
    gap = 1
    while i-gap in range(0, length) and i+gap in range(0, length):
        if s[i-gap] != s[i+gap]:
            break
        if s[i-gap] != '_':
            count += 1
        gap += 1
        
    c = 0 if s[i] == '_' else 1
    return 2*count + c

while True:
    try:
        s = input()
        res = longestBP(s)
        print(res)
    except:
        break