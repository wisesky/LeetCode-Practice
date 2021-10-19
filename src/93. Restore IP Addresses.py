from typing  import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = self.constructIP([],s)
        result =  []
        for r in res:
            r = [str(x) for x in r]
            result.append('.'.join(r))
        return result

    def constructIP(self, res, remain_s):
        if len(remain_s) == 0:
            return []
        if len(res) == 3:
            ip4 = int(remain_s)
            if str(ip4) != remain_s:
                return []
            if ip4 in range(256):
                return [res+[ip4] ]
            else:
                return []

        length = min(len(remain_s), 3)

        r = []
        for i in range(length):
            ref_s = remain_s[ :i+1]
            ref_ip = int(ref_s)
            # 判别 0 是否会被int 忽略 
            if ref_s != str(ref_ip):
                continue
            if ref_ip in range(256):
                tmp = self.constructIP(res+[ref_ip], remain_s[i+1: ])
                r.extend(tmp)
        
        return r

s = '192168011'
so = Solution()
result = so.restoreIpAddresses(s)
print(result)