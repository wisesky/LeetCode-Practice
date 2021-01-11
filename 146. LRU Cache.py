class ListNode:
    def __init__(self, x=None):
        self.val = x
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.key2prenode = {}
        self.node2key = {}
        self.root =  ListNode()
        self.tail = self.root
        self.size = 0
        self.capacity = capacity

    def pop(self):
        if self.size < 1:
            return
        cur = self.root.next
        post = cur.next
        self.root.next = post
        if cur in self.node2key:
            key = self.node2key[cur]
            self.key2prenode.pop(key)
            self.node2key.pop(cur)

        if post in self.node2key:
            post_key = self.node2key[post]
            self.key2prenode[post_key] = self.root

        return

    def append(self, key, value):
        node = ListNode(value)
        self.key2prenode[key] = self.tail
        self.node2key[node] = key
        self.tail.next = node
        self.tail = node
        return

    def getPreNode(self, key):
        if key in self.key2prenode:
            return self.key2prenode[key]
        return None
    
    def update(self, prenode):
        if prenode == None or prenode.next == None:
            return 
        cur = prenode.next
        post = cur.next
        if cur == self.tail:
            return

        tail_old = self.tail
        self.tail.next = cur
        cur.next = None
        self.tail = cur
        if cur in self.node2key:
            key = self.node2key[cur]
            self.key2prenode[key] = tail_old
        prenode.next = post
        if post in self.node2key:
            post_key = self.node2key[post]
            self.key2prenode[post_key] = prenode
        return

    def get(self, key: int) -> int:
        pre = self.getPreNode(key)
        if pre == None or pre.next == None:
            return -1
        else:
            val = pre.next.val
            self.update(pre)
            return val
        
    def put(self, key: int, value: int) -> None:
        pre = self.getPreNode(key)
        if pre == None or pre.next == None:
            if self.size == self.capacity:
                self.pop()
                self.append(key, value)
            else:
                self.append(key, value)
                self.size += 1
        else:
            pre.next.val = value
            self.update(pre)
            
        return

def printNode(root):
    print('*'*20)
    cur = root.next
    while cur != None:
        print(cur.val)
        cur = cur.next
    print('*'*20)
    return


capacity = 3
obj = LRUCache(capacity)
obj.put(1,1)
obj.put(2,2)
obj.put(3,3)
obj.put(4,4)
print(obj.get(4))
print(obj.get(3))
print(obj.get(2))
print(obj.get(1))
obj.put(5,5)
print(obj.get(1))
print(obj.get(2))
print(obj.get(3))
print(obj.get(4))
print(obj.get(5))
# Your LRUCache object will be instantiated and called as such:
# capacity = 2
# obj = LRUCache(capacity)
# obj.put(1,1)
# obj.put(2,2)
# print(obj.get(1))
# obj.put(3,3)
# print(obj.get(2))
# obj.put(4,4)
# print(obj.get(1))
# # print('-'*10)
# # printNode(obj.root)
# # print('-'*10)
# print(obj.get(3))
# # print('-'*10)
# # printNode(obj.root)
# # print('-'*10)
# print(obj.get(4))
# # # print(obj.get(3))
# # # print('-'*10)
# # # printNode(obj.root)
# # # print('-'*10)