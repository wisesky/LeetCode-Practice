#------------------------------------------------------------------------------------
# A generic stack, implemented using a singly list
#------------------------------------------------------------------------------------

class Stack:
    def __init__(self, items=[]) -> None:
        self.items = items
        # self.n = len(items)

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def isEmpty(self):
        return self.size() == 0
    
    def size(self):
        return len(self.items)

if __name__=="__main__":
    nums = list(range(10))
    stk = Stack(nums)
    while not stk.isEmpty():
        print(stk.pop())