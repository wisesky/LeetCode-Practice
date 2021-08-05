#
# @lc app=leetcode id=210 lang=python3
#
# [210] Course Schedule II
#
# https://leetcode.com/problems/course-schedule-ii/description/
#
# algorithms
# Medium (43.58%)
# Likes:    4035
# Dislikes: 174
# Total Accepted:    418.7K
# Total Submissions: 959.6K
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
# Return the ordering of courses you should take to finish all courses. If
# there are many valid answers, return any of them. If it is impossible to
# finish all courses, return an empty array.
# 
# 
# Example 1:
# 
# 
# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: [0,1]
# Explanation: There are a total of 2 courses to take. To take course 1 you
# should have finished course 0. So the correct course order is [0,1].
# 
# 
# Example 2:
# 
# 
# Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
# Output: [0,2,1,3]
# Explanation: There are a total of 4 courses to take. To take course 3 you
# should have finished both courses 1 and 2. Both courses 1 and 2 should be
# taken after you finished course 0.
# So one correct course order is [0,1,2,3]. Another correct ordering is
# [0,2,1,3].
# 
# 
# Example 3:
# 
# 
# Input: numCourses = 1, prerequisites = []
# Output: [0]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= numCourses <= 2000
# 0 <= prerequisites.length <= numCourses * (numCourses - 1)
# prerequisites[i].length == 2
# 0 <= ai, bi < numCourses
# ai != bi
# All the pairs [ai, bi] are distinct.
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        s2t = {}
        t2s = {}
        marked = {}
        # inStack = {}
        res = {}
        for t,s in prerequisites:
            if s in s2t:
                s2t[s].append(t)
            else:
                s2t[s] = [t]
            if t in t2s:
                t2s[t].append(t)
            else:
                t2s[t] = [s]

        starts = []
        for i in range(numCourses):
            if i not in marked:
                res = self.dfs(i, t2s, marked)
                starts.extend(res)
                
        # result = []
        # for start in starts:
        #     res = self.bfs(start, s2t)
        #     result.extend(res)
        # return result
        # return self.bfs(starts, s2t)
        cur = starts
        # post = []
        result = []
        while len(cur) > 0:
            res = []
            for c in cur:
                res.extend(s2t.get(c, []))

            for r in res:
                if r in cur:
                    cur.remove(r) 
            result.extend(cur)
        
            cur = list(set(res))
            # post = []
        return result
    # BFS
    def bfs(self, starts, s2t):
        # q = [start]
        q = starts.copy()
        res = starts
        while len(q) > 0:
            course = q.pop(0)
            nextCourses = s2t.get(course, [])
            
            for nextCourse in nextCourses:
                if nextCourse in q:
                    q.remove(nextCourse)   
                q.append(nextCourse)

                if nextCourse not in res:
                    res.append(nextCourse)
        return res

    def dfs(self, course, s2t, marked):
        marked[course] = True
        preCourses = s2t.get(course, [])
        if len(preCourses) == 0:
            return [course]
        
        r = []
        for preCourse in preCourses:
            if preCourse not in marked:
                tmp = self.dfs(preCourse, s2t, marked)
                r.extend(tmp)

        return  list(set(r))
# @lc code=end

if __name__ == "__main__":
    num = 2
    pre = [[1,0]]
    # pre = [[0,1]]
    num = 4
    pre = [[1,0],[2,0],[3,1],[3,2]]
    num = 3
    # pre = [[2,0],[2,1]]
    # pre = [[0,1],[0,2],[1,2]]
    pre = [[1,0],[1,2],[0,1]]
    so = Solution()
    r = so.findOrder(num, pre)
    print(r)
