"""
Given a binary string s ​​​​​without leading zeros, return true​​​ if s contains at most one contiguous segment of ones. Otherwise, return false.

 

Example 1:

Input: s = "1001"
Output: false
Explanation: The ones do not form a contiguous segment.
Example 2:

Input: s = "110"
Output: true
 

Constraints:

1 <= s.length <= 100
s[i]​​​​ is either '0' or '1'.
s[0] is '1'.
"""


class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        ones = [k for k in s.split('0') if len(k) > 0]
        # print(ones)
        return len(ones) == 1

S = Solution()
s = "1001"
print(S.checkOnesSegment(s))
s = "110"
print(S.checkOnesSegment(s))