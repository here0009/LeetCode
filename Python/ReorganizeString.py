"""
Given a string S, check if the letters can be rearranged so that two characters that are adjacent to each other are not the same.

If possible, output any possible result.  If not possible, return the empty string.

Example 1:

Input: S = "aab"
Output: "aba"
Example 2:

Input: S = "aaab"
Output: ""
Note:

S will consist of lowercase letters and have length in range [1, 500].
"""
from collections import Counter
class Solution:
    def reorganizeString(self, string: str) -> str:
        s_counter = Counter(string)
        len_s = len(string)
        keys_list = sorted(s_counter.keys(), key = lambda x: s_counter[x], reverse = True)
        max_v = max(s_counter.values())
        flag = max_v <= len_s//2 + len_s % 2
        if not flag: #not possible
            return ''
        res = [' ']*len_s
        index = 0
        for i in range(0,len_s,2):
            while s_counter[keys_list[index]] <= 0:
                index += 1
            res[i] = keys_list[index]
            s_counter[keys_list[index]] -= 1

        for i in range(1,len_s,2):
            while s_counter[keys_list[index]] <= 0:
                index += 1
            res[i] = keys_list[index]
            s_counter[keys_list[index]] -= 1
        return ''.join(res)

s = Solution()
string = "aab"
print(s.reorganizeString(string))
string = "aaab"
print(s.reorganizeString(string))