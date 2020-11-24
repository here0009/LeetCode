"""
Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

 

Example 1:

Input: s = "aab"
Output: 1
Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.
Example 2:

Input: s = "a"
Output: 0
Example 3:

Input: s = "ab"
Output: 1
 

Constraints:

1 <= s.length <= 2000
s consists of lower-case English letters only.
"""


from functools import lru_cache
class Solution:
    def minCut(self, s: str) -> int:
        """
        TLE
        """
        @lru_cache(None)
        def dp(string):
            if string == string[::-1]:
                return 0
            res = float('inf')
            for i in range(1, len(string)):
                res = min(res, dp(string[:i]) + dp(string[i:]))
            return res + 1

        return dp(s)

from functools import lru_cache
from bisect import bisect_right
from collections import defaultdict
class Solution:
    def minCut(self, s: str) -> int:
        @lru_cache(None)
        def isPalindrome(string):
            if len(string) <= 1:
                return True
            left, right = 0, len(string)-1
            while left < right:
                if string[left] != string[right]:
                    return False
                left += 1
                right -= 1
            return True

        @lru_cache(None)
        def dp(string):
            if isPalindrome(string):
                return 0
            res = float('inf')
            for i in range(1, len(string)):
                res = min(res, dp(string[:i]) + dp(string[i:]))
            return res + 1

        return dp(s)

from functools import lru_cache
import sys
class Solution:
    def minCut(self, s: str) -> int:
        sys.setrecursionlimit(999999)
        @lru_cache(None)
        def dp(string):
            if string == string[::-1]:
                return 0
            res = len(string)
            for i in range(1, len(string)):
                if string[:i]==string[:i][::-1]:
                    res = min(res, dp(string[i:]))
            return res + 1
        return dp(s)

S = Solution()
s = "aab"
print(S.minCut(s))
s = "a"
print(S.minCut(s))
s = "ab"
print(S.minCut(s))
s = "apjesgpsxoeiokmqmfgvjslcjukbqxpsobyhjpbgdfruqdkeiszrlmtwgfxyfostpqczidfljwfbbrflkgdvtytbgqalguewnhvvmcgxboycffopmtmhtfizxkmeftcucxpobxmelmjtuzigsxnncxpaibgpuijwhankxbplpyejxmrrjgeoevqozwdtgospohznkoyzocjlracchjqnggbfeebmuvbicbvmpuleywrpzwsihivnrwtxcukwplgtobhgxukwrdlszfaiqxwjvrgxnsveedxseeyeykarqnjrtlaliyudpacctzizcftjlunlgnfwcqqxcqikocqffsjyurzwysfjmswvhbrmshjuzsgpwyubtfbnwajuvrfhlccvfwhxfqthkcwhatktymgxostjlztwdxritygbrbibdgkezvzajizxasjnrcjwzdfvdnwwqeyumkamhzoqhnqjfzwzbixclcxqrtniznemxeahfozp"
print(S.minCut(s))