"""
括号。设计一种算法，打印n对括号的所有合法的（例如，开闭一一对应）组合。

说明：解集不能包含重复的子集。

例如，给出 n = 3，生成结果为：

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/bracket-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
print(3)

from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        wrong answer
        """

        def genParen(n):
            if n == 0:
                return set([''])
            if n == 1:
                return set(['()'])
            res = set()
            for elem in genParen(n - 1):
                res.add('()' + elem)
                res.add('(' + elem + ')')
                res.add(elem +'()')
            return res

        return list(genParen(n))

# from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        def genParen(path, left, right):
            if left == right == n:
                self.res.add(path)
                return
            if left < n:
                genParen(path + '(', left + 1, right)
            if left > right:
                genParen(path + ')', left, right + 1)

        self.res = set()
        genParen('', 0, 0)
        # print(n)
        return list(self.res)

S = Solution()
print(S.generateParenthesis(3))

output = ["((()))()","()((()))","()(()())","(()(()))","(())()()","(()())()","((())())","(((())))","(()()())","((()()))","()()()()","()()(())","()(())()"]
expected =["(((())))","((()()))","((())())","((()))()","(()(()))","(()()())","(()())()","(())(())","(())()()","()((()))","()(()())","()(())()","()()(())","()()()()"]
print(len(output), len(expected))
for o, e in zip(sorted(output), sorted(expected)):
    print(o, e)
print(sorted(expected)[-1])