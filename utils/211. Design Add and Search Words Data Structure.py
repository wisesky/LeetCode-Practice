class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # self.wordList = set()
        self.length2WordList = {}
        
    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        length = len(word)
        if length in self.length2WordList:
            self.length2WordList[length].add(word)
        else:
            tmp = set()
            tmp.add(word)
            self.length2WordList[length] = tmp
        return
        
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        length = len(word)
        set_length = self.length2WordList.get(length, set())
        for word1 in set_length:
            if self.match(word1, word):
                return True
            # else:
            #     continue
        return False

    def match(self, word1, word2):
        if len(word1) != len(word2):
            return False
        for c1, c2 in zip(word1, word2):
            if c1 == '.' or c2 == '.' or c1 == c2:
                continue
            else:
                return False
        return True


# Your WordDictionary object will be instantiated and called as such:
obj = WordDictionary()
word1 = 'abc'
word2 = 'cba'
obj.addWord(word1)
param_2 = obj.search(word2)
print(param_2)