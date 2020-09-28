"""
Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

Example:
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Input: word1 = “coding”, word2 = “practice”
Output: 3
Input: word1 = "makes", word2 = "coding"
Output: 1
Note:
You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shortest-word-distance
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
                res = min(res, abs(j-i))
        return res

S = Solution()
words = ["practice", "makes", "perfect", "coding", "makes"]
word1 = "coding"
word2 = "practice"
print(S.shortestDistance(words, word1, word2))
word1 = "makes"
word2 = "coding"
print(S.shortestDistance(words, word1, word2))