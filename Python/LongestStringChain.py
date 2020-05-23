"""
Given a list of words, each word consists of English lowercase letters.

Let's say word1 is a predecessor of word2 if and only if we can add exactly one letter anywhere in word1 to make it equal to word2.  For example, "abc" is a predecessor of "abac".

A word chain is a sequence of words [word_1, word_2, ..., word_k] with k >= 1, where word_1 is a predecessor of word_2, word_2 is a predecessor of word_3, and so on.

Return the longest possible length of a word chain with words chosen from the given list of words.

 

Example 1:

Input: ["a","b","ba","bca","bda","bdca"]
Output: 4
Explanation: one of the longest word chain is "a","ba","bda","bdca".
 

Note:

1 <= words.length <= 1000
1 <= words[i].length <= 16
words[i] only consists of English lowercase letters.
"""
import re
from collections import defaultdict
class Solution:
    def isPre(self,w1, w2):
        # if len(w2) != len(w1)+1:
        #     return False
        w1_pattern = r'\w*'+r'\w*'.join(list(w1))+r'\w*'
        # print(re.search(w1_pattern, w2))
        if re.search(w1_pattern, w2) is not None:
            return True
        return False

    def longestStrChain(self, words) -> int:
        def dfs(w):
            vis.add(w)
            length = 0
            if  w not in pre_dict:
                return 1
            for w2 in pre_dict[w]:
                length = max(length,dfs(w2)+1) 
            return length

        words_len_dict = defaultdict(set)
        pre_dict = defaultdict(set)
        res = 1
        for word in words:
            # words_len_dict[len(word)] = words_len_dict[len(word)]|{word}
            words_len_dict[len(word)].add(word)

        # print(words_len_dict)
        words_len = sorted(list(words_len_dict.keys()))
        # print(words_len)
        for i in range(1,len(words_len)):
            if words_len[i-1] + 1 == words_len[i]:
                for w1 in words_len_dict[words_len[i-1]]:
                    for w2 in words_len_dict[words_len[i]]:
                        # print(w1,w2)
                        # print(self.isPre(w1, w2))
                        if self.isPre(w1, w2):
                            pre_dict[w1].add(w2)
        # print(pre_dict)
        vis = set()
        for val in pre_dict.keys():
            if val not in vis:
                res = max(res,dfs(val))
            vis.add(val)
        return res


s = Solution()
words = ["a","b","ba","bca","bda","bdca"]
print(s.longestStrChain(words))
# print(s.isPre('a','ab'))