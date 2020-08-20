import sys

lines = []
for line in sys.stdin:
    lines.append(line.strip())

l = len(lines)

def minOut(nums, n):
    leftRes = [0]*n
    rightRes = [0]*n

    for left in range(1,n):
        leftVal = nums[left]
        leftMax = -1
        for i in range(left):
            if nums[i] < leftVal:
                leftMax = max(leftMax, leftRes[i])
        
        leftRes[left] = leftMax + 1

    for right in range(n-1,-1,-1):
        rightVal = nums[right]
        rightMax = -1
        for j in range(n-1, right, -1):
            if nums[j] < rightVal:
                rightMax = max(rightMax, rightRes[j])
        
        rightRes[right] = rightMax + 1

    res = []
    for le, ri in zip(leftRes, rightRes):
        res.append(le+ri)
    
    return n - max(res) - 1

# result = []
for i in range(0, l, 2):
    n = int(lines[i])
    nums = lines[i+1]
    nums = [int(x) for x in nums.split(' ')]
    res = minOut(nums, n)
    print(res)



