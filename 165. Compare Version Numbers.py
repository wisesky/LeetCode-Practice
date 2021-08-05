class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        l1 = version1.split('.')
        l2 = version2.split('.')
        length1 = len(l1)
        length2 = len(l2)
        if length1 == 0 or length2 == 0:
            if length1 != 0:
                return 1
            if length2 != 0:
                return -1
            return 0

        length = min(length1, length2)
        for i in range(length):
            v1 = int(l1[i])
            v2 = int(l2[i])
            if v1 > v2:
                return 1
            if v1 < v2:
                return -1
        if length1 > length:
            j = length
            while j < length1:
                v1 = int(l1[j])
                if v1 > 0:
                    return 1
                j += 1
            return 0
        if length2 > length:
            j = length
            while j < length2:
                v2 = int(l2[j])
                if v2 > 0:
                    return -1
                j += 1
            return 0
        return 0

version1 = '7.5.2.4'
version2 = '7.5.3'

so = Solution()
print(so.compareVersion(version1, version2))
