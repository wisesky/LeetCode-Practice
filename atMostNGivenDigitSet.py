class Solution:
    def atMostNGivenDigitSet(self, D, N):
        """
        :type D: List[str]
        :type N: int
        :rtype: int
        """

        ld = len(D)
        n = str(N)
        ln = len(n)
        res = sum(ld ** i for i in range(1,ln))
        i = 0
        while i < ln:
            res += sum(c < n[i] for c in D) * (ld ** (ln - i -1))
            if n[i] not in D:
                break
            i += 1
        return res + (i == ln)