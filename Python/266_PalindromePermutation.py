"""
Given a string, determine if a permutation of the string could form a palindrome.

Example 1:

Input: "code"
Output: false
Example 2:

Input: "aab"
Output: true
Example 3:

Input: "carerac"
Output: true

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/palindrome-permutation
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


from collections import Counter
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        counter = Counter(s)
        return sum(v % 2 == 1 for v in counter.values()) < 2

S = Solution()
s = "code"
print(S.canPermutePalindrome(s))
s = "aab"
print(S.canPermutePalindrome(s))
s = "carerac"
print(S.canPermutePalindrome(s))