"""
Given string S and a dictionary of words words, find the number of words[i] that is a subsequence of S.

Example :
Input: 
S = "abcde"
words = ["a", "bb", "acd", "ace"]
Output: 3
Explanation: There are three words in words that are a subsequence of S: "a", "acd", "ace".
Note:

All words in words and S will only consists of lowercase letters.
The length of S will be in the range of [1, 50000].
The length of words will be in the range of [1, 5000].
The length of words[i] will be in the range of [1, 50].
"""
class Solution:
    def numMatchingSubseq(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        res = 0
        for word in words:
            index = -1
            for letter in word:
                index = S.find(letter, index+1)
                if index == -1:
                    break
            # print(index)
            if index != -1:
                res += 1
        return res
s = Solution()
S = "abcde"
words = ["a", "bb", "acd", "ace"]
print(s.numMatchingSubseq(S, words))