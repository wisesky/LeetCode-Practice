#------------------------------------------------------------------
# python Bag.py < tobe.txt
# 
# A generic bag or multiset, implemented using a singly linked list.
#------------------------------------------------------------------

class Node:
    def __init__(self, item=None) -> None:
        self.item = item
        self.next = None

class Bag:
    def __init__(self, items=[]) -> None:
        self.head = Node()
        self.n = 0
        for item in items:
            self.add(item)

    def add(self, item):
        newNode = Node(item)
        newNode.next = self.head.next
        self.head.next = newNode
        self.n += 1

    def isEmpty(self):
        return self.n==0

    def size(self):
        return self.n

    # solution1:  generator 
    def __iter__(self):
        crt = self.head
        while crt.next!=None:
            yield crt.next.item
            crt = crt.next
    # solution2: new iteratorBag 
    def __iter__(self):
        return IteratorBag(self)

class IteratorBag:
    def __init__(self, bagInst):
        self.crt = bagInst.head
        self.n = bagInst.n
    def __iter__(self):
        return self
    def __next__(self):
        self.crt = self.crt.next
        if self.crt != None:
            return self.crt.item
        else:
            raise StopIteration


if __name__=="__main__":
    nums = list(range(10))

    bag = Bag(nums)

    for b in bag:
        print(b)

    it1 = iter(bag)
    it2 = iter(bag)
    print(next(it1))
    print(next(it2))
    print(next(it1))
    print(next(it2))
