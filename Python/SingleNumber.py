class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = 0
        for i in nums:
            k ^= i
        return k

s = Solution()
print(s.singleNumber([4,1,2,1,2]))