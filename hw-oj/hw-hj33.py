def ip2num(ip):
    ip = ip.split('.')

    
    binary_list = [bin(int(i))[2: ] for i in ip]
    binary_fills = []
    for b in binary_list:
        bf = 8 - len(b)
        bt = '0'*bf + b
        binary_fills.append(bt)
    binary_str = ''.join(binary_fills)
    return int(binary_str, base=2)

def num2ip(num):
    binary = bin(int(num))[2: ]
    if len(binary) < 32:
        fills = 32 - len(binary)    
        adds = '0' * fills
        binary = adds + binary
    
    ip_list = []
    for pos in range(0,25,8):
        n = binary[pos:pos+8]
        n = int(n, base=2)
        if n > 255:
            return 0
        
        ip_list.append(str(n))

    ip_str = '.'.join(ip_list)
    return ip_str

while True:
    try:
        ip = input()
        num = input()
        # ip = '10.0.3.193'
        # num = '167969729'

        newNum = ip2num(ip)
        newIp = num2ip(num)

        print(newNum)
        print(newIp)
    except:
        break