"""
Given a string s. An awesome substring is a non-empty substring of s such that we can make any number of swaps in order to make it palindrome.

Return the length of the maximum length awesome substring of s.

 

Example 1:

Input: s = "3242415"
Output: 5
Explanation: "24241" is the longest awesome substring, we can form the palindrome "24142" with some swaps.
Example 2:

Input: s = "12345678"
Output: 1
Example 3:

Input: s = "213123"
Output: 6
Explanation: "213123" is the longest awesome substring, we can form the palindrome "231132" with some swaps.
Example 4:

Input: s = "00"
Output: 2
 

Constraints:

1 <= s.length <= 10^5
s consists only of digits.
"""



class Solution:
    def longestAwesome(self, string: str) -> int:
        seen = {0:-1}
        res, prefix = 0, 0
        for i,v in enumerate(string):
            prefix ^= (1 << int(v))
            res = max(res, i - seen.get(prefix, float('inf'))) #all even nums
            for num in range(10): #1 odd num
                x = prefix ^ (1 << num)
                res = max(res, i - seen.get(x, float('inf')))
            seen[prefix] = min(seen.get(prefix, float('inf')), i)
        return res

from collections import defaultdict
class Solution:
    def longestAwesome(self, string: str) -> int:
        seen = defaultdict(lambda: float('inf'))
        seen[0] = -1
        res, prefix = 0, 0
        for i,v in enumerate(string):
            prefix ^= (1 << int(v))
            res = max(res, i - seen[prefix])
            for num in range(10):
                x = prefix ^ (1 << num)
                res = max(res, i - seen[x])
            seen[prefix] = min(seen[prefix], i)
        return res


S = Solution()
string = "3242415"
print(S.longestAwesome(string))
string = "12345678"
print(S.longestAwesome(string))
string = "213123"
print(S.longestAwesome(string))
string = "00"
print(S.longestAwesome(string))
