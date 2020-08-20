import math
label = ['零','壹','贰','叁','肆','伍','陆','柒','捌','玖']
num2lable = { str(i):x for i,x in enumerate(label)}

first = ['','拾','佰','仟']
second = ['万','亿']

def num2Words(num):
    if num < 10:
        return label[num] if num != 0 else ''

    if num < 100:
        pre = num // 10
        if pre == 1:
            prefix = ''
        else: # 2-9
            prefix = label[pre]
        suffix = num2Words(num%10)
        return prefix + '拾' + suffix

    if num < 1000:
        suffix = num2Words(num%100)
        if num%100 < 10 and  len(suffix) > 0:
            suffix = '零' + suffix
        return label[num//100] + '佰' + suffix

    if num < 10000:
        suffix = num2Words(num%1000)
        if num%1000 < 100 and len(suffix) > 0:
            suffix = '零' + suffix
        return label[num//1000] + '仟' + suffix

    p = math.floor(math.log(num, 10000))
    p1 = p % 2
    p2 = p // 2
    part1 =  [] if p1 == 0 else ['万']
    part2 =  ['亿' for _ in range(p2)]
    w = ''.join(part1+part2)

    suffix = num2Words(num%10000**p)
    if (num%10000**p) < (10**(4*p-1)) and len(suffix) > 0:
        suffix = '零' + suffix

    return num2Words(num//10000**p) + w + suffix

# nums = [0, 10,100,1000,10000,1000000]
# nums = [0, 1123,12345,54123,12343543,12334523234136]
# # nums = [x+1 for x in nums]
# for num in nums:
#     print(num2Words(num))

while True:
    try:
        num1, num2 = input().split('.')

        if num2 == '00':
            suffix = '整'
        else:
            suffix = ''
            if num2[0] != '0':
                suffix += num2lable[num2[0]] + '角' 
            if num2[1] != '0':
                suffix += num2lable[num2[1]] + '分'

        prefix = num2Words(int(num1))
        if len(prefix) > 0:
            prefix = prefix + '元'
        print('人民币'+prefix+ suffix)
    except:
        break