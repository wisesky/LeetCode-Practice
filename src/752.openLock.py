#! python3
# -*- encoding: utf-8 -*-
'''
@File   : 752.openLock.py
@Time   : 2023/12/08 09:52:30
@Author : Franklin Chen
@Contact: wisesky1988@gmail.com
@Licence: MIT License
@Desc   : 
'''
import string
class Solution:
    # BFS， 最短路径一般都是BFS
    # 遍历最短路径，要素： queue, visited, 路径长度 count
    # crt 的某一位，有plus 和 minus ，两个方向，如果是四位 ‘0000’ 那么就有8种可能， 相当于图中有8个邻接点
    # 8种可能要排除不合法的 剪枝路径 和 已经找到target的 终止路径
    # 不要忘记处理 visited，不走回头路，否则会陷入死循环
    def openLock(self,deadends, target):
        self.deadends = deadends
        start = '0000'
        # if start in deadends:
        #     return -1
        q = [start]
        visited = set(start)
        flipCounts = 0

        # BFS 循环终止条件是 Queue 不为空
        while len(q) > 0 :
            length = len(q)
            # 每一轮循环 取出当前层step 的所有节点
            for _ in range(length):
                crt = q.pop(0)
                # 类似DFS ， 一开始就要剪枝 和 写出终止条件
                if crt in self.deadends:
                    continue
                if crt == target:
                    return flipCounts
                # 一般情况，取出邻接点，加入 Queue 和 visited
                for adj in  self.adjs(crt, target):
                    if adj not in visited:
                        q.append(adj)
                        visited.add(adj)
            # 不要忘记一轮循环完毕，下一轮就是下一层计数了
            flipCounts += 1
        # 如果Queue 为空，那么就表示遍历了所有组合，仍然没有找到的话，就是无法找到合法路径
        return -1

    def adjs(self,crt, target):
        # 搜索crt的邻接点，终止条件不应该放到这里，应该在BFS队列取出的时候处理
        # if crt == target:
        #     return []
        adjs = []
        for i, (c, t )in enumerate(zip(crt, target)):
            # 原本的设想是，按照优先顺序，选择最接近的方向去靠近target
            # 但是 过早的选择优化剪枝，破坏了自顶向下的思维方式，导致底层的优化和上层设计 混杂在一起，导致逻辑bug
            # 实际上，这里依照遍历的设计，应该选择所有方向去靠近target， 如果因为crt某一位 与 target对应位相同，而不去变动这一位
            # 会导致因为deadend的阻拦，错过稍微绕路，但是仍然能靠近target的可能的最短路径
            # 所以 顶层设计的逻辑完备性（遍历所有路径） 大于 早起的剪枝优化， 剪枝过程放到后面
            # if c == t:
            #     continue
            pre = self.nextString(crt, i, itv=-1)
            post = self.nextString(crt, i, itv=1)
            adjs.append(pre)
            adjs.append(post)                
        
        return adjs
    
    # crt[pos] 向前 和 向后的 方法 ， 注意0-9 是循环的，边界问题要处理
    def nextString(self, crt, pos, itv=1):
        newChr = chr(ord(crt[pos]) + itv)
        if newChr == ":" :
            newChr = '0'
        elif newChr == '/':
            newChr = '9'
        newStr = list(crt)
        newStr[pos] = newChr
        return ''.join(newStr)


if __name__=="__main__":
    so = Solution()
    # count = so.openLock(['8888'], taxrget='0009')
    # count = so.openLock(["0201","0101","0102","1212","2002"], target='0202')
    # count = so.openLock(["8887","8889","8878","8898","8788","8988","7888","9888"], target='8888')
    count = so.openLock(['0000'], target='8888')
    print(count)