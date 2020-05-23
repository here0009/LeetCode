"""
Given a string s consisting only of characters a, b and c.

Return the number of substrings containing at least one occurrence of all these characters a, b and c.

 

Example 1:

Input: s = "abcabc"
Output: 10
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" and "abc" (again). 
Example 2:

Input: s = "aaacb"
Output: 3
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "aaacb", "aacb" and "acb". 
Example 3:

Input: s = "abc"
Output: 1
 

Constraints:

3 <= s.length <= 5 x 10^4
s only consists of a, b or c characters.
"""


from collections import Counter
class Solution:
    def numberOfSubstrings(self, string: str) -> int:
        def valid():
            return s_counter['a'] > 0 and s_counter['b'] > 0 and s_counter['c'] > 0

        length = len(string)
        s_counter = Counter()
        dp = [0]*length
        left = 0
        flag = False
        for i, v in enumerate(string):
            s_counter[v] += 1
            tmp = 0
            # print(i,v,s_counter)
            if valid():
                if not flag: #1st time valid
                    tmp = 1
                    flag = True
                else:
                    tmp = dp[i-1]
            while valid() and left < length and s_counter[string[left]] > 1:
                s_counter[string[left]] -= 1
                left += 1
                tmp += 1
            dp[i] = tmp
        # print(dp)
        return sum(dp)


class Solution:
    def numberOfSubstrings(self, string: str) -> int:
        def valid():
            return s_counter['a'] > 0 and s_counter['b'] > 0 and s_counter['c'] > 0

        length = len(string)
        s_counter = Counter()
        res = 0
        left = 0
        for i, v in enumerate(string):
            s_counter[v] += 1
            while left < length and valid():
                s_counter[string[left]] -= 1
                left += 1
            res += left
            # there are total left substrings that start at 0~left-1, end at i
        return res


class Solution:
    def numberOfSubstrings(self, string: str) -> int:
        res = 0
        last_index = [-1]*3
        for i, v in enumerate(string):
            last_index[ord(v) - ord('a')] = i
            res += min(last_index) + 1
            #substring can start at 0~min(last_index), end at i
        return res

S = Solution()
string = "abcabc"
print(S.numberOfSubstrings(string))
string = "aaacb"
print(S.numberOfSubstrings(string))
string = "abc"
print(S.numberOfSubstrings(string))
string = "acbbcac"
print(S.numberOfSubstrings(string))
# Output
# 4
# Expected
# 11
string = "abab"
print(S.numberOfSubstrings(string))