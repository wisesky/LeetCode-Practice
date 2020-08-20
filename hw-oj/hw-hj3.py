import sys

lines = []

for line in sys.stdin:
    lines.append(line.strip())

def deAndSort(nums, n):
    snums = list(set(nums))
    r = sorted(snums)
    return r

le = len(lines)
res = []
i = 0
# for i in range(0, len(lines), 2):
while i < le:
    n = lines[i]
    n = int(n)
    nums = []
    for j in range(n):
        nums.append(lines[int(i+j+1)])
    nums = [int(x) for x in nums]
    r = deAndSort(nums, n)
    res.extend(r)
    i = i + n + 1

for e in res:
    print(e)