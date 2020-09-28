"""
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Write a function to determine if a number is strobogrammatic. The number is represented as a string.

 

Example 1:

Input: num = "69"
Output: true
Example 2:

Input: num = "88"
Output: true
Example 3:

Input: num = "962"
Output: false
Example 4:

Input: num = "1"
Output: true

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/strobogrammatic-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        length = len(num)
        d, r = divmod(length, 2)
        if r == 1 and num[d] not in {'0', '1', '8'}:
            return False
        pairs = {'0':'0', '1':'1', '6':'9', '8':'8', '9':'6'}
        for i in range(d):
            if num[i] not in pairs or pairs[num[i]] != num[length-1-i]:
                return False
        return True


S = Solution()
num = "69"
print(S.isStrobogrammatic(num))
num = "88"
print(S.isStrobogrammatic(num))
num = "962"
print(S.isStrobogrammatic(num))
num = "1812"
print(S.isStrobogrammatic(num))