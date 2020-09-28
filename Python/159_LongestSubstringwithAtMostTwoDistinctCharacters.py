"""
Given a string s , find the length of the longest substring t  that contains at most 2 distinct characters.

Example 1:

Input: "eceba"
Output: 3
Explanation: t is "ece" which its length is 3.
Example 2:

Input: "ccaabbb"
Output: 5
Explanation: t is "aabbb" which its length is 5.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-substring-with-at-most-two-distinct-characters
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


from collections import deque
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, string: str) -> int:
        res = 0
        dq = deque([])
        counts = dict()
        for letter in string:
            if letter not in counts and len(counts) == 2:
                while dq:
                    v = dq.popleft()
                    counts[v] -= 1
                    if counts[v] == 0:
                        del counts[v]
                        break
            dq.append(letter)
            counts[letter] = counts.get(letter, 0) + 1
            res = max(res, sum(counts.values()))
        return res


from collections import Counter
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, string: str) -> int:
        res = 0
        i = 0
        counts = Counter()
        l_set = set()
        for j, v in enumerate(string):
            l_set.add(v)
            if len(l_set) > 2:
                while i < j:
                    pre_v = string[i]
                    counts[pre_v] -= 1
                    i += 1
                    if counts[pre_v] == 0:
                        l_set.remove(pre_v)
                        break
            counts[v] += 1
            res = max(res, j-i+1)
        return res

S = Solution()
string = "eceba"
print(S.lengthOfLongestSubstringTwoDistinct(string))
string = "ccaabbb"
print(S.lengthOfLongestSubstringTwoDistinct(string))
string = "ababacccccc"
print(S.lengthOfLongestSubstringTwoDistinct(string))