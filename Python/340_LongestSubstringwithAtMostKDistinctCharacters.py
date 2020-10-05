"""
Given a string, find the length of the longest substring T that contains at most k distinct characters.

Example 1:

Input: s = "eceba", k = 2
Output: 3
Explanation: T is "ece" which its length is 3.
Example 2:

Input: s = "aa", k = 1
Output: 2
Explanation: T is "aa" which its length is 2.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-substring-with-at-most-k-distinct-characters
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


from collections import Counter
class Solution:
    def lengthOfLongestSubstringKDistinct(self, string: str, k: int) -> int:
        if k == 0:
            return 0
        left = 0
        counter = Counter()
        res = 0
        for right in range(len(string)):
            counter[string[right]] += 1
            while len(counter) > k:
                counter[string[left]] -= 1
                if counter[string[left]] == 0:
                    del counter[string[left]]
                left += 1
            res = max(res, right-left+1)
        return res


S = Solution()
string = "eceba"
k = 2
print(S.lengthOfLongestSubstringKDistinct(string, k))
string = "aa"
k = 1
print(S.lengthOfLongestSubstringKDistinct(string, k))

string = "a"
k = 0
print(S.lengthOfLongestSubstringKDistinct(string, k))