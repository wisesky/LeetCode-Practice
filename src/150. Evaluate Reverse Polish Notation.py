from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        length = len(tokens)
        if length == 0:
            return 0
        if length == 1:
            return tokens[0]
        operations = ['+','-','*', '/']
        nums = []
        for token in tokens:
            if token not in operations:
                nums.append(token)
            else:
                p2, p1 = nums.pop(), nums.pop()
                p = self.ops(token, int(p1), int(p2))
                nums.append(p)
        return int(nums[-1])


    def ops(self, operation, p1, p2):
        if operation == '/':
            return p1 / p2 if abs(p1) >= abs(p2) else 0
        return eval('p1'+operation+'p2')


tokens = ["2", "1", "+", "3", "*"]
tokens = ["4", "13", "5", "/", "+"]
# tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
tokens = ["-78","-33","196","+","-19","-","115","+","-","-99","/","-18","8","*","-86","-","-","16","/","26","-14","-","-","47","-","101","-","163","*","143","-","0","-","171","+","120","*","-60","+","156","/","173","/","-24","11","+","21","/","*","44","*","180","70","-40","-","*","86","132","-84","+","*","-","38","/","/","21","28","/","+","83","/","-31","156","-","+","28","/","95","-","120","+","8","*","90","-","-94","*","-73","/","-62","/","93","*","196","-","-59","+","187","-","143","/","-79","-89","+","-"]
so = Solution()
r =so.evalRPN(tokens)
print(r)