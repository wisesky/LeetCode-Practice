while True:
    try:
        num1, num2 = input().split('.')

        label = ['零','壹','贰','叁','肆','伍','陆','柒','捌','玖']
        num2lable = { str(i):x for i,x in enumerate(label)}

        first = ['','拾','佰','仟']
        second = ['万','亿']
        

        def split4(chars):
            output = []
            prelabel = ''
            for i, c in enumerate(reversed(chars)):
                curlabel = num2lable[c]
                if curlabel == prelabel and curlabel == '零':
                    continue
                if curlabel == '壹' and first[i] == '拾' and i == len(chars) - 1:
                    output.append('拾')
                    break
                output.append(curlabel + first[i])
                prelabel = curlabel

            output = reversed(output)
            return ''.join(output)
        
        
        if num2 == '00':
            suffix = '整'
        else:
            suffix = ''
            if num2[0] != '0':
                suffix += num2lable[num2[0]] + '角' 
            if num2[1] != '0':
                suffix += num2lable[num2[1]] + '分'


        l = len(num1)
        # revnum = ''.join(reversed(num1))
        units = []
        res = []
        pre = ''
        for i in range(l,-1,-4):
            ed = i
            st = i-4 if i-4>=0 else 0
            four = num1[st:ed]
            r = split4(four)
            res.append(r)

            if pre == '' :
                pre = '元'
            elif pre == '元':
                pre = '万'
            else: # pre[0] == '万'
                if pre[0] == '万':
                    pre = '亿' + pre[1: ]
                else: # 亿
                    pre = '万' + pre[1: ]
            units.append(pre)

        prefix = ''
        for k,v in zip(res, units):
            prefix = k + v + prefix
        if int(num1) == 0:
            prefix = ''

        print('人民币'+prefix+suffix)

    except:
        break
