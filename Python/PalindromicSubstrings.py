"""
Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

Example 1:

Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
 

Example 2:

Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
 

Note:

The input string length won't exceed 1000.
"""
from collections import defaultdict
class Solution:
    def countSubstrings(self, s: str) -> int:
        pldrmc_set = set()
        pos_dict = defaultdict(list)
        for i,c in enumerate(s):
            pos_dict[c].append(i)
        # print(pos_dict)
        res = len(s)
        for i, c in enumerate(s):
            poses = pos_dict[c]
            pos_i = 0
            while  poses[pos_i] < i:
                if (poses[pos_i] + 1, i-1) in pldrmc_set or (i - poses[pos_i] <= 2):
                    res += 1
                    pldrmc_set.add((poses[pos_i], i))
                pos_i += 1
        # for l,r in pldrmc_set:
        #     print(s[l:r+1])
        # print(pldrmc_set)
        return res

S = Solution()
s = 'abcabcacaae'
print(S.countSubstrings(s))

s = "abc"
print(S.countSubstrings(s))

s = "aaa"
print(S.countSubstrings(s))