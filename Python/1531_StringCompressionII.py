"""
Run-length encoding is a string compression method that works by replacing consecutive identical characters (repeated 2 or more times) with the concatenation of the character and the number marking the count of the characters (length of the run). For example, to compress the string "aabccc" we replace "aa" by "a2" and replace "ccc" by "c3". Thus the compressed string becomes "a2bc3".

Notice that in this problem, we are not adding '1' after single characters.

Given a string s and an integer k. You need to delete at most k characters from s such that the run-length encoded version of s has minimum length.

Find the minimum length of the run-length encoded version of s after deleting at most k characters.

 

Example 1:

Input: s = "aaabcccd", k = 2
Output: 4
Explanation: Compressing s without deleting anything will give us "a3bc3d" of length 6. Deleting any of the characters 'a' or 'c' would at most decrease the length of the compressed string to 5, for instance delete 2 'a' then we will have s = "abcccd" which compressed is abc3d. Therefore, the optimal way is to delete 'b' and 'd', then the compressed version of s will be "a3c3" of length 4.
Example 2:

Input: s = "aabbaa", k = 2
Output: 2
Explanation: If we delete both 'b' characters, the resulting compressed string would be "a4" of length 2.
Example 3:

Input: s = "aaaaaaaaaaa", k = 0
Output: 3
Explanation: Since k is zero, we cannot delete anything. The compressed string is "a11" of length 3.
 

Constraints:

1 <= s.length <= 100
0 <= k <= s.length
s contains only lowercase English letters.
"""

from collections import defaultdict
class Solution:
    def compress(string):
        res = ''
        if not string:
            return res
        pre, count = string[0], 1
        for i in range(1, len(string)):
            if string[i] != pre:
                if count != 1:
                    res += pre + count
                count = 1
                pre = string[i]
            else:
                count += 1
        res += pre + count
        return res

    def getLengthOfOptimalCompression(self, string: str, k: int) -> int:
        if k == 0:
            return self.compress(string)
        gaps = []
        pos = defaultdict(list)
        for i, v in enumerate(string):
            pos[v].append(i)


# https://leetcode.com/problems/string-compression-ii/discuss/755970/Python-dynamic-programming
from functools import lru_cache
class Solution:
    def getLengthOfOptimalCompression(self, string: str, k: int) -> int:

        @lru_cache(None)
        def dp(index, pre, count, ks):
            if ks < 0:
                return float('inf')
            if index >= length:
                return 0
            if string[index] == pre: #res only +1 when count in 1,9,99
                res = dp(index+1, pre, count+1, ks)
                if count in {1, 9, 99}:
                    res += 1
                return res
            else: #delete string[index] or keep it
                return min(dp(index+1, pre, count, ks-1), 1+dp(index+1, string[index], 1, ks))

        length = len(string)
        return dp(0, '', 0, k)

S = Solution()
string = "aaabcccd"
k = 2
print(S.getLengthOfOptimalCompression(string, k))
string = "aabbaa"
k = 2
print(S.getLengthOfOptimalCompression(string, k))
string = "aaaaaaaaaaa"
k = 0
print(S.getLengthOfOptimalCompression(string, k))