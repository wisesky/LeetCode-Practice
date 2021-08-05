#
# @lc app=leetcode id=223 lang=python3
#
# [223] Rectangle Area
#
# https://leetcode.com/problems/rectangle-area/description/
#
# algorithms
# Medium (38.63%)
# Likes:    575
# Dislikes: 896
# Total Accepted:    122.1K
# Total Submissions: 315.2K
# Testcase Example:  '-3\n0\n3\n4\n0\n-1\n9\n2'
#
# Given the coordinates of two rectilinear rectangles in a 2D plane, return the
# total area covered by the two rectangles.
# 
# The first rectangle is defined by its bottom-left corner (ax1, ay1) and its
# top-right corner (ax2, ay2).
# 
# The second rectangle is defined by its bottom-left corner (bx1, by1) and its
# top-right corner (bx2, by2).
# 
# 
# Example 1:
# 
# 
# Input: ax1 = -3, ay1 = 0, ax2 = 3, ay2 = 4, bx1 = 0, by1 = -1, bx2 = 9, by2 =
# 2
# Output: 45
# 
# 
# Example 2:
# 
# 
# Input: ax1 = -2, ay1 = -2, ax2 = 2, ay2 = 2, bx1 = -2, by1 = -2, bx2 = 2, by2
# = 2
# Output: 16
# 
# 
# 
# Constraints:
# 
# 
# -10^4 <= ax1, ay1, ax2, ay2, bx1, by1, bx2, by2 <= 10^4
# 
# 
#

# @lc code=start
class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        area_a = (ax2-ax1)*(ay2-ay1)
        area_b = (bx2-bx1)*(by2-by1)
        c1 = self.commonLength(ax1, ax2, bx1, bx2)
        c2 = self.commonLength(ay1, ay2, by1, by2)
        area_com = c1 * c2
        return area_a+area_b - area_com

    def commonLength(self, ax1, ax2, bx1, bx2):
        if ax1 > bx1:
            ax1, ax2, bx1, bx2 = bx1, bx2, ax1, ax2
        if ax2 >= bx1:
            return min(ax2, bx2) - bx1
        return 0
# @lc code=end
if __name__ == "__main__":
    so = Solution()
    # ax1,ay1,ax2,ay2=-3,0, 3, 4
    # bx1,by1,bx2,by2 = 0,-1, 9,2
    ax1 = -2
    ay1 = -2
    ax2 = 2
    ay2 = 2
    bx1 = -2
    by1 = -2
    bx2 = 2
    by2 = 2
    r = so.computeArea(ax1,ay1,ax2,ay2,
                        bx1,by1,bx2,by2
                        )
    print(so.commonLength(-1,1,0,0))                        
