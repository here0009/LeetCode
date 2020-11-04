"""
Given a text string and words (a list of strings), return all index pairs [i, j] so that the substring text[i]...text[j] is in the list of words.

 

Example 1:

Input: text = "thestoryofleetcodeandme", words = ["story","fleet","leetcode"]
Output: [[3,7],[9,13],[10,17]]
Example 2:

Input: text = "ababa", words = ["aba","ab"]
Output: [[0,1],[0,2],[2,3],[2,4]]
Explanation: 
Notice that matches can overlap, see "aba" is found in [0,2] and [2,4].
 

Note:

All strings contains only lowercase English letters.
It's guaranteed that all strings in words are different.
1 <= text.length <= 100
1 <= words.length <= 20
1 <= words[i].length <= 50
Return the pairs [i,j] in sorted order (i.e. sort them by their first coordinate in case of ties sort them by their second coordinate).

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/index-pairs-of-a-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def indexPairs(self, text: str, words):
        words_set = set(words)
        res = []
        length = len(text)
        for i in range(length):
            for j in range(i+1, length+1):
                if text[i:j] in words_set:
                    res.append([i,j-1])
        return res

# 作者：alvin-55
# 链接：https://leetcode-cn.com/problems/index-pairs-of-a-string/solution/bu-chong-python-by-alvin-55/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        ans = []
        def findall(p, s):
            i = s.find(p)
            while i != -1:
                yield i
                i = s.find(p, i + 1)
        for word in words:
            a =  [[i, i+len(word)-1] for i in findall(word, text)]
            ans.extend(a)
        return sorted(ans)
            
            
S = Solution()
text = "thestoryofleetcodeandme"
words = ["story","fleet","leetcode"]
print(S.indexPairs(text, words))
text = "ababa"
words = ["aba","ab"]
print(S.indexPairs(text, words))
