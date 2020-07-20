"""
Given a string s of lowercase letters, you need to find the maximum number of non-empty substrings of s that meet the following conditions:

The substrings do not overlap, that is for any two substrings s[i..j] and s[k..l], either j < k or i > l is true.
A substring that contains a certain character c must also contain all occurrences of c.
Find the maximum number of substrings that meet the above conditions. If there are multiple solutions with the same number of substrings, return the one with minimum total length. It can be shown that there exists a unique solution of minimum total length.

Notice that you can return the substrings in any order.

 

Example 1:

Input: s = "adefaddaccc"
Output: ["e","f","ccc"]
Explanation: The following are all the possible substrings that meet the conditions:
[
  "adefaddaccc"
  "adefadda",
  "ef",
  "e",
  "f",
  "ccc",
]
If we choose the first string, we cannot choose anything else and we'd get only 1. If we choose "adefadda", we are left with "ccc" which is the only one that doesn't overlap, thus obtaining 2 substrings. Notice also, that it's not optimal to choose "ef" since it can be split into two. Therefore, the optimal way is to choose ["e","f","ccc"] which gives us 3 substrings. No other solution of the same number of substrings exist.
Example 2:

Input: s = "abbaccd"
Output: ["d","bb","cc"]
Explanation: Notice that while the set of substrings ["d","abba","cc"] also has length 3, it's considered incorrect since it has larger total length.
 

Constraints:

1 <= s.length <= 10^5
s contains only lowercase English letters.
"""


from collections import defaultdict
from functools import lru_cache
class Solution:
    def maxNumOfSubstrings(self, string: str):
        index_dict = defaultdict(list)
        for i,v in enumerate(string):
            index_dict[v].append(i)


        def sumofLength(l):
            return sum([j-i for i,j in l])


        @lru_cache(None)
        def helper(i, j):
            res = []
            if index_dict[string[i]][-1] < j and index_dict[string[i]][0] >= i:
                res = [(i, j)]
            for k in range(i+1, j):
                if index_dict[string[k]][-1] < i and index_dict[string[k]][0] >= j:
                    continue
                pre = helper(i, k)
                latter = helper(k, j)
                if len(pre) + len(latter) > len(res):
                    res = pre + latter
                elif len(pre) + len(latter) == len(res):
                    if sumofLength(pre) + sumofLength(latter) < sumofLength(res):
                        res = pre + latter
            return res

        res = helper(0, len(string))
        return [string[i:j] for i,j in res]

# https://leetcode.com/problems/maximum-number-of-non-overlapping-substrings/discuss/744726/Python-Easy-to-Read-solution-with-explanation
from collections import defaultdict
class Solution:
    def maxNumOfSubstrings(self, string: str):
        index_dict = defaultdict(list)
        for i,c in enumerate(string):
            index_dict[c].append(i)

        for c in index_dict.keys():
            left, right = index_dict[c][0], index_dict[c][-1] + 1
            tmpl, tmpr = left, right
            while True:
                char_set = set(string[left:right])
                for k in char_set:
                    tmpl = min(index_dict[k][0], tmpl)
                    tmpr = max(index_dict[k][-1]+1, tmpr)
                if (tmpl, tmpr) == (left, right):
                    break
                else:
                    left, right = tmpl, tmpr
            index_dict[c] = [left, right]
        # print(index_dict)
        intervals = sorted(index_dict.values(), key=lambda x: x[1])
        # print(intervals)
        res, pre = [], 0
        for start, end in intervals:
            if start >= pre:
                res.append(string[start:end])
                pre = end
        return res


S = Solution()
# string = "adefaddaccc"
# print(S.maxNumOfSubstrings(string))
# string = "abbaccd"
# print(S.maxNumOfSubstrings(string))
# string = "abab"
# print(S.maxNumOfSubstrings(string))
# Input:
# "abab"
# Output:
# ["bab"]
# Expected:
# ["abab"]
string = "cbadabdb"
print(S.maxNumOfSubstrings(string))
# Output
# ["c","adabd"]
# Expected
# ["c","badabdb"]