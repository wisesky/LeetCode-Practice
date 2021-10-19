from typing import List
import heapq
import string
from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        q = deque()
        q.append((1,beginWord))
        wordList_set = set(wordList) - set([beginWord])
        if endWord not in wordList_set:
            return 0
        # visited = {}

        while len(q)>0:
            step, word = q.popleft()
            # visited[word] = True
            
            if word == endWord:
                return step

            for i in range(len(word)):
                for char in string.ascii_lowercase:
                    tmp = word[ :i] + char + word[i+1: ]
                    if tmp in wordList_set:
                        q.append((step+1,tmp))
                        wordList_set -= set([tmp])
        return 0

beginWord = 'hot'
endWord = 'dog'
wordList = ["hot","dog"]

so = Solution()
r = so.ladderLength(beginWord, endWord, wordList)
print(r)