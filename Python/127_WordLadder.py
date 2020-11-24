"""
Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list.
Note:

Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: 0

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
"""


from typing import List
from collections import defaultdict
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        TLE
        """
        def similar(w1, w2):
            cost = 0
            for i in range(len_w):
                cost += (w1[i] != w2[i])
                if cost > 1:
                    return False
            return cost == 1

        wordList.append(beginWord)
        length = len(wordList)
        if length == 0 or endWord not in wordList:
            return 0
        len_w = len(wordList[0])
        transform_dict = defaultdict(set)
        for i in range(length-1):
            for j in range(i+1, length):
                if similar(wordList[i], wordList[j]):
                    transform_dict[wordList[i]].add(wordList[j])
                    transform_dict[wordList[j]].add(wordList[i])
        # print(transform_dict)
        bfs = set([beginWord])
        visited = set([beginWord])
        res = 2
        while bfs:
            bfs2 = set()
            # print(bfs)
            for word in bfs:
                for next_word in transform_dict[word]:
                    if next_word == endWord:
                        return res
                    if next_word not in visited:
                        visited.add(next_word)
                        bfs2.add(next_word)
            bfs = bfs2
            res += 1
        return 0

from typing import List
from collections import defaultdict
from string import ascii_lowercase
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def transform(word):
            res = set()
            for i in range(len_w):
                for letter in ascii_lowercase:
                    t_word = word[:i] + letter + word[i+1:]
                    if t_word in word_set and t_word not in visited:
                        visited.add(t_word)
                        res.add(t_word)
            return res


        word_set = set(wordList)
        if not word_set or endWord not in word_set:
            return 0
        len_w = len(wordList[0])
        # transform_dict = defaultdict(set)
        bfs = set([beginWord])
        visited = set([beginWord])
        res = 1
        while bfs:
            bfs2 = set()
            if endWord in bfs:
                return res
            for word in bfs:
                bfs2 |= transform(word)
            res += 1
            bfs = bfs2
        return 0



S = Solution()
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
print(S.ladderLength(beginWord, endWord, wordList))
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]
print(S.ladderLength(beginWord, endWord, wordList))