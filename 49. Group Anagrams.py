from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for s in strs:
            sort_s = ''.join(sorted(s))
            if sort_s in d:
                d[sort_s].append(s)
            else:
                tmp = []
                tmp.append(s)
                d[sort_s] = tmp

        return list(d.values())

if __name__ == "__main__":
    
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    so = Solution()
    r = so.groupAnagrams(strs)
    print(r)