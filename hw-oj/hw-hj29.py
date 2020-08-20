import string
def encrypt(c):
    if c in string.digits:
        pos = string.digits.index(c)
        des = pos+1 if c != '9' else 0
        return string.digits[des]
    elif c in string.ascii_uppercase:
        pos = string.ascii_uppercase.index(c)
        des = pos+1 if c!='Z' else 0
        return string.ascii_uppercase[des].lower()
    elif c in string.ascii_lowercase:
        pos = string.ascii_lowercase.index(c)
        des = pos+1 if c!='z' else 0
        return string.ascii_lowercase[des].upper()
    else:
        return c

def decrypt(c):
    if c in string.digits:
        pos = string.digits.index(c)
        des = pos-1 if c != '0' else 9
        return string.digits[des]
    elif c in string.ascii_uppercase:
        pos = string.ascii_uppercase.index(c)
        des = pos-1 if c!='a' else 25
        return string.ascii_uppercase[des].lower()
    elif c in string.ascii_lowercase:
        pos = string.ascii_lowercase.index(c)
        des = pos-1 if c!='A' else 25
        return string.ascii_lowercase[des].upper()
    else:
        return c

while True:
    try:
        src = input()
        tgt = input()

        ensrc = []
        for c in src:
            ensrc.append(encrypt(c))
        print(''.join(ensrc))

        detgt = []
        for c in tgt:
            detgt.append(decrypt(c))
        print(''.join(detgt))
    except :
        break