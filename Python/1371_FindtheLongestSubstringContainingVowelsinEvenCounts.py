"""
Given the string s, return the size of the longest substring containing each vowel an even number of times. That is, 'a', 'e', 'i', 'o', and 'u' must appear an even number of times.

 

Example 1:

Input: s = "eleetminicoworoep"
Output: 13
Explanation: The longest substring is "leetminicowor" which contains two each of the vowels: e, i and o and zero of the vowels: a and u.
Example 2:

Input: s = "leetcodeisgreat"
Output: 5
Explanation: The longest substring is "leetc" which contains two e's.
Example 3:

Input: s = "bcbcbc"
Output: 6
Explanation: In this case, the given string "bcbcbc" is the longest because all vowels: a, e, i, o and u appear zero times.
 

Constraints:

1 <= s.length <= 5 x 10^5
s contains only lowercase English letters.
"""


from collections import defaultdict
class Solution:
    def findTheLongestSubstring(self, string: str) -> int:
        vowels = 'aeiou'
        vowels_dict = dict(zip(vowels, range(5)))
        curr = 0
        pos_dict = defaultdict(lambda: float('inf'))
        pos_dict[0] = -1
        res = 0
        for i, v in enumerate(string):
            if v in vowels_dict:
                curr ^= 1 << vowels_dict[v]
            res = max(res, i - pos_dict[curr])
            pos_dict[curr] = min(pos_dict[curr], i)
        return res


from collections import defaultdict
class Solution:
    def findTheLongestSubstring(self, string: str) -> int:
        vowels = 'aeiou'
        vowels_dict = dict(zip(vowels, range(5)))
        curr = 0
        pos_dict = {0:-1}
        res = 0
        for i, v in enumerate(string):
            if v in vowels_dict:
                curr ^= 1 << vowels_dict[v]
            if curr in pos_dict:
                res = max(res, i - pos_dict[curr])
            else:
                pos_dict[curr] = i
        return res


S = Solution()
string = "eleetminicoworoep"
print(S.findTheLongestSubstring(string))
string = "leetcodeisgreat"
print(S.findTheLongestSubstring(string))
string = "bcbcbc"
print(S.findTheLongestSubstring(string))