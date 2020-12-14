"""
Given a string s and an integer k, return the length of the longest substring of s such that the frequency of each character in this substring is greater than or equal to k.

 

Example 1:

Input: s = "aaabb", k = 3
Output: 3
Explanation: The longest substring is "aaa", as 'a' is repeated 3 times.
Example 2:

Input: s = "ababbc", k = 2
Output: 5
Explanation: The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.
 

Constraints:

1 <= s.length <= 104
s consists of only lowercase English letters.
1 <= k <= 105
"""


from collections import Counter
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        def check(string):
            counts = Counter(string)
            split_index = []
            for i,v in enumerate(string):
                if counts[v] < k:
                    split_index.append(i)
            # print(split_index, string)
            if not split_index:
                return len(string)
            split_index.append(len(string))
            pre = 0
            res = 0
            for curr in split_index:
                if curr - pre >= k:
                    res = max(res, check(string[pre:curr]))
                pre = curr+1
            return res

        return check(s)

S = Solution()
# s = "aaabb"
# k = 3
# print(S.longestSubstring(s, k))
# s = "ababbc"
# k = 2
# print(S.longestSubstring(s, k))
s = "bbaaacbd"
k = 3
print(S.longestSubstring(s, k))

# Output
# 0
# Expected
# 3