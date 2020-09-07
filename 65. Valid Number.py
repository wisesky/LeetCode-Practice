import string

class Solution:
    def isNumber(self, s: str) -> bool:
        s = ''.join(s.strip())

        if 'e' in s:
            newS = s.split('e')
            if len(newS) != 2:
                return False
            # newS = [x for x in newS if x]
            
            pre, post = newS
            return self.isNum(pre) and self.isInt(post)
            
        else:
            return self.isNum(s)
        
    def isNum(self, part):
        return self.isInt(part) or self.isFloat(part)
        
    def isInt(self, part):
        if part.startswith('-') or part.startswith('+'):
            part = part[1: ]
        if len(part) == 0:
            return False
        for char in part:
            if char not in string.digits:
                return False
        return True

    def isFloat(self, part):
        if part.startswith('-') or part.startswith('+'):
            part = part[1: ]

        if '.' in part:
            dots_parts = part.split('.')
            if len(dots_parts) != 2 :
                return False
            dots_parts = [x for x in dots_parts if x]
            if len(dots_parts) == 0:
                return False
            for dots_part in dots_parts:
                if not self.isInt(dots_part) or dots_part.startswith('+') or dots_part.startswith('-'):
                    return False
            return True  
        else:
            return False

if __name__ == "__main__":
    so = Solution()
    s = "e.7e5"
    r = so.isNumber(s)
    print(r)