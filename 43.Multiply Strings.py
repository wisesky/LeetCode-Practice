class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        l1 = len(num1)
        l2 = len(num2)

        if l1 >= l2:
            first = num1
            second = num2
        else:
            first = num2
            second = num1
            l1 = len(first)
            l2 = len(second)
        
        res = 0
        for i in range(l2-1, -1, -1):
            x = int(second[i])
            alpha = 10**(l2-i-1)

            r = 0 
            for j in range(l1-1, -1, -1):
                y = int(first[j])
                beta = 10**(l1-j-1)
                r += y * x * beta

            res += r * alpha

        return str(res)

if __name__ == "__main__":
    so = Solution()
    num1 = '123'
    num2 = '456'
    num2 = '0'
    res = so.multiply(num1, num2)
    print(res)
                