from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        length = len(gas)
        if length == 0:
            return -1

        l = [0]*length
        for i in range(length):
            g = gas[i]
            c = cost[i]
            l[i] = g-c

        if sum(l) < 0 :
            return -1

        st = []
        for j in range(length):
            if l[j] >= 0 :
                st.append(j)
        
        for s in st:
            v = 0
            t = s
            for _ in range(length):
                v += l[t]
                t = (t+1) % length
                if v < 0:
                    break
            else:
                return s

        return -1

gas = [1,2,3,4,5]
cost = [3,4,5,1,2]
gas = [5,1,2,3,4]
cost = [4,4,1,5,1]
# gas = [2]
# cost = [2]

so = Solution()
idx = so.canCompleteCircuit(gas, cost)
print(idx)