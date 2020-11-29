from typing import List
from collections import deque

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        l = len(arr)
        dests = {} # 如果 起点i 可以到达 终点j : dests[j] = i
        ends = []
        for i,v in enumerate(arr):
            # dest = [i+x for x in [v,-v] if i+x in range(l)]
            dest = [i+v, i-v]
            dest = [x for x in dest if x in range(l)]
            for des in dest:
                if des in dests:
                    dests[des].append(i)
                else:
                    dests[des] = [i]
                
            if v == 0:
                ends.append(i)

        res = []
        for end in ends:
            r = self.endCanReach(arr, end, dests)
            # res.update(r)
            res.extend(r)

        return start in res
        

    def endCanReach(self, arr, end, dests):
        visited = {}
        queue = deque()
        queue.append(end)

        while len(queue) > 0:
            st = queue.popleft()
            visited[st] = True
            dest = dests.get(st, [])
            # checkedDest = [x for x in dest if visited.get(x, False) == True]
            for des in dest:
                if visited.get(des, False) != True:
                    queue.append(des)

        return list(visited.keys())


if __name__ == "__main__":
    so = Solution()
    arr = [4,2,3,0,3,1,2]
    start = 6
    arr = [3,0,2,1,2]
    start = 2
    canReach = so.canReach(arr, start)
    print('Rechable : ' , canReach)
