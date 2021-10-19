

def longestPermut(nums, n, st=1):

    dl = {}
    for num in nums:
        dl[num] = dl.get(num, 0) + 1

    length = 0
    for i in range(st, n+1):
        if dl.get(i) == None:
            break
        
        length += 1

    return length

n = int(input())
nums = list(map(int, input().split()))

length = longestPermut(nums,n)
print(length)