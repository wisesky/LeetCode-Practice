while True:
    try:
        n, inSeq = int(input()), input().split()

        inSeq = ''.join(inSeq)
        stack = ''
        
        def outSeq(inSeq, stack):
            if len(inSeq) == 0:
                return [''.join(reversed(stack))]
            if len(stack) == 0:
                outLater = outSeq(inSeq[1: ], stack + inSeq[0])
                return outLater
            else:
                head = stack[-1]
                outNow = [head+x for x in outSeq(inSeq, stack[ :-1]) if len(x)!=0]   
                outLater = outSeq(inSeq[1: ], stack + inSeq[0])

                return outNow + outLater
        
        r = outSeq(inSeq, stack)
        # print(len(r))
        r = [' '.join(list(x)) for x in r]
        print('\n'.join(r))

    except:
        break