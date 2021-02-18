"""
Given a list of words (without duplicates), please write a program that returns all concatenated words in the given list of words.
A concatenated word is defined as a string that is comprised entirely of at least two shorter words in the given array.

Example:
Input: ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]

Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]

Explanation: "catsdogcats" can be concatenated by "cats", "dog" and "cats"; 
 "dogcatsdog" can be concatenated by "dog", "cats" and "dog"; 
"ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".
Note:
The number of elements of the given array will not exceed 10,000
The length sum of elements in the given array will not exceed 600,000.
All the input string will only include lower case letters.
The returned elements order does not matter.
"""


from typing import List
from functools import lru_cache
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        @lru_cache(None)
        def dfs(word):
            for j in range(1, len(word)):
                # print(j, word[:j], word[j:])
                if word[:j] in words_set:
                    if word[j:] in words_set or dfs(word[j:]):
                        return True
            return False

        res = []
        words_set = set(words)
        # print(words_set)
        for word in words:
            words_set.remove(word)
            if dfs(word):
                res.append(word)
            words_set.add(word)
        return res


S = Solution()
words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
print(S.findAllConcatenatedWordsInADict(words))
words = ["a","b","ab","abc"]
print(S.findAllConcatenatedWordsInADict(words))