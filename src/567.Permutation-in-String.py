#! python3
# -*- encoding: utf-8 -*-
'''
@File   : 567.Permutation-in-String.py
@Time   : 2023/12/21 10:33:53
@Author : Franklin Chen
@Contact: wisesky1988@gmail.com
@Licence: MIT License
@Desc   : 
'''
from collections import Counter, defaultdict
class Solution:
    # 滑动窗口双指针法
    # 题目关键在于，substring 的每个字母的计数，来判断是否是完全相同的子序列
    # need 用来计算目标序列计数， windows 用来计算待选序列的计数
    # valids 则来判断相同数目的字母的个数，如果valids == len（need）代表windows 里面的序列和 need序列数目完全一样，是超集
    # 但是不代表windows == need ，还需要更强的条件限制，length == len(s1)
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need = Counter(s1)
        valids = 0
        windows = defaultdict(lambda : 0)
        # length = 1
        left = 0
        # 右指针先移动，并且字符划入窗口计数
        for right, rc in enumerate(s2):
            windows[rc] += 1
            if rc in need :
                # valids 只有在字符相同的时候才更新
                if windows[rc] == need[rc]:
                    valids += 1
            # 左指针移动条件： 窗口内序列是否和目标序列s1一样
            # 一般来说，left指针都是用来缩减窗口的，所以为避免bug，length >= len(s1)
            while right - left + 1 == len(s1):
                # 如果满足 length == len(s1) 同时 valids == len(need)，代表是全排列子序列
                if valids == len(need) :
                    return True
                lc = s2[left]
                if lc in need:
                    if windows[lc] == need[lc]:
                        valids -= 1
                windows[lc] -= 1
                left += 1
                # length = right - left + 1

        return False
    
if __name__ =="__main__":
    so = Solution()
    s1 = 'ab'
    s2 = 'eidboaooo'
    result = so.checkInclusion(s1, s2)
    print(result)

                