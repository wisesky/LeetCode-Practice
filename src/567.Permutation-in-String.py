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
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need = Counter(s1)
        valids = 0
        windows = defaultdict(lambda : 0)
        # length = 1
        left = 0
        for right, rc in enumerate(s2):
            windows[rc] += 1
            if rc in need :
                if windows[rc] == need[rc]:
                    valids += 1

            while right - left + 1 == len(s1):
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

                