"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""
class Solution_1:
    def generateParenthesis(self, n: int):
        """
        wrong answer
        """
        if n == 0:
            return []
        if n == 1:
            return ['()']
        children = self.generateParenthesis(n-1)
        res = set()
        for child in children:
            res |= set(['()'+ child, '(' + child + ')', child+'()']) 
        return list(res)

class Solution_2:
    def generateParenthesis(self, n: int):
        def backtrack(string, left, right):
            # print(string, left, right)
            if len(string) == 2*n:
                self.res.append(string)
                return
            if left < n:
                backtrack(string + '(', left+1, right)
            if right < left:
                backtrack(string + ')', left, right+1)
        
        self.res = []
        backtrack('',0,0)
        return self.res

class Solution:
    def generateParenthesis(self, n: int):
        if n == 0:
            return ['']
        res = []
        for c in range(n):
            for left in self.generateParenthesis(c):
                for right in self.generateParenthesis(n-c-1):
                    res.append('{}({})'.format(left, right)) #same as res.append('({}){}'.format(left, right))
        # print(n,res)
        return res


s = Solution()
print(s.generateParenthesis(3))
# print(s.generateParenthesis(0))
# print(s.generateParenthesis(1))
# l1= ["((())())","()(()())","()((()))","((()()))","(())()()","((()))()","(()()())","(((())))","()()()()","(()(()))","(()())()","()(())()","()()(())"]

# l2 = ["(((())))","((()()))","((())())","((()))()","(()(()))","(()()())","(()())()","(())(())","(())()()","()((()))","()(()())","()(())()","()()(())","()()()()"]

# print(set(l2)-set(l1))