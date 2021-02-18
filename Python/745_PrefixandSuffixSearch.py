"""
Given many words, words[i] has weight i.

Design a class WordFilter that supports one function, WordFilter.f(String prefix, String suffix). It will return the word with given prefix and suffix with maximum weight. If no word exists, return -1.

Examples:

Input:
WordFilter(["apple"])
WordFilter.f("a", "e") // returns 0
WordFilter.f("b", "") // returns -1
 

Note:

words has length in range [1, 15000].
For each test case, up to words.length queries WordFilter.f may be made.
words[i] has length in range [1, 10].
prefix, suffix have lengths in range [0, 10].
words[i] and prefix, suffix queries consist of lowercase letters only.
"""


from typing import Set
class TrieNode:
    def __init__(self):
        self.children = {}
        self.index = set()


class TrieTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str, i: int) -> None:
        node = self.root
        for w in word:
            if w not in node.children:
                node.children[w] = TrieNode()
            node.children[w].index.add(i)
            node = node.children[w]
        node.children['$'] = '$'

    def query(self, word: str) -> Set[int]:
        node = self.root
        for w in word:
            if w not in node.children:
                return set()
            node = node.children[w]
        return node.index

from functools import lru_cache
class WordFilter:
    """
    use a variation of Trie tree, self.index record the index of words that got the prefix or suffix
    """
    def __init__(self, words):
        self.preTrie = TrieTree()
        self.suffTrie = TrieTree()
        for i, word in enumerate(words):
            self.preTrie.insert(word, i)
            self.suffTrie.insert(word[::-1], i)

    @lru_cache(None)
    def f(self, prefix: str, suffix: str) -> int:
        p_set = self.preTrie.query(prefix)
        s_set = self.suffTrie.query(suffix[::-1])
        lst = list(p_set & s_set)
        return max(lst) if lst else -1



class TrieNode:
    def __init__(self):
        self.children = {}
        self.index = -1


class TrieTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str, i: int) -> None:
        node = self.root
        for w in word:
            if w not in node.children:
                node.children[w] = TrieNode()
            node.children[w].index = i
            node = node.children[w]
        node.children['$'] = '$'

    def query(self, word: str) -> Set[int]:
        node = self.root
        for w in word:
            if w not in node.children:
                return -1
            node = node.children[w]
        return node.index


class WordFilter:
    """
    use a variation of Trie tree, self.index record the index of words that got the prefix or suffix
    because the length of the word is short, we could enumerate all suffix of word, and creat a tree use suffix + # + word, then search for suffix + # + pre
    """
    def __init__(self, words):
        self.trie = TrieTree()
        for i, word in enumerate(words):
            for j in range(len(word)):
                self.trie.insert(word[j:] + '#' + word, i)

    @lru_cache(None)
    def f(self, prefix: str, suffix: str) -> int:
        return self.trie.query(suffix + '#' + prefix)

# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)
wf = WordFilter(["apple", "apfsfwefle", "banana"])
print(wf.f("a", "e"))
print(wf.f("b", ""))
print(wf.f("app", "el"))
print(wf.f("b", "a"))

["WordFilter","f","f","f","f","f","f","f","f","f","f"]
[[["cabaabaaaa","ccbcababac","bacaabccba","bcbbcbacaa","abcaccbcaa","accabaccaa","cabcbbbcca","ababccabcb","caccbbcbab","bccbacbcba"]],["bccbacbcba","a"],["ab","abcaccbcaa"],["a","aa"],["cabaaba","abaaaa"],["cacc","accbbcbab"],["ccbcab","bac"],["bac","cba"],["ac","accabaccaa"],["bcbb","aa"],["ccbca","cbcababac"]]
# Output:
# [null,9,-1,5,-1,-1,-1,-1,-1,3,-1]
# Expected:
# [null,9,4,5,0,8,1,2,5,3,1]