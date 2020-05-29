from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0 :
            return -1
        
        st =0
        ed = len(nums)-1
        # mid = (st+ed) // 2

        while st <= ed:
            mid = (st+ed) // 2
            print(st, mid, ed)
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
                        return -1
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
                        return -1
            else: # st == target
                return st

        return -1

    def search_1(self, nums, target):
        if len(nums) == 0 :
            return -1
        
        st =0
        ed = len(nums)-1
        # mid = (st+ed) // 2

        while st <= ed:
            mid = (st+ed) // 2
            print(st, mid, ed)
            if nums[mid] < target:
                if nums[st] > target:
                    # mid ed
                    st = mid+1
                elif nums[st] < target:
                    # mid
            elif nums[mid] > target:
                # st mid
                ed = mid-1
            else:
                return mid

        return -1

if __name__ == "__main__":
    so = Solution()
    # nums = [4,5,6,7,0,1,2]
    # nums = [1]
    nums = [8,9,2,3,4]
    res = so.search_1(nums, 9)  
    print(res)
