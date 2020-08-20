import math
def numberToWords(num):
    to19='one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen seventeen sixten eighteen nineteen'.split()
    tens="twenty thirty forty fifty sixty seventy eighty ninety".split()
    # thousands = "_ thousand million billion".split()
    def words(n):
        if n<20:return to19[n-1:n]
        if n<100:return [tens[n//10-2]]+words(n%10)
        if n<1000:
            remainder = words(n%100)
            if len(remainder) == 0:
                suffix = []
            else:
                suffix = ['and'] +  remainder
            return [to19[n//100-1]]+["hundred"] + suffix

        p = math.floor(math.log(n, 1000))   
        p1 = p // 3
        p2 = p % 3
        pre = []
        if p2 == 1:
            pre.append('thousand')
        elif p2 == 2:
            pre.append('million')
        else:
            pass
        pre.extend(['billion' for _ in range(p1)])
        w = ' '.join(pre)
        # print('w : ',w)
        # for p,w in enumerate(('thousand',"million","billion"),1):
        #     if n<1000**(p+1):
        return words(n//1000**p)+[w]+words(n%1000**p)
        
    return " ".join(words(num)) or "Zero"
while True:
    try:
        print(numberToWords(int(input())))
    except:break
