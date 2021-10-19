import re

class Solution:
    def simplifyPath(self, path: str) -> str:
        cur = ['']
        dirs = re.split('/+', path)
        dirs = filter(lambda x: x, dirs)

        for dirName in dirs:
            if dirName == '.':
                pass
            elif dirName == '..':
                if len(cur) == 1:
                    continue
                else:
                    cur.pop()
            else:
                cur.append(dirName)

        if len(cur) == 1:
            return '/'
        return '/'.join(cur)

if __name__ == "__main__":
    so = Solution()
    path = "/../"
    path = "/home//foo/"
    # path = '/home/'
    # path = "/a/./b/../../c/"
    # path ="/a/../../b/../c//.//"
    # path ="/a//b////c/d//././/.."
    res = so.simplifyPath(path)
    print(res)