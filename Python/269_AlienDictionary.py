"""
There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you. You receive a list of non-empty words from the dictionary, where words are sorted lexicographically by the rules of this new language. Derive the order of letters in this language.

Example 1:

Input:
[
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]

Output: "wertf"
Example 2:

Input:
[
  "z",
  "x"
]

Output: "zx"
Example 3:

Input:
[
  "z",
  "x",
  "z"
] 

Output: "" 

Explanation: The order is invalid, so return "".
Note:

You may assume all letters are in lowercase.
If the order is invalid, return an empty string.
There may be multiple valid order of letters, return any one of them is fine.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/alien-dictionary
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


from collections import Counter
from collections import defaultdict
class Solution:
    def alienOrder(self, words) -> str:
        """
        topological sort, remeber each letter's indegree, and link out if a letter's indegree is 0 append it to res
        """
        def genOrders(words):
            """
            generate orders from words
            """
            # print(words)
            if len(words) == 0 or self.flag or all(len(w) == 0 for w in words):
                return
            for i in range(1, len(words)):
                if words[i] == '' and words[i-1] != '':
                    self.flag = True
                    return
            letters = [word[0] for word in words if len(word) > 0]
            pre = letters[0]
            next_words = [words[0][1:]]
            for i in range(1, len(letters)):
                # print(next_words)
                curr = letters[i]
                if curr != pre:
                    if pre in next_letter[curr]:
                        self.flag = True
                        return
                    if curr not in next_letter[pre]:
                        indegree[curr] += 1
                        next_letter[pre].add(curr)
                    pre = curr
                    genOrders(next_words)
                    next_words = [words[i][1:]]
                else:
                    next_words.append(words[i][1:])
            genOrders(next_words)

        self.flag = False # if a letter is infront of blank, then set self.flag to True
        indegree = Counter()
        next_letter = defaultdict(set)
        genOrders(words)
        all_letters = set(''.join(words))
        # print(all_letters)
        bfs = set(all_letters - set(indegree.keys()))
        # print(words)
        # print(indegree)
        # print(next_letter)
        res = ""
        if not bfs or self.flag:
            return res
        while bfs:
            bfs2 = set()
            for i in bfs:
                res += i
                for j in next_letter[i]:
                    indegree[j] -= 1
                    if indegree[j] == 0:
                        bfs2.add(j)
            bfs = bfs2
        if sum(indegree.values()) > 0:
            return ""
        # print(indegree)
        # print(next_letter)
        return res


from collections import Counter
from collections import defaultdict
class Solution:
    def alienOrder(self, words) -> str:
        """
        topological sort, remeber each letter's indegree, and link out if a letter's indegree is 0 append it to res
        """
        def blank(word):
            """
            if word is '', return ' ' 
            """
            return ' ' if word == '' else word

        def genOrders(words):
            """
            generate orders from words
            """
            if len(words) == 0 or all(w == ' ' for w in words):
                return
            letters = [word[0] for word in words if len(word) > 0]
            if not letters:
                return
            pre = letters[0]
            next_words = [blank(words[0][1:])]
            for i in range(1, len(letters)):
                curr = letters[i]
                if curr != pre:
                    if curr not in next_letter[pre]:
                        indegree[curr] += 1
                        next_letter[pre].add(curr)
                    pre = curr
                    genOrders(next_words)
                    next_words = [words[i][1:]]
                else:
                    next_words.append(blank(words[i][1:]))
            genOrders(next_words)

        indegree = Counter()
        next_letter = defaultdict(set)
        genOrders(words)
        all_letters = set(''.join(words))
        bfs = set(all_letters - set(indegree.keys()))
        if ' ' in next_letter:
            bfs.add(' ')

        res = ""
        if not bfs or ' ' in indegree:
            return res

        while bfs:
            bfs2 = set()
            for i in bfs:
                if i != ' ':
                    res += i
                for j in next_letter[i]:
                    indegree[j] -= 1
                    if indegree[j] == 0:
                        bfs2.add(j)
            bfs = bfs2

        if sum(indegree.values()) > 0:
            return ""
        return res

S = Solution()
# words = ["wrt","wrf","er","ett","rftt"]
# print(S.alienOrder(words))
# words = ["z","x"]
# print(S.alienOrder(words))
# words = ["z","x","z"]
# print(S.alienOrder(words))
# words = ["z","z"]
# print(S.alienOrder(words))
# words = ["za","zb","ca","cb"]
# print(S.alienOrder(words))
# # 输出：
# # "zac"
# # 预期结果：
# # "abzc"
# words = ["abc","ab"]
# print(S.alienOrder(words))
# # 输出：
# # "abc"
# # 预期结果：
# # ""
# words = ["ri","xz","qxf","jhsguaw","dztqrbwbm","dhdqfb","jdv","fcgfsilnb","ooby"]
# print(S.alienOrder(words))

# # 输出：
# # "bculsnvtywgzmairxhq"
# # 预期结果：
# # ""
# words = ["bsusz","rhn","gfbrwec","kuw","qvpxbexnhx","gnp","laxutz","qzxccww"]
# print(S.alienOrder(words))
# 输出：
# "pnsctwezvbfaxuhr"
# 预期结果：
# ""
words = ["wrt","wrtkj"]
print(S.alienOrder(words))
# 输出：
# ""
# 预期结果：
# "jkrtw"