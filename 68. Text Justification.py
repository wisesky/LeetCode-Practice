from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        candidateWords = []
        wordslength = 0
        for i, word in enumerate(words):
            l = len(word)
            maybyLength = wordslength + l + 1 if len(candidateWords) > 0 else l
            if maybyLength > maxWidth:
                r = self.constructSpace(candidateWords, maxWidth)
                res.append(r)
                candidateWords = [word]
                wordslength = l
            else:
                wordslength = maybyLength
                candidateWords.append(word)
    
        if len(candidateWords) > 0:
            spaceLength = maxWidth - wordslength
            extra = ' ' * spaceLength
            r = ' '.join(candidateWords) + extra
            res.append(r)
        return res

    def constructSpace(self, words, maxWidth):
        length = len(words)
        spaceLength = maxWidth - len(''.join(words)) 
        if length == 1:
            return ''.join(words) + ' '*spaceLength
        evenSapce,extraSpace = divmod(spaceLength, length-1)

        even = ' '*evenSapce
        extra = ' '*(evenSapce+1)
        r = ''
        for i, word in enumerate(words):
            if i == length - 1:
                r += word
            else:
                if extraSpace > 0:
                    r = r + word + extra
                    extraSpace -= 1
                else:
                    r = r + word + even
        return r

if __name__ == "__main__":
    so = Solution()
    words = ["This", "is", "an", "example", "of", "text", "justification."]
    words = ["What","must","be","acknowledgment","shall","be"]
    maxWidth = 16
    
    words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]  
    maxWidth = 20

    words = ["Listen","to","many,","speak","to","a","few."]
    maxWidth = 6
    res = so.fullJustify(words, maxWidth)
    print(res)
