class IndexMinPQ:
    """
    IndexMinPQ API came from algs4: priority queue -> IndexMinPQ
    """
    def __init__(self, d={}) -> None:
        """
        index is heap inner index  start from 1
            so father_index == son_index // 2
                left_son_index = father_index * 2
                right_son_index = left_son_index + 1
        a little similar sortedDict but sorted by value
        data relationship:
            index(heap) <==> key --> val
        
        """
        self.n = 0
        self.key2index = {}
        self.index2key = {}
        self.k2v = {}

        if len(d) > 0:
            for k,v in d.items():
                self.insert(k, v)

    def insert(self, key, val):
        """"
        insert k,v 
        if k in pq, then change k,v 
        """
        if self.contains(key):
            return self.change(key, val)
        self.k2v[key] = val
        # index start from 1
        self.n += 1
        self.index2key[self.n] = key
        self.key2index[key] = self.n
        self.swim(self.n)

    def change(self, key, val):
        assert self.contains(key), 'key not in pq'
        self.k2v[key] = val
        index = self.key2index[key]
        self.swim(index)
        self.sink(index)

    def contains(self, key):
        return key in self.k2v

    def delete(self, key):
        assert self.contains(key), 'key not in pq'
        index = self.key2index[key]
        self.exch(index, self.n)
        new_index = self.key2index[key]
        assert new_index == self.n, 'self.exch index and last index error'
        self.n -= 1
        self.key2index.pop(key)
        self.index2key.pop(new_index)
        self.k2v.pop(key)
        # swim and sink must after n -= 1
        self.swim(index)
        self.sink(index)

    def min(self):
        """
        return min val
        """
        min_index = 1
        min_key = self.index2key[min_index]
        return self.k2v[min_key]

    def minKey(self):
        """
        original minIndex in algs4(Java)
        but I think heap index <==> key --> val 
         will be more clear
        """
        min_index = 1
        return self.index2key[min_index]

    def delMin(self):
        assert not self.isEmpty(), 'pq empty'
        min_index = 1
        min_key = self.index2key[min_index]
        min_val = self.k2v[min_key]
        self.exch(min_index, self.n)
        new_min_index = self.key2index[min_key]
        assert new_min_index == self.n, 'self.exch error'
        self.n -= 1
        self.key2index.pop(min_key)
        self.index2key.pop(new_min_index)
        self.k2v.pop(min_key)
        self.sink(min_index)
        return min_val

    def isEmpty(self):
        return self.n == 0

    def size(self):
        return self.n

    def get(self, key):
        """
        keyOf in algs4(Java)
        """
        assert self.contains(key), 'key not in pq'
        return self.k2v[key]

    def decreaseVal(self, key, val):
        """
        decreaseKey in algs4(Java)
        decrease old_val in key with new_val
        """
        assert self.contains(key), 'key not in pq'
        assert self.k2v[key] >= val, 'decreaseVal but new val is greater'
        self.k2v[key] = val
        index = self.key2index[key]
        self.swim(index)

    def increaseVal(self, key, val):
        """
        increaseKey in algs4(Java)
        increase old_val in key with new_val
        """
        assert self.contains(key), 'key not in pq'
        assert self.k2v[key] <= val, 'increaseVal but new val is smaller'
        self.k2v[key] = val
        index = self.key2index[key]
        self.sink(index)

#------------------------------------------------
# index version prirority queue basic operation
    def swim(self, i):
        """
        i ==> index_i
        """
        # i // 2 > 0 <==> i > 1
        while i // 2 > 0 and  self.greater(i//2, i):
            self.exch(i, i//2)
            i = i // 2

    def sink(self, i):
        """
        i ==> index_i
        """
        while 2*i <= self.n :
            son = 2*i
            if son < self.n  and self.greater(son, son+1):
                son += 1
            if self.greater(son, i):
                break
            self.exch(i, son)
            i = son

    def greater(self, i, j):
        """
        i,j ==> index_i, index_j
        compare val[key_i] with val[key_j]
        """
        key_i = self.index2key[i]
        key_j = self.index2key[j]
        return self.k2v[key_i] > self.k2v[key_j]

    def exch(self, i,j ):
        """
        exchange index_i: vals with indedx_j: vals
        before 
            index_i -> key_i -> val_i
            index_j -> key_j -> val_j
        after
            index_i -> key_j -> val_j
            index_j -> key_i -> val_i
        """
        key_i = self.index2key[i]
        key_j = self.index2key[j]

        self.index2key[i] = key_j
        self.index2key[j] = key_i
        self.key2index[key_i] = j
        self.key2index[key_j] = i

d = {
    'v1': 3,
    'v2': 4,
    'v3' : 6,
    'v1': 7,
}
pq = IndexMinPQ(d)

pq.increaseVal('v2', 10)
pq.decreaseVal('v3', 5)

while not pq.isEmpty():
    # print(pq.delMin())
    min_key = pq.minKey()
    min_val = pq.min()
    min_val_1 = pq.get(min_key)
    assert min_val == min_val_1, 'min_val error'
    pq.delete(min_key)
    print(min_key, min_val)