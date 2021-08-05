#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#
# https://leetcode.com/problems/course-schedule/description/
#
# algorithms
# Medium (44.45%)
# Likes:    6196
# Dislikes: 262
# Total Accepted:    612.1K
# Total Submissions: 1.4M
# Testcase Example:  '2\n[[1,0]]'
#
# There are a total of numCourses courses you have to take, labeled from 0 to
# numCourses - 1. You are given an array prerequisites where prerequisites[i] =
# [ai, bi] indicates that you must take course bi first if you want to take
# course ai.
# 
# 
# For example, the pair [0, 1], indicates that to take course 0 you have to
# first take course 1.
# 
# 
# Return true if you can finish all courses. Otherwise, return false.
# 
# 
# Example 1:
# 
# 
# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0. So it is possible.
# 
# 
# Example 2:
# 
# 
# Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0, and to take course 0 you
# should also have finished course 1. So it is impossible.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= numCourses <= 10^5
# 0 <= prerequisites.length <= 5000
# prerequisites[i].length == 2
# 0 <= ai, bi < numCourses
# All the pairs prerequisites[i] are unique.
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    # 无向图 的环检测
    # 需要注意 除了 marked 来进行遍历判断之外，还需要 inStack 来判断DFS时的环判断
    # 许久没有 做图相关的 算法， 写DFS的时候， marked inStack 的逻辑意义
    # 混淆了， 结果 inStack marked 应该在何处修改值 发生了混乱，调试了很久才发现， marked inStack 的位置搞反了
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if numCourses < 2:
            return True
        t2s = {}
        marked = {}
        inStack = {}
        for t,s in prerequisites:
            if t in t2s:
                t2s[t].append(s)
            else:
                t2s[t] = [s]

        for i in range(numCourses):
            if not marked.get(i, False) :
                if self.cycleCheck(i, t2s, marked, inStack):
                    return False
        else:
            return True
    # dfs check cycle
    def cycleCheck(self, course, t2s,marked,inStack):
        marked[course] = True
        nextCourses = t2s.get(course, [])
        if len(nextCourses) == 0 :
            return False
        
        totalCycle = False
        inStack[course] = True
        for nextCourse in nextCourses:
            # 先判断DFS inStack ，然后判断 marked 
            # marked 一定是 dfs inStack 的超集
            if inStack.get(nextCourse, False):
                return True
            # marked 判断， 已经dfs 遍历过的，不需要重复遍历
            if nextCourse in marked:
                continue
            
            isCycle = self.cycleCheck(nextCourse, t2s, marked, inStack)
            totalCycle = totalCycle or isCycle
        inStack[course] = False
        return totalCycle
        

# @lc code=end
if __name__ == "__main__":
    numsCourses = 2
    pre = [[1,0]] # True
    # pre = [[1,0],[0,1]] # False
    # False
    # numsCourses = 20
    # pre = [[0,10],[3,18],[5,5],[6,11],[11,14],[13,1],[15,1],[17,4]]
    # False
    numsCourses = 3
    pre = [[1,0],[1,2],[0,1]]
    so = Solution()
    r = so.canFinish(numsCourses, pre)
    print(r)
