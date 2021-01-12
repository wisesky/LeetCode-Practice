from typing import List

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) == 0:
            return 0
        if len(points) == 1:
            return 1
        d = {}
        c1 = float('-inf')
        for i in range(len(points)-1):
            p1 = points[i]
            d[p1[0],p1[1]] = d.get((p1[0],p1[1]), 0) + 1
            for j in range(i+1, len(points)):
                p2 = points[j]
                # d[p2[0],p2[1]] = d.get((p2[0],p2[1]), 0) + 1
                c1 = max(c1, self.online(p1, p2, points))
        d[points[-1][0],points[-1][1]] = d.get((points[-1][0],points[-1][1]), 0) + 1
        c2 = max(d.values())
        return max(c1, c2)

    def online(self, p1, p2, points):
        if p1 == p2 :
            return 2
        x1,y1 = p1
        x2,y2 = p2
        count = 0
        for p in points:
            # if p == p1 or p == p2:
            #     continue
            x3, y3 = p
            if (x1-x2)*(y1-y3) == (x1-x3)*(y1-y2):
                count += 1
        return count

points = [[1,1],[2,2],[3,3]]
# points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
# points = [[1,1],[1,1],[0,0],[3,4],[4,5],[5,6],[7,8],[8,9]]
points = [[1,1],[1,1],[1,1]]

so = Solution()
r = so.maxPoints(points)
print(r)