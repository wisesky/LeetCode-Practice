class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def initListNodes(nums):
        root = ListNode(-1)
        last = root
        for num in nums:
            node = ListNode(num)
            last.next = node
            last = node
        return root

while True:
    try:
        n = int(input())
        nums = list(map(int, input().split() ))
        k = int(input())
        
        # trick
        # print(nums[-k])
        root = ListNode.initListNodes(nums)
        post = root
        for _ in range(k):
            if post != None:
                post = post.next
            else:
                print(None)

        if post == None:
            print(None)
        else:
            pre = root
            while post != None:
                pre = pre.next
                post = post.next
            # OJ 很坑
            #  代码是while 循环验证所有用例 所以不能轻易break
            if k == 0:
                print(0)
                # break
            else:
                print(pre.val)

    except:
        break