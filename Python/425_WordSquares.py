"""
Given a set of words (without duplicates), find all word squares you can build from them.

A sequence of words forms a valid word square if the kth row and column read the exact same string, where 0 ≤ k < max(numRows, numColumns).

For example, the word sequence ["ball","area","lead","lady"] forms a word square because each word reads the same both horizontally and vertically.

b a l l
a r e a
l e a d
l a d y
Note:
There are at least 1 and at most 1000 words.
All words will have the exact same length.
Word length is at least 1 and at most 5.
Each word contains only lowercase English alphabet a-z.
Example 1:

Input:
["area","lead","wall","lady","ball"]

Output:
[
  [ "wall",
    "area",
    "lead",
    "lady"
  ],
  [ "ball",
    "area",
    "lead",
    "lady"
  ]
]

Explanation:
The output consists of two word squares. The order of output does not matter (just the order of words in each word square matters).
Example 2:

Input:
["abat","baba","atan","atal"]

Output:
[
  [ "baba",
    "abat",
    "baba",
    "atan"
  ],
  [ "baba",
    "abat",
    "baba",
    "atal"
  ]
]

Explanation:
The output consists of two word squares. The order of output does not matter (just the order of words in each word square matters).

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/word-squares
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# Solution 1
class TreeNode:
    def __init__(self, v):
        self.v = v
        self.children = dict()

    def insert(self, node, word):
        if not word:
            node.children['$'] = None
            return
        letter = word[0]
        if letter not in node.children:
            node.children[letter] = TreeNode(letter)
        node = node.children[letter]
        self.insert(node, word[1:])

    def dfs(self, node, path):
        if not node:
            self.res.append(path[:-1])
            return
        for letter in node.children:
            self.dfs(node.children[letter], path+letter)

    def search(self, node, pre):
        for letter in pre:
            if letter in node.children:
                node = node.children[letter]
            else:
                return []
        self.res = []
        for letter in node.children:
            self.dfs(node.children[letter], pre+letter)
        return self.res




class Solution:
    def wordSquares(self, words):
        """
        Thoughts: prefix tree
        """
        def dp(curr):
            len_curr = len(curr)
            if len_curr == length:
                self.res.append(curr)
                return
            prefix = ''
            for i in range(len_curr):
                prefix += curr[i][len_curr]
            lst = root.search(root, prefix)
            for word in lst:  # word can be used repeatedly
                dp(curr + [word])

        self.res = []
        if not words:
            return self.res
        length = len(words[0])

        root = TreeNode('')
        for word in words:
            root.insert(root, word)
        dp([])
        return self.res

# Solution 2
class TrieNode:
    def __init__(self):
        self.children = {}


class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.children['$'] = 0  # '$' means ending

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return '$' in curr.children

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True

    def dfs(self, node:TrieNode, path, res):
        if not node:
            res.append(path[:-1])  # exclude the last '$' sign
            return
        for letter in node.children:
            self.dfs(node.children[letter], path+letter, res)

    def getList(self, prefix):
        curr = self.root
        res = []
        for c in prefix:
            if c in curr.children:
                curr = curr.children[c]
            else:
                return res
        self.dfs(curr, prefix, res)
        return res


class Solution:
    def wordSquares(self, words):
        """
        Thoughts: prefix tree
        """
        def dp(curr):
            len_curr = len(curr)
            if len_curr == length:
                self.res.append(curr)
                return
            prefix = ''
            for i in range(len_curr):
                prefix += curr[i][len_curr]
            lst = root.getList(prefix)
            # print(curr, lst)
            for word in lst:  # word can be used repeatedly
                dp(curr + [word])

        self.res = []
        if not words:
            return self.res
        length = len(words[0])

        root = Trie()
        for word in words:
            root.insert(word)
        dp([])
        return self.res

S = Solution()
words = ["area","lead","wall","lady","ball"]
print(S.wordSquares(words))

words = ["abat","baba","atan","atal"]
print(S.wordSquares(words))