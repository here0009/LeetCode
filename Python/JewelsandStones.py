class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        ans = 0
        for s in S:
            if s in J:
                ans += 1
        return ans

s = Solution()
print(s.numJewelsInStones("Aa", "aAAbbbb"))
J = "z"
S = "ZZ"
print(s.numJewelsInStones(J,S))