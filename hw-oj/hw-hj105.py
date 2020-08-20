import sys

lines = []

for line in sys.stdin:
    lines.append(line.strip())


nums = [int(x) for x in lines]

count = 0
nonNeg = []

for num in nums:
    if num < 0:
        count += 1
    else:
        nonNeg.append(num)

l = len(nonNeg)
if l > 0:
    mean = round(sum(nonNeg) / len(nonNeg), 1)
else:
    mean = 0.0

print(count)
print(mean)