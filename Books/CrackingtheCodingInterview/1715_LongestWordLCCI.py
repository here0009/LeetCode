"""
给定一组单词words，编写一个程序，找出其中的最长单词，且该单词由这组单词中的其他单词组合而成。若有多个长度相同的结果，返回其中字典序最小的一项，若没有符合要求的单词则返回空字符串。

示例：

输入： ["cat","banana","dog","nana","walk","walker","dogwalker"]
输出： "dogwalker"
解释： "dogwalker"可由"dog"和"walker"组成。
提示：

0 <= len(words) <= 200
1 <= len(words[i]) <= 100

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-word-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


from typing import List
class TrieNode:

    def __init__(self):
        self.children = dict()
        self.isEnd = False

class TireTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for w in word:
            if w not in node.children:
                node.children[w] = TrieNode()
            node = node.children[w]
        node.isEnd = True

    def query(self, word):
        node = self.root
        for w in word:
            if w not in node.children:
                return False
            node = node.children[w]
        return node.isEnd is True


class Solution:
    def longestWord(self, words: List[str]) -> str:
        """
        wrong answer because word can be constructed by more than one subword
        """

        tree = TireTree()
        for word in words:
            tree.insert(word)

        res = ''
        for word in words:
            for i in range(1, len(word)):
                if len(word) > len(res) or (len(word) == len(res) and word < res):
                    if tree.query(word[:i]) and tree.query(word[i:]):
                        res = word
        return res


from functools import lru_cache
class Solution:
    def longestWord(self, words: List[str]) -> str:

        @lru_cache(None)
        def dp(word, flag):
            if flag is True and word in word_set:
                return True
            for i in range(1, len(word)):
                if dp(word[:i], True) and dp(word[i:], True):
                    return True
            return False


        word_set = set(words)

        res = ''
        for word in words:
            for i in range(1, len(word)):
                if len(word) > len(res) or (len(word) == len(res) and word < res):
                    if dp(word, False):
                        res = word
        return res


S = Solution()
words = ["cat","banana","dog","nana","walk","walker","dogwalker"]
print(S.longestWord(words))
words = ["qlmql","qlmqlmqqlqmqqlq","mqqlqmqqlqmqqlq","mqqlq","mqqlqlmlsmqq","qmlmmmmsm","lmlsmqq","slmsqq","mslqssl","mqqlqmqqlq"]
# 输出：
# "qlmqlmqqlqmqqlq"
# 预期结果：
# "mqqlqmqqlqmqqlq"
print(S.longestWord(words))
words = ["llllcccl","clclll","ccc","llccllccl","lcclccclcl","c"]
print(S.longestWord(words))
# 输出：
# ""
# 预期结果：
# "ccc"