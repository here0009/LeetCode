"""
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
"""


class Solution:
    def wordBreak(self, string: str, wordDict) -> bool:
        self.res = False
        wordDict = set(wordDict)
        def check(string):
            if self.res or len(set(string) - word_letters) > 0:
                return
            if not string:
                self.res = True
            tmp = ''
            for i,s in enumerate(string):
                tmp += s
                if tmp in wordDict:
                    check(string[i+1:])

        word_letters = set()
        for word in wordDict:
            word_letters |= set(word)

        check(string)
        return self.res


class Solution:
    def wordBreak(self, string: str, wordDict) -> bool:
        wordDict = set(wordDict + [''])
        length = len(string)
        max_word_len = max(map(len, wordDict))  # in case wordDict is empty
        dp = [True] + [False]*length
        for i in range(length):
            for j in range(i+1, min(i+max_word_len, length)+1):
                # print(string[i:j])
                if dp[i] and string[i:j] in wordDict:  # dp[i] for string[i-1]
                    dp[j] = True
        return dp[-1]

class Solution:
    def wordBreak(self, s, words):
        ok = [True]
        max_len = max(map(len,words+['']))
        words = set(words)
        for i in range(1, len(s)+1):
            ok += any(ok[j] and s[j:i] in words for j in range(max(0, i - max_len), i)),
        return ok[-1]

S = Solution()
string ="bb"
wordDict = ["a","b","bbb","bbbb"]
print(S.wordBreak(string, wordDict))
string ="a"
wordDict =[]
print(S.wordBreak(string, wordDict))
string = "leetcode"
wordDict = ["leet", "code"]
print(S.wordBreak(string, wordDict))
string = "applepenapple"
wordDict = ["apple", "pen"]
print(S.wordBreak(string, wordDict))
string = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
print(S.wordBreak(string, wordDict))


string ="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
wordDict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
print(S.wordBreak(string, wordDict))
