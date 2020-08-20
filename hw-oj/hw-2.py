import heapq
from collections import OrderedDict

class Solution:
    def unitErrs(self, lines):
        r = OrderedDict()

        for i,line in enumerate(lines):
            path, row = line.split(' ')
            filename = path.split('\\')[-1]
            nameRow = ' '.join([filename, row])
            r[nameRow] = r.get(nameRow, 0) + 1

        res = sorted(r.items(), key=lambda x: x[1], reverse=True)

        result = []
        for k,v in res[ :8]:
            result.append(str(k) + ' ' + str(v))

        return '\n'.join(result)

if __name__ == "__main__":
    lines = ['E:\V1R2\product\\fpgadrive.c 1325',
            'E:\V1R2\product\\fpgadrive.c 1326'   ]   
    so = Solution()
    result = so.unitErrs(lines)

    print(result)


