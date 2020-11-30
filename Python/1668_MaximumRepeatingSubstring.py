"""
For a string sequence, a string word is k-repeating if word concatenated k times is a substring of sequence. The word's maximum k-repeating value is the highest value k where word is k-repeating in sequence. If word is not a substring of sequence, word's maximum k-repeating value is 0.

Given strings sequence and word, return the maximum k-repeating value of word in sequence.

 

Example 1:

Input: sequence = "ababc", word = "ab"
Output: 2
Explanation: "abab" is a substring in "ababc".
Example 2:

Input: sequence = "ababc", word = "ba"
Output: 1
Explanation: "ba" is a substring in "ababc". "baba" is not a substring in "ababc".
Example 3:

Input: sequence = "ababc", word = "ac"
Output: 0
Explanation: "ac" is not a substring in "ababc". 
 

Constraints:

1 <= sequence.length <= 100
1 <= word.length <= 100
sequence and word contains only lowercase English letters.
"""


class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        if sequence.find(word) == -1:
            return 0
        left = 1
        right = len(sequence)//len(word) + 1
        while left < right:
            mid = (left + right)//2
            if word*mid in sequence:
                left = mid + 1
            else:
                right = mid
        return left-1



S = Solution()
sequence = "ababc"
word = "ab"
print(S.maxRepeating(sequence, word))
sequence = "ababc"
word = "ba"
print(S.maxRepeating(sequence, word))
sequence = "ababc"
word = "ac"
print(S.maxRepeating(sequence, word))
sequence = "baba"
word = "b"
print(S.maxRepeating(sequence, word))
