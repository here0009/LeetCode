"""
Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)
search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.

Example:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
Note:
You may assume that all words are consist of lowercase letters a-z.
"""
class TrieNode:
    def __init__(self):
        self.children = dict()
    def __repr__(self):
        return ' '.join(self.children.keys())

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        root = self.root
        for letter in word:
            if letter not in root.children:
                root.children[letter] = TrieNode()
            root = root.children[letter]
        root.children['$'] = TrieNode()


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        def dfs(root, word):
            if self.flag:
                return
            if len(word) == 0:
                if '$' in root.children:
                    print('2',root.children, word)
                    self.flag = True
                return

            letter = word[0]
            if letter != '.':
                if letter in root.children:
                    root = root.children[letter]
                    dfs(root, word[1:])
            else:
                for c in root.children:
                    dfs(root.children[c],word[1:])

        root = self.root
        self.flag = False
        dfs(root, word)
        return self.flag



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord("bad")
# obj.addWord("dad")
# obj.addWord("mad")
# print(obj.search("pad"))
# print(obj.search("bad"))
# print(obj.search(".ad"))
# print(obj.search("b.."))

""""
["WordDictionary","addWord","addWord","search","search","search","search","search","search","search","search"]
[[],["a"],["ab"],["a"],["a."],["ab"],[".a"],[".b"],["ab."],["."],[".."]]
Output = [null,null,null,true,false,false,false,false,false,true,false]
Expected = [null,null,null,true,true,true,false,true,false,true,true]
"""

"""
["WordDictionary","addWord","addWord","addWord","addWord","search","search","addWord","search","search","search","search","search","search"]
[[],["at"],["and"],["an"],["add"],["a"],[".at"],["bat"],[".at"],["an."],["a.d."],["b."],["a.d"],["."]]
Output = [null,null,null,null,null,false,false,null,true,true,false,true,true,false]
Expected = [null,null,null,null,null,false,false,null,true,true,false,false,true,false]
"""
obj = WordDictionary()
obj.addWord("at")
obj.addWord("and")
obj.addWord("an")
obj.addWord("add")
obj.addWord("baz")
print(obj.search("b."))
print(obj.search("babc"))