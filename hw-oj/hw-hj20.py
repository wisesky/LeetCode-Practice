import string
def validPasswd(chars):
    length = len(chars)
    if length <= 8:
        return False
    
    digits = 0
    lower = 0
    upper= 0
    other = 0

    for c in chars:
        if c in string.digits:
            digits = 1
        elif c in string.ascii_lowercase:
            lower = 1
        elif c in string.ascii_uppercase:
            upper = 1
        else:
            other = 1

    flag_sum = digits + lower + upper + other
    if flag_sum < 3:
        return False
    
    for i in range(length-3):
        pre = chars[ :i]
        mid = chars[i:i+3]
        post = chars[i+3: ]

        if mid in pre or mid in post:
            return False

    return True


while True:
    try:
        passwd = input()
        flag = validPasswd(passwd)
        if flag:
            print('OK')
        else:
            print('NG')
    except:
        break