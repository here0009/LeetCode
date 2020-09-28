"""
Design a class which receives a list of words in the constructor, and implements a method that takes two words word1 and word2 and return the shortest distance between these two words in the list. Your method will be called repeatedly many times with different parameters. 

Example:
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Input: word1 = “coding”, word2 = “practice”
Output: 3
Input: word1 = "makes", word2 = "coding"
Output: 1
Note:
You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shortest-word-distance-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from collections import defaultdict
class WordDistance:
    def __init__(self, words):
        self.index_dict = defaultdict(list)
        for i,v in enumerate(words):
            self.index_dict[v].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        res = float('inf')
        for i in self.index_dict[word1]:
            for j in self.index_dict[word2]:
                res = min(res, abs(j-i))
        return res


from collections import defaultdict
class WordDistance:
    def __init__(self, words):
        self.index_dict = defaultdict(list)
        for i,v in enumerate(words):
            self.index_dict[v].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        res = float('inf')
        l1, l2 = self.index_dict[word1], self.index_dict[word2]
        i1, i2 = 0, 0
        while i1 < len(l1) and i2 < len(l2):
            res = min(res, abs(l1[i1]-l2[i2]))
            if l1[i1] < l2[i2]:
                i1 += 1
            else:
                i2 += 1
        return res

# Your WordDistance object will be instantiated and called as such:

words = ["practice", "makes", "perfect", "coding", "makes"]
wd = WordDistance(words)
word1 = "coding"
word2 = "practice"
print(wd.shortest(word1, word2))
word1 = "makes"
word2 = "coding"
print(wd.shortest(word1, word2))