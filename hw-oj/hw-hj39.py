def isSubnet(ip1, ip2, mask):
    ip1 = ip1.split('.')
    ip2 = ip2.split('.')
    mask = mask.split('.')

    if len(ip1) !=4 or len(ip2) !=4 or len(mask)!=4:
        return 1

    for i,j,k in zip(ip1, ip2, mask):
        m1 = int(i) & int(k)
        m2 = int(j) & int(k)

        if m1 != m2 :
            return  2

    return 0

while True:
    try:
        mask = input()
        ip1 = input()
        ip2 = input()

        res = isSubnet(ip1, ip2, mask)
        print(res)

    except:
        break