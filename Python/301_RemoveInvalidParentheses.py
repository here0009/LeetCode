"""
Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).

Example 1:

Input: "()())()"
Output: ["()()()", "(())()"]
Example 2:

Input: "(a)())()"
Output: ["(a)()()", "(a())()"]
Example 3:

Input: ")("
Output: [""]
"""


from typing import List
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        """
        Thought
        """

        left, right = 0, 0
        bfs = [[]]
        right_p_tmp = []
        no_remove = True
        for i,v in enumerate(s):
            # print(i,v,bfs,right_p_tmp, left, right)
            if v == '(':
                left += 1
            elif v == ')':
                right += 1
                if right > left:
                    no_remove = False
                    bfs2 = []
                    if not right_p_tmp:
                        bfs2.extend(lst+[i] for lst in bfs)
                    else:
                        for j in right_p_tmp:
                            bfs2.extend(lst + [j] for lst in bfs)
                        right_p_tmp = [i]
                    bfs = bfs2
                    right -= 1
                else:
                    right_p_tmp.append(i)
            # print(i,v,bfs,right_p_tmp, left, right)

        # print(bfs, left, right)
        if no_remove and left == right:
            return [s]
        res = []
        if left != right:
            return ['']
        for lst in bfs:
            tmp = set(lst)
            res.append(''.join(v for i,v in enumerate(s) if i not in tmp))
        return res


from typing import List
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        """
        wrong answer, we can also remove left parentheses to make the string valid
        """

        left, right = 0, 0
        bfs = [[]]
        right_p_tmp = []
        no_remove = True
        for i,v in enumerate(s):
            # print(i,v,bfs,right_p_tmp, left, right)
            if v == '(':
                left += 1
            elif v == ')':
                right += 1
                if right > left:
                    no_remove = False
                    bfs2 = []
                    if not right_p_tmp:
                        bfs2.extend(lst+[i] for lst in bfs)
                    else:
                        for j in right_p_tmp:
                            bfs2.extend(lst + [j] for lst in bfs)
                        right_p_tmp = [i]
                    bfs = bfs2
                    right -= 1
                else:
                    right_p_tmp.append(i)
            # print(i,v,bfs,right_p_tmp, left, right)

        # print(bfs, left, right)
        if no_remove and left == right:
            return [s]
        res = []
        if left != right:
            return ['']
        for lst in bfs:
            tmp = set(lst)
            res.append(''.join(v for i,v in enumerate(s) if i not in tmp))
        return res

S = Solution()
s = "()())()"
print(S.removeInvalidParentheses(s))
s = "(a)())()"
print(S.removeInvalidParentheses(s))
s = ")("
print(S.removeInvalidParentheses(s))
s = "))"
print(S.removeInvalidParentheses(s))
s = ""
print(S.removeInvalidParentheses(s))
s = "x("
print(S.removeInvalidParentheses(s))