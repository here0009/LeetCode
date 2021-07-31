"""
A wonderful string is a string where at most one letter appears an odd number of times.

For example, "ccjjc" and "abab" are wonderful, but "ab" is not.
Given a string word that consists of the first ten lowercase English letters ('a' through 'j'), return the number of wonderful non-empty substrings in word. If the same substring appears multiple times in word, then count each occurrence separately.

A substring is a contiguous sequence of characters in a string.

 

Example 1:

Input: word = "aba"
Output: 4
Explanation: The four wonderful substrings are underlined below:
- "aba" -> "a"
- "aba" -> "b"
- "aba" -> "a"
- "aba" -> "aba"
Example 2:

Input: word = "aabb"
Output: 9
Explanation: The nine wonderful substrings are underlined below:
- "aabb" -> "a"
- "aabb" -> "aa"
- "aabb" -> "aab"
- "aabb" -> "aabb"
- "aabb" -> "a"
- "aabb" -> "abb"
- "aabb" -> "b"
- "aabb" -> "bb"
- "aabb" -> "b"
Example 3:

Input: word = "he"
Output: 2
Explanation: The two wonderful substrings are underlined below:
- "he" -> "h"
- "he" -> "e"
 

Constraints:

1 <= word.length <= 105
word consists of lowercase English letters from 'a' to 'j'.
"""


class Solution:
    def wonderfulSubstrings(self, word: str) -> int:

        len_w = len(word)
        preSum = [[0] * 10]
        for i in range(len_w):
            idx = ord(word[i]) - ord('a')
            preSum.append(preSum[-1][:])
            preSum[i + 1][idx] = preSum[i][idx] + 1
        # for row in preSum:
        #     print(row)
        res = 0
        for i in range(1, len_w + 1):
            for j in range(i):
                diff = [preSum[i][k] - preSum[j][k] for k in range(10)]
                res += sum([d % 2 for d in diff]) < 2
        return res



S = Solution()
word = "aba"
print(S.wonderfulSubstrings(word))
word = "aabb"
print(S.wonderfulSubstrings(word))
word = "he"
print(S.wonderfulSubstrings(word))
word = "fiabhedce"
print(S.wonderfulSubstrings(word))