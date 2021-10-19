class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return '0'
        num = abs(numerator)
        denum = abs(denominator)
        if num != numerator:
            flag = denum != denominator
        else:
            flag = denum == denominator
        z = num // denum
        f = num % denum

        r = []
        fs = [f]
        while f != 0:
            s = f*10

            fz = s // denum
            f = s % denum
            r.append(str(fz))
            if f in fs:
                break
            fs.append(f)

        str_z = '-' + str(z) if flag == False else str(z)
        if len(r) == 0:
            return str_z

        if f == 0:
            return str_z + '.' + ''.join(r)

        pos = fs.index(f)
        p1 = ''.join(r[ :pos])
        p2 = '(' + ''.join(r[pos: ]) + ')'
        
        return str_z + '.' + p1 + p2

numerator = 0
denominator = -5

so = Solution()
print(so.fractionToDecimal(numerator, denominator))