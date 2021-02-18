"""
Given a string s, return the number of distinct substrings of s.

A substring of a string is obtained by deleting any number of characters (possibly zero) from the front of the string and any number (possibly zero) from the back of the string.

 

Example 1:

Input: s = "aabbaba"
Output: 21
Explanation: The set of distinct strings is ["a","b","aa","bb","ab","ba","aab","abb","bab","bba","aba","aabb","abba","bbab","baba","aabba","abbab","bbaba","aabbab","abbaba","aabbaba"]
Example 2:

Input: s = "abcdefg"
Output: 28
 

Constraints:

1 <= s.length <= 500
s consists of lowercase English letters.
 

Follow up: Can you solve this problem in O(n) time complexity?

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/number-of-distinct-substrings-in-a-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def countDistinct(self, string: str) -> int:
        visited = set()
        len_s = len(string)
        for left in range(len_s):
            for right in range(left + 1, len_s + 1):
                visited.add(string[left: right])
        return len(visited)

class Solution:
    def countDistinct(self, string: str) -> int:
        visited = set()
        len_s = len(string)
        for right in range(1, len_s + 1):
            left = 0
            while left < right and string[left: right] not in visited:
                visited.add(string[left: right])
                left += 1
            # print(visited)
        return len(visited)

S = Solution()
s = "aabbaba"
print(S.countDistinct(s))
s = "abcdefg"
print(S.countDistinct(s))