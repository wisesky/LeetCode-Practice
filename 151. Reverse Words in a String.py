class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        words = words[ : :-1]
        return ' '.join(words)

s = 'a b c'
s = "a good   example"
so = Solution()
print(so.reverseWords(s))