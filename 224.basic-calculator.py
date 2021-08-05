# @lc app=leetcode id=224 lang=python3

import re
# @lc code=start
class Solution:
    def calculate(self, s: str) -> int:
        """
        模仿 Dijkstra’s Two-Stack Algorithm，但是需要根据题目做适配，
        原算法 是针对 (2+(3*4)) 这种始终有括号表示优先级，且只有2个数之间的运算
        如果是多个数的连续运算，那么就需要做一定的修改

        关于无括号表示优先级的问题，在 227 Basic Calculator II 中已做解答
        此处应该是是需要识别括号的优先级 和 多个数之间的 + — 运算

        大体思路是，分离 运算符 和 运算数 ， 用list 来表示被（） 包围的连续+—运算，
        当遍历到 反括号） 的时候， 直接将括号内的数做求和运算，求和结果添加到，上一个括号的最后一位
        实践证明这个方法是可行的，只是对于 -(1+2) 这种括号前已经有符号的时候，需要额外一位来记录这个符号
        那就是表示括号的list的第一位，若括号前是+， 初始化为[1],若括号前是-，初始化为[-1]
        遇到反括号）需要求和结果时候，list[0] * sum(list[1: ]) 则为求和结果
        """
        s = re.sub('\s+', '', s)
        s = re.split('([\(\)+-])', s)
        s = [x for x in s if len(x)!=0]

        nums = [[]]
        positive = True
        for e in s:  
            if e == '(':
                # nums.append([])
                # 正括号（  前的 正负直接影响括号内的求和结果
                if positive:
                    nums.append([1])
                else:
                    nums.append([-1])
                positive = True
            elif e == ')':
                last = nums.pop()
                val = last[0] * sum(last[1: ])
                nums[-1].append(val)
            elif e == '+':
                pass
            elif e == '-':
                positive = not positive
            else:
                num = int(e)
                # 数字前的 正负号，只影响当前 数的值，且减号当作负数加入列表的时候，需要及时修正为+
                if positive:
                    nums[-1].append(num)
                else:
                    nums[-1].append(-num)
                    positive = True

        return sum(nums[0])
# @lc code=end

if __name__=='__main__':
    so = Solution()
    s = '1+2'
    # s = " 2-1 + 2 "
    # s = "+48 + -48"
    # s = "(1+(4+5+2)-3)+(6+8)"
    s = "- (3 + (4 + 5))"
    r = so.calculate(s)
    print(r)