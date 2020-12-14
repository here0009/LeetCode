class Solution:
    def numberOfMatches(self, n: int) -> int:
        res = 0
        while n > 1:
            # print(n, res)
            q, rmd = divmod(n, 2)
            n = q + rmd
            res += q
        return res

S = Solution()
print(S.numberOfMatches(7))
print(S.numberOfMatches(14))