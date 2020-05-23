class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # the last one is 1, or the last one is 2, so

        if n == 1:
            ways = 1
        elif n == 2:
            ways = 2
        else:
            pre_2 = 1
            pre_1 = 2
            for num in range(3, n+1):
                ways = pre_1 + pre_2
                pre_2 = pre_1
                pre_1 = ways
        return ways

s = Solution()
input_list = [1,2,3,4,5,35]
for num in input_list:
    print(s.climbStairs(num))