from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        return self.searchHelper_1(nums, target)

    def searchHelper(self, nums: List[int], target: int) -> int:
        if len(nums) == 0 :
            return -1
        
        st =0
        ed = len(nums)-1
        # mid = (st+ed) // 2

        while st <= ed:
            mid = (st+ed) // 2
            # print(st, mid, ed)
            if nums[st] < target:
                if nums[mid] < nums[st]:
                    # st mid
                    ed = mid-1
                elif nums[mid] > nums[st]:                    
                    if nums[mid] < target:
                        #  mid ed
                        st = mid+1
                    elif nums[mid] > target:
                        # st mid
                        ed = mid-1
                    else:
                        return mid
                else: # mid == st
                    if nums[mid] == target:
                        return mid
                    elif nums[ed] == target:
                        return ed
                    else:
                        # return -1
                        st = mid+1
            elif nums[st] > target:
                if nums[mid] > nums[ed]:
                    # mid ed
                    st = mid+1
                elif nums[mid] < nums[ed]:
                    if nums[mid] > target:
                        # st mid
                        ed = mid-1
                    elif nums[mid] < target:
                        # mid ed
                        st = mid+1
                    else:
                        return mid
                else: # mid == ed
                    if nums[mid] == target:
                        return mid
                    if nums[st] == target:
                        return st
                    else:
                        # return -1
                        st = mid+1
            else: # st == target
                return st

        return -1

    def searchHelper_1(self, nums: List[int], target: int) -> int:
        if len(nums) == 0 :
            return False
        
        st =0
        ed = len(nums)-1
        while st <= ed:
            mid = (st+ed) // 2
            if nums[mid] == target :
                return True

            # left sorted
            if nums[st] < nums[mid]:
                if target >= nums[st] and target < nums[mid]:
                    ed = mid - 1
                else:
                    st = mid + 1
            elif nums[st] == nums[mid]:
                st += 1
            # right sorted
            else :# nums[mid] < nums[ed]
                if target > nums[mid] and target <= nums[ed]:
                    st = mid + 1
                else:
                    ed = mid - 1 
                    
        return False
        
if __name__ == "__main__":
    so = Solution()
    # nums = [4,5,6,7,0,1,2]
    # nums = [1]
    # nums = [8,9,2,3,4]
    # nums = [0,0,0,0,0,1,2,3]
    nums = [1,3,1,1,1]
    res = so.search(nums, 3)  
    print(res)
