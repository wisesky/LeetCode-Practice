def biSearch(l, n):
    lo = 0
    hi = len(l)-1
    while lo <= hi :  
        mid = math.ceil((lo + hi)/2)
        if mid >= len(l):
            return len(l)
        if l[mid] > n:
            #return biSearch(l[lo:mi-1], n)
            hi = mid -  1
        elif l[mid] < n:
            #return biSearch(l[mi+1:hi], n)
            lo = mid + 1
        else:
            return mid
    # 这里犯错了，在lo 》 hi的情况下跳出循环，但是mid并没有更新，所以要重新计算mid再return
    return math.ceil((lo + hi) / 2)
