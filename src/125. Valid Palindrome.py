import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = []
        for char in s:
            if char in string.ascii_letters or char in string.digits:
                l.append(char.lower())
        news = '_'.join(l)
        return self.check(news)

    def check(self, news):
        # news = '_'.join(s)
        length = len(news)
        if length == 0:
            return True
        mid = length // 2
        for i in range(mid+1):
            x = mid + i
            y = mid - i
            if news[x] != news[y]:
                return False
        return True

s = '0P'
so = Solution()
r = so.isPalindrome(s)
print(r)