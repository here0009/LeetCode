"""
Given a list of strings words representing an English Dictionary, find the longest word in words that can be built one character at a time by other words in words. If there is more than one possible answer, return the longest word with the smallest lexicographical order.

If there is no answer, return the empty string.
Example 1:
Input: 
words = ["w","wo","wor","worl", "world"]
Output: "world"
Explanation: 
The word "world" can be built one character at a time by "w", "wo", "wor", and "worl".
Example 2:
Input: 
words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
Output: "apple"
Explanation: 
Both "apply" and "apple" can be built from other words in the dictionary. However, "apple" is lexicographically smaller than "apply".
Note:

All the strings in the input will only contain lowercase letters.
The length of words will be in the range [1, 1000].
The length of words[i] will be in the range [1, 30].
"""
class Solution_1:
    def longestWord(self, words: 'List[str]') -> 'str':
        
        words = sorted(words, reverse = True)
        words = sorted(words, key = len)
        res = words[0]
        for word in words[1:]:
            break_flag = False
            tmp = word[:-1]
            for i in range(len(tmp),0,-1):
                if tmp[:i] not in words:
                    break_flag = True
                    break
            if not break_flag:
                res = word
        return res
        # print(word)

class Solution:
    def longestWord(self, words: 'List[str]') -> 'str':
        tested = set()
        res = ''
        words = sorted(words, key = len)
        for word in words:
            if len(word) == 1 or word[:-1] in tested:
                tested.add(word)
                # print(tested)
                if len(word) > len(res):
                    res = word
                elif len(word) == len(res) and word < res:
                    res = word
        return res

s = Solution()
words = ["w","wo","wor","worl", "world"]
print(s.longestWord(words))

words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
print(s.longestWord(words))

words = ["w"]
print(s.longestWord(words))

words = ["yo","ew","fc","zrc","yodn","fcm","qm","qmo","fcmz","z","ewq","yod","ewqz","y"]
print(s.longestWord(words))