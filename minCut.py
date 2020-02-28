class Solution:
    def minCut(self, s: str) -> int:
        regs = '#'.join(s)
        res = []
        for i in range(len(regs)):
            for j in range(1, len(regs)):
                st = i - j
                ed = i + j
                if st < 0 or ed >= len(regs) or regs[st] != regs[ed]:
                    res.append(j-1)
                    break
        memo = {}
        return self.search(0, res, regs, memo) - 1


    def search(self, start, res, regs, memo):
        if start == len(regs)-1 :
            return 1
        if start >= len(regs):
            return 0

        if start in memo.keys():
            return memo[start]

        lens = []
        for mid,radius in enumerate(res):
            st = mid - radius
            if start <= mid and start >= st:
                move = mid - st
                # +1 : 右边界的下一个为访问字符
                end = mid + move + 1
                #  跳过'#'
                if end < len(regs):
                    end = end if (regs[end] != '#')  else end + 1 
                le = self.search(end, res, regs, memo)
                lens.append(le+1)

        memo[start] = min(lens)
        return min(lens)

if __name__ == "__main__":
    # s = 'bbccdccbb'
    # 75
    s = "fifgbeajcacehiicccfecbfhhgfiiecdcjjffbghdidbhbdbfbfjccgbbdcjheccfbhafehieabbdfeigbiaggchaeghaijfbjhi"
    # 273
    # s = "adabdcaebdcebdcacaaaadbbcadabcbeabaadcbcaaddebdbddcbdacdbbaedbdaaecabdceddccbdeeddccdaabbabbdedaaabcdadbdabeacbeadbaddcbaacdbabcccbaceedbcccedbeecbccaecadccbdbdccbcbaacccbddcccbaedbacdbcaccdcaadcbaebebcceabbdcdeaabdbabadeaaaaedbdbcebcbddebccacacddebecabccbbdcbecbaeedcdacdcbdbebbacddddaabaedabbaaabaddcdaadcccdeebcabacdadbaacdccbeceddeebbbdbaaaaabaeecccaebdeabddacbedededebdebabdbcbdcbadbeeceecdcdbbdcbdbeeebcdcabdeeacabdeaedebbcaacdadaecbccbededceceabdcabdeabbcdecdedadcaebaababeedcaacdbdacbccdbcece"
    so = Solution()
    print(so.minCut((s)))