"""
Given an integer, return its base 7 string representation.

Example 1:
Input: 100
Output: "202"
Example 2:
Input: -7
Output: "-10"
Note: The input will be in range of [-1e7, 1e7].
"""
class Solution:
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return '0'
        minus_flag = False
        if num < 0:
            minus_flag = True
        res = []
        num = abs(num)
        while num > 0:
            num, rmd = divmod(num, 7)
            res.append(rmd)
        res_str = ''.join([str(i) for i in res[::-1]])
        if minus_flag:
            res_str = '-'+res_str
        return res_str

s = Solution()
print(s.convertToBase7(100))
print(s.convertToBase7(-70))
print(s.convertToBase7(0))
print(s.convertToBase7(1))