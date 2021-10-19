from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        length = len(digits)
        last = digits[-1]
        plus, digits[-1] = divmod(last + 1, 10)

        for i in reversed(range(length-1)):
            if plus > 0:
                plus, digits[i] = divmod(digits[i]+plus, 10)
            else:
                break
        else:
            if plus > 0:
                digits.insert(0,plus)

        return digits

if __name__ == "__main__":
    so = Solution()
    digits = [9,9,9,9]
    # digits = [4,3,2,1]
    # digits = [0]
    res = so.plusOne(digits)
    print(res)
        

