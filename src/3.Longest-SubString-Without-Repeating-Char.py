#! python3
# -*- encoding: utf-8 -*-
'''
@File   : 3.Longest-SubString-Without-Repeating-Char.py
@Time   : 2023/12/21 11:30:59
@Author : Franklin Chen
@Contact: wisesky1988@gmail.com
@Licence: MIT License
@Desc   : 
'''
from collections import Counter, defaultdict
class Solution:
    # 滑动窗口双指针法:
    # 关键还是判断左指针滑动条件： 新添加进来right 是否导致重复字符，如果是，那么通过滑动左边窗口消灭重复字符  
    def lengthOfLongestSubstring(self, s: str):
        windows = defaultdict(lambda : 0)
        left = 0
        length = 0
        for right, rc in enumerate(s):
            windows[rc] += 1

            while windows[rc] > 1:
                lc = s[left]
                windows[lc] -= 1
                left += 1
    
            length = max(length, right-left+1)

        return length
    # Trick Solution: 通过记录每个字符 crt 之前出现过的位置 c2idx: character -> last seen
    # 这样left = max(目前为止，所有出现过的字符的 last seen)
    # 实际上是一个更加优化版本的滑动窗口
    # The function iterates through the string "s", updating the "left" pointer and "res" as it finds non-repeating substrings.
    def lengthOfLongestSubstring_2(self, s: str):
        length = len(s)
        if length == 0:
            return 0
        res = 0
        # c2idx = defaultdict(lambda : 0)
        c2idx = {}
        left = 0
        for right, rc in enumerate(s):
            if rc in c2idx:
                left = max(left, c2idx[rc] + 1)
            c2idx[rc] = right
            res = max(res, right-left+1)

        return res
    
if __name__=="__main__":
    so = Solution()
    # s = 'abcabcbb'
    # s = 'bbbbb'
    # s = 'pwwkew'
    s = 'ebcabe'
    result_1 = so.lengthOfLongestSubstring(s)
    result_2 = so.lengthOfLongestSubstring_2(s)
    print(result_1)
    print('-'*20)
    print(result_2)
