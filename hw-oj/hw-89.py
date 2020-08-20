def permutate(vals):
    r = []
    for i in range(4):
        for j in range(4):
            if j == i:
                continue
            for k in range(4):
                if k == i or k == j:
                    continue
                for l in range(4):
                    if l ==i or l ==j or l ==k:
                        continue
                    r.append([vals[i],vals[j],vals[k],vals[l]])

    return r

def permutate_new(vals, sublist=[]):
    if len(sublist) == len(vals):
        perm_r.append(sublist)
        return
    
    for val in vals:
        if val in sublist:
            continue
        newSublist = sublist.copy()
        newSublist.append(val)
        permutate_new(vals, newSublist)

from itertools import permutations
import random

def calbyops(n1, n2, ops):
    if ops == '+':
        return n1 + n2
    elif ops == '-':
        return n1 - n2
    elif ops == '*':
        return n1 * n2
    elif ops == '/':
        return n1 / n2

def calVals(chars):
    vals = []
    for c in chars:
        if c not in s2v:
            return 'ERROR'
        vals.append(s2v[c])
        
    for i in ops:
        # ri = calbyops(vals[0], vals[1] , i)
        for j in ops:
            # rj = calbyops(ri, vals[2] , j)
            for k in ops:
                # rk = calbyops(rj, vals[3], k)
                evl = '('+'('+str(vals[0])+i+str(vals[1])+')'+j+str(vals[2])+')'+k+str(vals[3])
                exp = chars[0] + i + chars[1] + j + chars[2] + k + chars[3]
                rk = eval(evl)
                if rk == 24:
                    # return ''.join([str(v2s[vals[0]]) , i , str(v2s[vals[1]]) , j , str(v2s[vals[2]]) , k ,  str(v2s[vals[3]])])
                    return exp
    return 'NONE'    


s2v = {str(x):x for x in range(1,11)}
s2v['J'] = 11
s2v['Q'] = 12
s2v['K'] = 13
s2v['A'] = 1
v2s = {v:k for k,v in s2v.items()}
ops = ['+','-','*','/']

while True:
    try:
        chars = input().split()
        vals = []
        
        if len(chars) != 4:
            print('ERROR')
            break

        perms = permutations(chars)
        r = ''
        for perm in perms:
            r = calVals(perm)
            if r != 'NONE' :
                break
        print(r)
    except:
        break
