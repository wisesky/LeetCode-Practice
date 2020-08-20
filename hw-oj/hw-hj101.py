import sys

lines = []
for line in sys.stdin:
    lines.append(line.strip())

l = len(lines)
i = 0
# res = []
while i < l:
    n = int(lines[i])
    if n > 0:
        row = lines[i+1]
        flag = lines[i+2]
        row = row.split(' ')
        row = [int(x) for x in row]
        row = sorted(row, reverse=True if flag=='1' else False)
        print(' '.join([str(x) for x in row]))
        # res.extend(row)
    i = i+3

# res = sorted(res)
# print(' '.join([str(x) for x in res]))

# for i in range(0,l,2):
#     n = int(lines[i])
#     if n == 0:
#         break
#     row = lines[i+1].split(' ')
#     row = [int(x) for x in row]
#     row = sorted(row)
#     print(' '.join([str(x) for x in row]))
