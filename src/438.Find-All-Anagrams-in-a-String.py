#! python3
# -*- encoding: utf-8 -*-
'''
@File   : 438.Find-All-Anagrams-in-a-String.py
@Time   : 2023/12/21 11:15:23
@Author : Franklin Chen
@Contact: wisesky1988@gmail.com
@Licence: MIT License
@Desc   : 
'''
from collections import Counter, defaultdict
    # 滑动窗口双指针法：
    # 同 567
class Solution:
    def findAnagrams(self, s: str, p: str) :
        need = Counter(p)
        valids = 0
        windows = defaultdict(lambda : 0)
        # length = 1
        left = 0
        res = []
        # 右指针先移动，并且字符划入窗口计数
        for right, rc in enumerate(s):
            windows[rc] += 1
            if rc in need :
                # valids 只有在字符相同的时候才更新
                if windows[rc] == need[rc]:
                    valids += 1
            # 左指针移动条件： 窗口内序列是否和目标序列p一样
            # 一般来说，left指针都是用来缩减窗口的，所以为避免bug，length >= len(p)
            while right - left + 1 == len(p):
                # 如果满足 length == len(p) 同时 valids == len(need)，代表是全排列子序列
                if valids == len(need) :
                    # return True
                    res.append(left)
                lc = s[left]
                if lc in need:
                    if windows[lc] == need[lc]:
                        valids -= 1
                windows[lc] -= 1
                left += 1
                # length = right - left + 1

        return res

if __name__ =="__main__":
    so = Solution()
    p = 'ab'
    s = 'eidbaooo'
    result = so.findAnagrams(s, p)
    print(result)