"""
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

Example:

Input: "aab"
Output:
[
  ["aa","b"],
  ["a","a","b"]
]
"""


from typing import List
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        length = len(s)
        if length == 0:
            return [[]]
        res = []
        for i in range(1, length+1):
            left, right = s[:i], s[i:]
            # print(s, left, right)
            if left == left[::-1]:
                res.extend([[left] + r for r in self.partition(right)])
        return res

S = Solution()
s = 'aab'
print(S.partition(s))
s = 'abccba'
print(S.partition(s))
s = 'a'
print(S.partition(s))
s = "bb"
print(S.partition(s))