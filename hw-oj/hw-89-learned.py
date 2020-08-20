import sys
import itertools
 
def calc_24points(data):
    map2={'J':'11','Q':'12','K':'13','A':'1'}
    new_data=[]
    for d in data:
        if d in map2:
            new_data.append(map2[d])
        else:
            new_data.append(d)
 
    map1={'0':'+','1':'-','2':'*','3':'/'}   
    # 生成数字位的排列序列
    for o in (''.join(x) for x in itertools.product(map(str,range(4)), repeat=3)):
        # (1775)# 生成运算符位的可能性组合
        for i in itertools.permutations(range(4),4):
            temp1='(('+new_data[i[0]]+map1[o[0]]+new_data[i[1]]+')'+map1[o[1]]+new_data[i[2]]+')'+map1[o[2]]+new_data[i[3]]
            temp2=data[i[0]]+map1[o[0]]+data[i[1]]+map1[o[1]]+data[i[2]]+map1[o[2]]+data[i[3]]
            if ('joker' in temp1)&('JOKER' in temp1):
                print('ERROR')
                return
            elif eval(temp1)==24:
                    print(temp2)
                    return                
    print('NONE')
 
for line in sys.stdin:
    data = list(map(str, line.strip().split()))
    calc_24points(data)