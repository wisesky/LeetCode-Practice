class Solution:
    def mySqrt(self, x: int) -> int:
        lo = 1
        hi = x
        while lo <= hi:
            mid = (lo+hi) // 2
            mid_sqrt = mid ** 2
            if mid_sqrt == x:
                return mid
            elif mid_sqrt > x:
                hi = mid - 1
            else:
                lo = mid + 1
        return lo - 1

        