"""
Given a string array words, find the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters. You may assume that each word will contain only lower case letters. If no such two words exist, return 0.

Example 1:

Input: ["abcw","baz","foo","bar","xtfn","abcdef"]
Output: 16
Explanation: The two words can be "abcw", "xtfn".
Example 2:

Input: ["a","ab","abc","d","cd","bcd","abcd"]
Output: 4
Explanation: The two words can be "ab", "cd".
Example 3:

Input: ["a","aa","aaa","aaaa"]
Output: 0
Explanation: No such pair of words.
"""


class Solution:
    def maxProduct(self, words) -> int:
        length = len(words)
        res = 0
        for i in range(length -1):
            for j in range(i+1, length):
                if not set(words[i]) & set(words[j]):
                    res = max(res, len(words[i])*len(words[j]))
        return res


class Solution:
    def maxProduct(self, words) -> int:
        sign_dict = dict()
        for word in words:
            sign = 0
            for letter in word:
                sign |= (1 << ord(letter) - ord('a'))
            sign_dict[sign] = max(sign_dict.get(sign, 0), len(word))
        # print(sign_dict)
        res = 0
        for x in sign_dict:
            for y in sign_dict:
                if x & y == 0:
                    res = max(res, sign_dict[x] * sign_dict[y])
        return res

S = Solution()
words = ["abcw","baz","foo","bar","xtfn","abcdef"]
print(S.maxProduct(words))
words = ["a","ab","abc","d","cd","bcd","abcd"]
print(S.maxProduct(words))
words = ["a","aa","aaa","aaaa"]
print(S.maxProduct(words))