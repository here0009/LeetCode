"""
Implement a magic directory with buildDict, and search methods.

For the method buildDict, you'll be given a list of non-repetitive words to build a dictionary.

For the method search, you'll be given a word, and judge whether if you modify exactly one character into another character in this word, the modified word is in the dictionary you just built.

Example 1:
Input: buildDict(["hello", "leetcode"]), Output: Null
Input: search("hello"), Output: False
Input: search("hhllo"), Output: True
Input: search("hell"), Output: False
Input: search("leetcoded"), Output: False
Note:
You may assume that all the inputs are consist of lowercase letters a-z.
For contest purpose, the test data is rather small by now. You could think about highly efficient algorithm after the contest.
Please remember to RESET your class variables declared in class MagicDictionary, as static/class variables are persisted across multiple test cases. Please see here for more details.
"""

class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = set()

    def buildDict(self, in_dict) -> None:
        """
        Build a dictionary through a list of words
        """
        # self.dict = dict()
        self.dict = set(in_dict)
        

    def search(self, word: str) -> bool:
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        """
        len_word = len(word)
        for key in self.dict:
            diff = 0
            if len(key) == len_word:
                for i in range(len_word):
                    if key[i] != word[i]:
                        diff += 1
                    if diff > 1:
                        break
            if diff == 1:
                return True
        return False
        


# Your MagicDictionary object will be instantiated and called as such:
obj = MagicDictionary()
obj.buildDict(dict)
param_2 = obj.search(word)

