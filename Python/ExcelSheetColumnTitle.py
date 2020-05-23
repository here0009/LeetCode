"""
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
    ...
Example 1:

Input: 1
Output: "A"
Example 2:

Input: 28
Output: "AB"
Example 3:

Input: 701
Output: "ZY"
"""
class Solution:
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = ''
        while n != 0:
            q, r = divmod(n,26)
            if r == 0:
                r = 26
                q -= 1
            res = chr(r+ord('A')-1) + res
            n = q
        return res

class Solution_1:
    def convertToTitle(self, n):
        title = ''
        while n > 0:
            n -= 1 #it is very convinient to use n-1 in calculation
            title = "{}{}".format(chr(n%26 + 65),title)
            n //= 26
        return title

s = Solution()
n_list = [1,28,701]
for n in n_list:
    print(n, s.convertToTitle(n))