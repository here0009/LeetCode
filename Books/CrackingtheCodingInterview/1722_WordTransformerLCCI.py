"""
给定字典中的两个词，长度相等。写一个方法，把一个词转换成另一个词， 但是一次只能改变一个字符。每一步得到的新词都必须能在字典中找到。

编写一个程序，返回一个可能的转换序列。如有多个可能的转换序列，你可以返回任何一个。

示例 1:

输入:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

输出:
["hit","hot","dot","lot","log","cog"]
示例 2:

输入:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

输出: []

解释: endWord "cog" 不在字典中，所以不存在符合要求的转换序列。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/word-transformer-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


from typing import List
from collections import defaultdict
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[str]:

        def path(idx):
            res = []
            while idx != -1:
                res.append(idx)
                idx = root[idx]
            return [wordList[idx] for idx in res][::-1]

        def isConvert(a, b):
            res = 0
            for k in range(len_w):
                if a[k] != b[k]:
                    res += 1
                    if res > 1:
                        return False
            return res == 1


        len_w = len(beginWord)
        wordList.append(beginWord)
        wordSet = set([w for w in wordList if len(w) == len_w])
        wordList = list(wordSet)
        # print(wordList, wordSet)
        edges = defaultdict(list)
        if endWord not in wordSet:
            return []

        length = len(wordList)
        for i in range(length):
            for j in range(i + 1, length):
                if isConvert(wordList[i], wordList[j]):
                    edges[i].append(j)
                    edges[j].append(i)

        bfs = [wordList.index(beginWord)]
        target = wordList.index(endWord)
        visited = set(bfs)

        # print(bfs, target, visited)
        root = [-1] * length
        while bfs:
            bfs2 = []
            # print([wordList[i] for i in bfs])
            for i in bfs:
                for j in edges[i]:
                    if j not in visited:
                        root[j] = i
                        visited.add(j)
                        bfs2.append(j)
                    if j == target:
                        return path(j)
            bfs = bfs2
        return []


from typing import List
from collections import defaultdict
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[str]:

        def path(idx):
            res = []
            while idx != -1:
                res.append(idx)
                idx = root[idx]
            return [wordList[idx] for idx in res][::-1]

        def isConvert(a, b):
            res = 0
            for k in range(len_w):
                if a[k] != b[k]:
                    res += 1
                    if res > 1:
                        return False
            return res == 1


        len_w = len(beginWord)
        wordList.append(beginWord)
        wordSet = set([w for w in wordList if len(w) == len_w])
        wordList = list(wordSet)
        
        wordDict = dict([(v, i) for i, v in enumerate(wordList)])
        # print(wordSet, wordList, wordDict)
        if endWord not in wordSet:
            return []

        length = len(wordList)
        bfs = [wordDict[beginWord]]
        target = wordDict[endWord]
        wordSet -= set([beginWord]) # do not use set(beginWord)
        root = [-1] * length
        while bfs and wordSet:
            # print(bfs)
            # print(root)
            # print(wordSet)
            bfs2 = []
            tmpSet = set()
            for i in bfs:
                for w in wordSet:
                    j = wordDict[w]
                    if w not in tmpSet and isConvert(w, wordList[i]):
                        root[j] = i
                        tmpSet.add(w)
                        bfs2.append(j)
                        if j == target:
                            return path(j)
            bfs = bfs2
            wordSet -= tmpSet
        return []


S = Solution()
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
print(S.findLadders(beginWord, endWord, wordList))
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]
print(S.findLadders(beginWord, endWord, wordList))