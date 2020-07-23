from typing import List
import heapq

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        
        if len(heightMap) == 0:
            return 0
        
        h = len(heightMap)
        w = len(heightMap[0])
        
        visited = {}
        pq = []
        
        for i in range(h):
            heapq.heappush(pq, (heightMap[i][0], (i, 0)))
            heapq.heappush(pq, (heightMap[i][w-1], (i, w-1)))
            visited[i, 0] = True
            visited[i, w-1] = True

        for j in range(1,w-1):
            heapq.heappush(pq, (heightMap[0][j], (0,j)))
            heapq.heappush(pq, (heightMap[h-1][j], (h-1,j)))
            visited[0, j] = True
            visited[h-1, j] = True

        h_max = 0
        res = 0
        while len(pq) > 0:
            value , (x, y) = heapq.heappop(pq)
            if value < h_max:
                res += h_max - value
            else:
                h_max = value

            up = (x-1, y) if x > 0 else None
            down = (x+1, y) if x < h-1 else None
            left = (x, y-1) if y > 0 else None
            right = (x, y+1) if y < w-1 else None

            if up != None and not visited.get(up, False):
                heapq.heappush(pq, (heightMap[up[0]][up[1]], up))
                visited[up] = True
            if down!= None and not visited.get(down, False):
                heapq.heappush(pq, (heightMap[down[0]][down[1]], down))
                visited[down] = True
            if left != None and not visited.get(left, False):
                heapq.heappush(pq, (heightMap[left[0]][left[1]], left))
                visited[left] = True
            if right != None and not visited.get(right, False):
                heapq.heappush(pq, (heightMap[right[0]][right[1]], right))
                visited[right] = True

        return res

if __name__ == "__main__":
    so = Solution()
    heightMap = [
  [1,4,3,1,3,2],
  [3,2,1,3,2,4],
  [2,3,3,2,3,1]
]
    # 14
    heightMap = [
        [12,13,1,12],
        [13,4,13,12],
        [13,8,10,12],
        [12,13,12,12],
        [13,13,13,13]
        ]
    # 3 
    heightMap = [
        [5,5,5,1],
        [5,1,1,5],
        [5,1,5,5],
        [5,2,5,8]
        ]

    # 44
    heightMap = [
        [78,16,94,36],
        [87,93,50,22],
        [63,28,91,60],
        [64,27,41,27],
        [73,37,12,69],
        [68,30,83,31],
        [63,24,68,36]
        ]

    # 25 
    heightMap = [
        [14,17,18,16,14,16],
        [17,3,10,2,3,8],
        [11,10,4,7,1,7],
        [13,7,2,9,8,10],
        [13,1,3,4,8,6],
        [20,3,3,9,10,8]
        ]

    # 11
    # heightMap = [
    #     [14,20,11,19,19,16],
    #     [11,10,7,4,9,6],
    #     [17,2,2,6,10,9],
    #     [15,9,2,1,4,1],
    #     [15,5,5,5,8,7],
    #     [14,2,8,6,10,7]
    #     ]

    result = so.trapRainWater(heightMap)
    print(result)


            