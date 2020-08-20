while True:
    try:
        n, k = list(map(int, input().split()))
        nums = list(map(int, input().split()))
        nums = sorted(nums)
        print(' '.join([str(x) for x in nums[ :k]]))


    except :
        break