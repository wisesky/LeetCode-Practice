import re
from collections import deque
class Solution:
    def calculate(self, s: str) -> int:
        """
        字符处理有点事生疏， sub 空格 \s, split 数字和字符 \d+
        re.split 会产生空字符

        总体思路是， 分离 数字 和 操作符， 同时观察操作符为 * / 的时候，就地计算并保存
        最后再计算剩下的 + - 
        大体上是模仿， 堆栈法 来计算，但是仍有 东施效颦 之嫌， 
        一方面 堆栈法只记得概要，
        其次，精髓部分仍然没能掌握
        经典算法，务必多温习
        """
        ops = deque()
        nums = deque()
        s = re.sub('\s+', '', s)
        for c in re.split('(\d+)', s):
            if c in ['+','-','*','/']:
                ops.append(c)
            elif c == '':
                continue
            else  :
                num = int(c)
                if len(ops)>0 and ops[-1] == '*':
                    ops.pop()
                    nums[-1] = nums[-1] * num
                elif len(ops)>0 and ops[-1] == '/':
                    ops.pop()
                    nums[-1] = nums[-1] // num
                else:
                    nums.append(num)
                    
        while len(ops) != 0:
            num = nums.popleft()
            op = ops.popleft()
            if op == '+':
                nums[0] = nums[0] + num
            else:
                nums[0] = num - nums[0]
        return nums[0]

if __name__ == "__main__":
    so = Solution()
    s = '3+ 42 * 2 '
    # s = ' 3/2 '
    # s ='1-1+1'
    # s = '1+1-1'
    s = "0-2147483647"
    r = so.calculate(s)
    print(r)