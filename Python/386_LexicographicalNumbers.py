"""
Given an integer n, return 1 - n in lexicographical order.

For example, given 13, return: [1,10,11,12,13,2,3,4,5,6,7,8,9].

Please optimize your algorithm to use less time and space. The input size may be as large as 5,000,000.
"""


from typing import List
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        lst = sorted(str(i) for i in range(1, n+1))
        return [int(s) for s in lst]

S = Solution()
print(S.lexicalOrder(13))
