# Input: S = "ADOBECODEBANC", T = "ABC"
# Output: "BANC"
from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t) # 记录t中所有字符 与 指针之前对应字符出现的频次 的差值
                            # 作为判断 new start 的依据
        missing = len(t) # 记录到指针目前为止， t中缺失字符的个数
        start , minStart= 0, 0
        minLen = float('inf')
        for end, char in enumerate(s):
            if need[char] > 0:
                missing -= 1
            need[char] -= 1
            
            # check new start
            # 判断条件是, missing 已经完全不缺失，可以搜索新起点，new start
            while missing == 0:
                # 在 s[start:end] 之间 搜索 new start
                # new start 的特征是， 作为 start:end 的左边界，必须是不可缺失的字符
                # 因为假如 左边界的字符 在 start:end 中继续出现，说明左边界仍然可以缩减并右移动
                if end-start < minLen:
                    minLen = end-start
                    minStart = start
                
                need[s[start]] += 1
                if need[s[start]] > 0:
                    missing += 1
                start += 1
        
        if minLen != float('inf'):
            return s[minStart:minStart+minLen+1] # minStart+minLen = minEnd 是枚举中实际可以访问的idx，作为索引则要+1
        return ''

if __name__=='__main__':
    so = Solution()
    S = "ADOBECODEBANC"
    T = "ABC"
    res = so.minWindow(S, T)
    print(res)