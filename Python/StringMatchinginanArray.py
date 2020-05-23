"""
Given an array of string words. Return all strings in words which is substring of another word in any order. 

String words[i] is substring of words[j], if can be obtained removing some characters to left and/or right side of words[j].

 

Example 1:

Input: words = ["mass","as","hero","superhero"]
Output: ["as","hero"]
Explanation: "as" is substring of "mass" and "hero" is substring of "superhero".
["hero","as"] is also a valid answer.
Example 2:

Input: words = ["leetcode","et","code"]
Output: ["et","code"]
Explanation: "et", "code" are substring of "leetcode".
Example 3:

Input: words = ["blue","green","bu"]
Output: []
 

Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 30
words[i] contains only lowercase English letters.
It's guaranteed that words[i] will be unique.
"""
from collections import deque
class Solution:
    def stringMatching(self, words):
        res = set()
        words_set = set()
        words = sorted(words, key = len)
        for word in words:
            if word in words_set:
                continue
            for substring in words_set:
                if substring in word:
                    res.add(substring)
                    # words_set.remove(substring)
            words_set.add(word)

        return list(res)

class Solution:
    def stringMatching(self, words):
        res = []
        words = sorted(words, key = len)
        length = len(words)
        for i in range(length-1):
            pattern = words[i]
            for j in range(i+1, length):
                if pattern in words[j]:
                    res.append(pattern)
                    break
        return res 

S = Solution()
words = ["mass","as","hero","superhero"]
print(S.stringMatching(words))
words = ["leetcode","et","code"]
print(S.stringMatching(words))
words = ["blue","green","bu"]
print(S.stringMatching(words))
