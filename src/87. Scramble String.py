from collections import Counter
class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        #print(s1, s2)
        if Counter(s1) != Counter(s2):
            return False
        for i in range(1, len(s1)):
            if self.isScramble(s1[ :i], s2[ :i]) & self.isScramble(s1[i: ], s2[i: ]):
                return True
            if self.isScramble(s1[ :i], s2[-i: ]) & self.isScramble(s1[i: ], s2[ :-i]):
                return True
        return False

if __name__ == "__main__":
    s1 = 'abced'
    s2 = 'caebd'
    # s1 = 'abcdefghijklmn'
    # s2 = 'efghijklmncadb'
    so = Solution()
    print(so.isScramble(s1,s2))
