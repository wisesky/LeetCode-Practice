from collections import OrderedDict
import sys
def statisErrors(errors):
    res = OrderedDict()

    for error in errors:
        path, lineNum = error.split()
        filename = path.split('\\')[-1]
        if len(filename) > 16:
            filename = filename[-16: ]

        if (filename, lineNum) in res:
            res[filename, lineNum] += 1
        else:
            res[filename, lineNum] = 1

    return res

errors = []    
# E:\V1R2\product\\fpgadrive.c 1325
for line in sys.stdin:
    errors.append(line.strip())

res = statisErrors(errors)

for r in list(res.keys())[-8: ]:
    print(r[0], r[1], res[r])