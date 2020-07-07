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
class TrieNode:
    def __init__():
        self.children = {}
        # self.index = None

class WordFilter:

    def __init__(self, words):
        preTrieNode = TrieNode()
        suffTrieNonde = TrieNode()
        for i, word in enumerate(words):
            pre = preTrieNode
            suff = suffTrieNonde
            for letter in word:
                if letter not in pre.children:
                    pre.children[letter] = TrieNode()
                pre = pre.children[letter]
                # pre.index = i
            for letter in word[::-1]:
                if letter not in suff.children:
                    suff.children[letter] = TrieNode()
                suff = suff.children[letter]
        

    def f(self, prefix: str, suffix: str) -> int:
        


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)
