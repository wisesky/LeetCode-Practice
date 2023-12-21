# Input: S = "ADOBECODEBANC", T = "ABC"
# Output: "BANC"
from collections import Counter, defaultdict

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
    
    # 双指针滑动窗口法， 本质和上一段代码相同，用更容易理解的方法重写一遍
    def slideWindows(self, s, t):
        need = Counter(t)
        windows = defaultdict(lambda : 0)
        # 记录 need 中，字符是否满足数量需求的char 数目
        valids = 0
        # 左边指针left 初始化
        left = 0
        # 记录结果的指针 start 和 有效长度
        start, length = 0, float('inf')
        
        # 右指针循环，开始扩大窗口
        for right, char in enumerate(s):
            if char in need :
                windows[char] += 1
                if windows[char] == need[char]:
                    valids += 1
            # 左指针循环，缩小窗口
            while valids == len(need):
                if right - left < length :
                    length = right - left
                    start = left
                if s[left] in need:
                    if windows[s[left]] == need[s[left]]:
                        valids -= 1
                    windows[s[left]] -= 1
                left += 1
        
        return "" if length is None else s[start:start+length+1]
    
if __name__=='__main__':
    so = Solution()
    S = "ADOBECODEBANC"
    T = "ABC"
    res = so.minWindow(S, T)
    res_1 = so.slideWindows(S, T)
    print(res)
    print('-'*10)
    print(res_1)