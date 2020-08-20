while True:
    try:
        s1, s2 = input(), input()
        flag = 'true'
        for s in s1:
            if s not in s2:
                flag = 'false'
                break
        print(flag)
        
    except :
        break