from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 0:
            return 0
        lo = 0
        hi = len(height) - 1
        lh, rh  = height[lo], height[hi]

        res = 0
        while lo < hi:
            if lh <= rh:
                lo += 1
                while lo < hi :
                    left = height[lo]
                    if left <= lh:
                        res += lh - left
                        lo += 1
                    else:
                        lh = left
                        break

            else: # lh > rh
                hi -= 1
                while lo < hi :
                    right = height[hi]
                    if right < rh:    
                        res += rh - right
                        hi -= 1
                    else:
                        rh = right
                        break

        return res

if __name__ == "__main__":
    heights = [0,1,0,2,1,0,1,3,2,1,2,1]
    so = Solution()
    res = so.trap(heights)
    print(res)