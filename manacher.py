# import numpy as np
class Solution:

    def calMaxsubseq(self,ss, ind,start=0, pos):

        for i in range(start, ind):
            itv = i + 1
            low = ind - itv
            high = ind + itv

            if high >= len(ss) or low < 0 :
                break
            
            if ss[low] == ss[high]:
                #if not pos.get(high, 'False'):
                pos[high] = i
                continue
            else:
                break
        if ss[low] == ss[high]:
            return high
        return high - 1

            

    def manacher(self , s):
        ss = '#' + '#'.join(s) + '#'
        rl = {}
        pos = 0
        maxRight = 0
        maxLen = 0

        for i, x in enumerate(ss):
            if i < maxRight:
                j = 2*pos - i
                rightEgde = maxRight - i
                
                r = min(rl[j], rightEgde)
                 
            else:
                r = 1

            # update maxright & pos with mid center:i
            while i-r>=0 and i+r<len(ss) and s[i-r]==s[i+r]:
                r += 1
                # update
                if r+i-1>maxRight:
                    maxRight = r+i-1
                    pos=i

            rl[i] = r
            maxLen = max(maxLen, r)
        return maxLen - 1
