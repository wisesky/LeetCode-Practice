from typing import List

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if len(heightMap) == 0:
            return 0
        
        h = len(heightMap)
        w = len(heightMap[0])
        
        dh = {}
        for i in range(h):
            nums = heightMap[i]
            res = self.cal2dRes(nums)
            dh[i] = res

        dw = {}
        for j in range(w):
            nums = [heightMap[k][j] for k in range(h)]
            res = self.cal2dRes(nums)
            dw[j] = res

        result = {}
        back = {}
        count = 0
        for i in range(h):
            for j in range(w):
                dhv = dh[i][j]
                dwv = dw[j][i]
                if  dhv != 0  and dwv != 0 :
                    result[i, j] = min(dhv, dwv)

                    # back tracking
                    upidx = i - 1 
                    leftidx = j - 1
                    if back.get((upidx, j)) != None:
                        uphead = back[upidx, j]
                        back[i,j] = uphead
                        if back.get((i, leftidx)) != None:
                            lefthead = back.get((i, leftidx))
                            for k,v in back.items():
                                if v == lefthead:
                                    back[k] = uphead

                    elif back.get((i, leftidx)) != None:
                        back[i,j] = back[i, leftidx]
                    else:
                        back[i,j] = count
                        count += 1

        for k,v in dh.items():
            print(k, v)
        print('-' * 50)
        for k,v in dw.items():
            print(k, v)
        for i in range(h):
            t = []
            for j in range(w):
                t.append(result.get((i,j), 0))
            print(t)

        head2idx = {}
        head2Wall = {}
        for idx, head in back.items():
            tmp1 = head2idx.get(head, [])
            tmp1.append(idx)
            head2idx[head] = tmp1

            m, n = idx
            tmp2 = head2Wall.get(head, [])
            up,down, left, right = (m-1,n), (m+1,n), (m, n-1), (m,n+1)
            if up not in back.keys():
                tmp2.append(up)
            if down not in back.keys():
                tmp2.append(down)
            if left not in back.keys():
                tmp2.append(left)
            if right not in back.keys():
                tmp2.append(right)    

            head2Wall[head] = tmp2
        
        head2min = {head:[heightMap[w[0]][w[1]] for w in wall] for head, wall in head2Wall.items()}
        head2min = {head:min(vl) for head, vl in head2min.items()}

        final = 0
        for head, idx in head2idx.items():
            for x in idx:
                i,j = x
                if head2min[head] - heightMap[i][j] > 0:
                    final += head2min[head] - heightMap[i][j]
                elif head2min[head] - heightMap[i][j] <= 0:
                    
            
        
        return final

    def cal2dRes(self, nums):
        if len(nums) == 0:
            return 0
        lo = 0
        hi = len(nums) - 1
        lh, rh  = nums[lo], nums[hi]

        res = {}
        res[lo] = 0
        res[hi] = 0
        while lo < hi:
            if lh <= rh:
                lo += 1
                while lo < hi :
                    left = nums[lo]
                    if left < lh:
                        # res += lh - left
                        # res[lo] = lh - left
                        res[lo] = lh
                        lo += 1
                    else:
                        res[lo] = 0
                        lh = left
                        break

            else: # lh > rh
                hi -= 1
                while lo < hi :
                    right = nums[hi]
                    if right < rh:    
                        # res += rh - right
                        # res[hi] = rh - right
                        res[hi] = rh
                        hi -= 1
                    else:
                        res[hi] = 0
                        rh = right
                        break

        
        result = [res.get(i, 0) for i in range(len(nums))]
        return result

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
    # heightMap = [
    #     [5,5,5,1],
    #     [5,1,1,5],
    #     [5,1,5,5],
    #     [5,2,5,8]
    #     ]

    # 44
    # heightMap = [
    #     [78,16,94,36],
    #     [87,93,50,22],
    #     [63,28,91,60],
    #     [64,27,41,27],
    #     [73,37,12,69],
    #     [68,30,83,31],
    #     [63,24,68,36]
    #     ]

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
    heightMap = [
        [14,20,11,19,19,16],
        [11,10,7,4,9,6],
        [17,2,2,6,10,9],
        [15,9,2,1,4,1],
        [15,5,5,5,8,7],
        [14,2,8,6,10,7]
        ]

    result = so.trapRainWater(heightMap)
    print(result)
