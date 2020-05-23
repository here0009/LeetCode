"""
In English, we have a concept called root, which can be followed by some other words to form another longer word - let's call this word successor. For example, the root an, followed by other, which can form another word another.

Now, given a dictionary consisting of many roots and a sentence. You need to replace all the successor in the sentence with the root forming it. If a successor has many roots can form it, replace it with the root with the shortest length.

You need to output the sentence after the replacement.

Example 1:

Input: dict_list = ["cat", "bat", "rat"]
sentence = "the cattle was rattled by the battery"
Output: "the cat was rat by the bat"
 

Note:

The input will only have lower-case letters.
1 <= dict words number <= 1000
1 <= sentence words number <= 1000
1 <= root length <= 100
1 <= sentence words length <= 1000
"""
class TrieNode:
    def __init__(self):
        # self.val = letter
        self.children = {}

class TrieTree:
    def __init__(self):
        # self.root = {}
        self.children = {}

    def insert(self, word):
        root = self.children
        for letter in word:
            if letter not in root:
                root[letter] = {}
            root = root[letter]
        root['$'] = {}
        # print(self.children)


    def search(self, word):
        root = self.children
        ans = ''
        for letter in word:
            if letter not in root:
                return word
            ans += letter
            root = root[letter]
            if '$' in root:
                return ans
        return word

class Solution:
    def replaceWords(self, dict_list, sentence: str) -> str:
        root = TrieTree()
        for word in dict_list:
            root.insert(word)
        res = []
        s_list = sentence.split()
        for word in s_list:
            re_word = root.search(word)
            res.append(re_word)
        return ' '.join(res)


s = Solution()
dict_list = ["cat", "bat", "rat"]
sentence = "the cattle was rattled by the battery"
print(s.replaceWords(dict_list, sentence))