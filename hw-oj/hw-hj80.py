while True:
    try:
        n1, num1, n2, num2, = int(input()), list(map(int, input().split())), int(input()), list(map(int, input().split()))
        l1 = len(num1)
        l2 = len(num2)

        i,j = 0, 0
        r = []
        while i<l1 or j<l2:
            if i>=l1:
                while j<l2:
                    if num2[j] not in r :
                        r.append(num2[j])
                    j += 1
                break
            if j>=l2:
                while i<l1:
                    if num1[i] not in r:
                        r.append(num1[i])
                    i += 1
                break
        
            x = num1[i]
            y = num2[j]
            if x > y:
                if y not in r:
                    r.append(y)
                j += 1
            elif x < y:
                if x not in r:
                    r.append(x)
                i += 1
            else:
                if x not in r:
                    r.append(x)
                i += 1
                y += 1
        
        output = ''.join([str(x) for x in r])
        print(output)

    except :
        break