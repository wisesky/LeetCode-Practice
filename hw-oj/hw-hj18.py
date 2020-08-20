import sys

def transformMask(mask):
    ms = mask.split('.')
    r = []
    for m in ms:
        try:
            bm = bin(int(m))[2: ]
        except:
            return False, ''

        if len(bm) > 8:
            return False, ''
        str_bm = bm.zfill(8)
        r.append(str_bm)

    res = ''.join(r)
    return True, res 

def isValidMask(binary_mask):
    pre = '1'
    if not binary_mask.startswith('1') or binary_mask.endswith('1'):
        return False
    switch = False
    for c in binary_mask:
        if c != pre:
            if switch:
                return False
            else:
                switch = True
                pre = '0'
    return True

def transformIp(ip):
    ips = ip.split('.')
    r = []
    for i in ips:
        if i == '*':
            continue
        try:
            bi = bin(int(i))[2: ]
        except:
            return False, ''

        if len(bi) > 8:
            return False, ''
        str_bi = bi.zfill(8)
        r.append(str_bi)

    res = ''.join(r)
    return True, res
        

def ipMask2Subnet(binary_ip, binary_mask):
    res = []
    for i in range(0,32,8):
        t_ip = binary_ip[i:i+8]
        t_mask = binary_mask[i:i+8]
        r = int(t_ip, base=2) & int(t_mask, base=2)
        res.append(r)
    return res

def isPrivateIp(ip_list):
    if ip_list[0] == 10:
        return True
    if ip_list[0] == 172 and ip_list[1] in range(16, 32):
        return True
    if ip_list[0] == 192 and ip_list[1] == 168:
        return True
    return False

a,b,c,d,e,error,private = [0]*7

# lines = []
for line in sys.stdin:
    # lines.append(line.strip())
    # print(line)
    ip, mask = line.strip().split('~')
    
    
    flag_mask, binary_mask = transformMask(mask)
    if not flag_mask or not isValidMask(binary_mask):
        error += 1
        continue

    flag_ip, binary_ip = transformIp(ip)
    if not flag_ip :
        error += 1
        continue
    #  127.*.*.*  ==> True '' 
    if len(binary_ip) == 0:
        continue

    res = ipMask2Subnet(binary_ip, binary_mask)
    # assert len(res) == 4
    # for i in res[1: ]:
    #     if i != 0:
    #         error += 1
    #         continue

    r = res[0]
    if r in range(1, 127):
        a += 1
    elif r in range(128, 192):
        b += 1
    elif r in range(192, 224):
        c += 1
    elif r in range(224, 240):
        d += 1
    elif r in range(240, 256):
        e += 1
    else:
        error += 1
        continue

    if isPrivateIp(res):
        private += 1

print(a,b,c,d,e,error, private)

# while True:
#     try:
#         print(a,b,c,d,e,error, private)
#         ip, mask = input().split('~')
        
#         flag_mask, binary_mask = transformMask(mask)
#         if not flag_mask or not isValidMask(binary_mask):
#             error += 1
#             continue

#         flag_ip, binary_ip = transformIp(ip)
#         if not flag_ip :
#             error += 1
#             continue
#         #  127.*.*.*  ==> True '' 
#         if len(binary_ip) == 0:
#             continue
    
#         res = ipMask2Subnet(binary_ip, binary_mask)
#         # assert len(res) == 4
#         # for i in res[1: ]:
#         #     if i != 0:
#         #         error += 1
#         #         continue

#         r = res[0]
#         if r in range(1, 127):
#             a += 1
#         elif r in range(128, 192):
#             b += 1
#         elif r in range(192, 224):
#             c += 1
#         elif r in range(224, 240):
#             d += 1
#         elif r in range(240, 256):
#             e += 1
#         else:
#             error += 1
#             continue

#         if isPrivateIp(res):
#             private += 1

        
#     except:
#         break