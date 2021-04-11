"""
给定一份单词的清单，设计一个算法，创建由字母组成的面积最大的矩形，其中每一行组成一个单词(自左向右)，每一列也组成一个单词(自上而下)。不要求这些单词在清单里连续出现，但要求所有行等长，所有列等高。

如果有多个面积最大的矩形，输出任意一个均可。一个单词可以重复使用。

示例 1:

输入: ["this", "real", "hard", "trh", "hea", "iar", "sld"]
输出:
[
   "this",
   "real",
   "hard"
]
示例 2:

输入: ["aa"]
输出: ["aa","aa"]
说明：

words.length <= 1000
words[i].length <= 100
数据保证单词足够随机

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/word-rectangle-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


from collections import defaultdict
from typing import List


class Node:
    def __init__(self):
        self.isWord = False
        self.child = {}


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        curr = self.root
        for w in word:
            if w not in curr.child:
                curr.child[w] = Node()
            curr = curr.child[w]
        curr.isWord = True


class Solution:
    def maxRectangle(self, words: List[str]) -> List[str]:
        myTrie = Trie()
        len2word = defaultdict(list)
        for word in words:
            myTrie.insert(word)
            len2word[len(word)].append(word)
        self.area, self.res = 0, []
        # print(myTrie.root.child.keys())
        def dfs(state, width, depth, candidate):
            if width * depth > self.area and all([x.isWord for x in state]):
                self.area = width * depth
                self.res = candidate
                print(self.res, self.area, width, depth)
            for word in len2word[width]:
                nxt = []
                for cur, ch in zip(state, word):
                    if ch not in cur.child:
                        break
                    nxt.append(cur.child[ch])
                if len(nxt) == width:
                    dfs(nxt, width, depth + 1, candidate + [word])
            return

        mxlen = max(len2word)
        for w in sorted(len2word)[::-1]:
            if w * mxlen < self.area:
                break
            dfs([myTrie.root] * w, w, 0, [])
        # for row in self.res:
        #     print(row)
        return self.res

# 作者：ga-beng-cui-7
# 链接：https://leetcode-cn.com/problems/word-rectangle-lcci/solution/liang-chong-jian-zhi-ban-fa-by-ga-beng-cui-7/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

class TrieNode:

    def __init__(self):
        self.children = dict()
        self.isEnd = False

class TrieTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for w in word:
            if w not in node.children:
                node.children[w] = TrieNode()
            node = node.children[w]
        node.isEnd = True


class Solution:
    def maxRectangle(self, words: List[str]) -> List[str]:

        def dfs(status, width, depth, candidate):
            if all(x.isEnd for x in status) and width * depth > self.area:
                self.area = width * depth
                self.res = candidate
                # return
            for word in len_dict[width]:
                nxt = []
                for ch, w in zip(status, word):
                    if w not in ch.children:
                        break
                    nxt.append(ch.children[w])
                if len(nxt) == width:
                    dfs(nxt, width, depth + 1, candidate + [word])

        tree = TrieTree()
        len_dict = defaultdict(list)
        for word in words:
            tree.insert(word)
            len_dict[len(word)].append(word)

        len_dict_keys = sorted(len_dict.keys(), reverse = True)
        max_len = len_dict_keys[0]
        self.res, self.area = [], 0
        for w in len_dict_keys:
            if w * max_len < self.area:
                break
            dfs([tree.root] * w, w, 0, [])
        return self.res



S = Solution()
words = ["this", "real", "hard", "trh", "hea", "iar", "sld"]
print(S.maxRectangle(words))
words =  ["aa"]
print(S.maxRectangle(words))
