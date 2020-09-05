from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        addIntervals = []
        # for newItv in newInterval:
        rItv = self.constructInterval(intervals, newInterval)

        resIntervals = []
        for i, itv in enumerate(intervals):
            rg = range(rItv[0], rItv[1]+1)
            if itv[0] not in rg or rItv[1] not in rg:
                resIntervals.append(itv)
        resIntervals.append(rItv)
        resIntervals.sort()
        return resIntervals

    def constructInterval(self,intervals, newItv):
        st, ed = newItv
        newSt, newEd = st, ed
        for interval in intervals:
            if st in range(interval[0], interval[1]+1):
                newSt = interval[0]
            if ed in range(interval[0], interval[1]+1):
                newEd = interval[1]
        return [newSt, newEd]

    def binSearch(self, nums, num):
        lo = 0
        hi = len(nums) - 1
        while lo < hi:
            mid = (lo+hi) // 2
            cand = nums[mid]
            if cand > num:
                hi = mid - 1
            elif cand < num:
                lo = mid + 1
            else:
                return mid
        return lo

if __name__ == "__main__":
    so = Solution()
    intervals = [[1,3],[6,9]]
    newInterval = [2,5]
    intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
    newInterval = [4,8]
    resIntervals = so.insert(intervals, newInterval)
    print(resIntervals)