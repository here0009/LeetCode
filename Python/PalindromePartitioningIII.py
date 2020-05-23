"""
You are given a string s containing lowercase letters and an integer k. You need to :

First, change some characters of s to other lowercase English letters.
Then divide s into k non-empty disjoint substrings such that each substring is palindrome.
Return the minimal number of characters that you need to change to divide the string.

 

Example 1:

Input: s = "abc", k = 2
Output: 1
Explanation: You can split the string into "ab" and "c", and change 1 character in "ab" to make it palindrome.
Example 2:

Input: s = "aabbc", k = 3
Output: 0
Explanation: You can split the string into "aa", "bb" and "c", all of them are palindrome.
Example 3:

Input: s = "leetcode", k = 8
Output: 0
 

Constraints:

1 <= k <= s.length <= 100.
s only contains lowercase English letters.

"""
"""
Thoughts:
dp(start, k) to calculate the changes needed to make that make s[start:] k parts
"""
from functools import lru_cache
class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        @lru_cache(None)
        def nChanges(i,j):
            """
            change s[i:j] to a palindrom seq
            """
            res = 0
            while i < j:
                if s[i] != s[j]:
                    res += 1
                i += 1
                j -= 1
            return res

        @lru_cache(None)
        def dp(start, k):
            if k == 1:
                return nChanges(start, len_s-1)
            if len_s - start == k:
                return 0
            res = float('inf')
            for i in range(start, len_s-k+1): #max i is len_s-k, so the remaning length is lens-(i+1) = k -1
                res = min(res, nChanges(start,i)+dp(i+1,k-1))
            return res

        len_s = len(s)
        return dp(0,k)

S = Solution()

s = "abc"
k = 2
print(S.palindromePartition(s,k))

s = "aabbc"
k = 3
print(S.palindromePartition(s,k))

s = "leetcode"
k = 8
print(S.palindromePartition(s,k))