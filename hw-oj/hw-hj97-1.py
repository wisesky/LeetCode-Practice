import sys

lines = []
for line in sys.stdin:
    lines.append(line.strip())

n = int(lines[0])

nums = []
count = 0
for num in lines[1: ]:
    num = int(num)
    if num > 0:
        nums.append(num)
    elif num < 0:
        count += 1

mean = round(sum(nums) / len(nums), 1)

output = ' '.join([str(count), str(mean)])
print(output)