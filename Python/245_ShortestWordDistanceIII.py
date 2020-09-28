"""
Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

word1 and word2 may be the same and they represent two individual words in the list.

Example:
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Input: word1 = “makes”, word2 = “coding”
Output: 1
Input: word1 = "makes", word2 = "makes"
Output: 3
Note:
You may assume word1 and word2 are both in the list.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shortest-word-distance-iii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from collections import defaultdict
class Solution:
    def shortestDistance(self, words, word1, word2) -> int:
        index_dict = defaultdict(list)
        for i,v in enumerate(words):
            index_dict[v].append(i)
        res = float('inf')
        for i in index_dict[word1]:
            for j in index_dict[word2]:
                if i != j:
                    res = min(res, abs(j-i))
        return res

from collections import defaultdict
class Solution:
    def shortestWordDistance(self, words, word1: str, word2: str) -> int:
        index_dict = defaultdict(list)
        for i,v in enumerate(words):
            index_dict[v].append(i)
        res = float('inf')
        l1, l2 = index_dict[word1], index_dict[word2]
        i1, i2 = 0, 0
        while i1 < len(l1) and i2 < len(l2):
            if l1[i1] != l2[i2]:
                res = min(res, abs(l1[i1]-l2[i2]))
            if l1[i1] < l2[i2]:
                i1 += 1
            else:
                i2 += 1
        return res


S = Solution()
words = ["practice", "makes", "perfect", "coding", "makes"]
word1 = "coding"
word2 = "practice"
print(S.shortestWordDistance(words, word1, word2))
word1 = "makes"
word2 = "coding"
print(S.shortestWordDistance(words, word1, word2))