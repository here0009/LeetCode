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


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        """
        use bfs try to remove every '(' or ')' if we can
        """
        def isValid(string):
            left, right = 0, 0
            for c in string:
                if c == '(':
                    left += 1
                elif c == ')':
                    right += 1
                if right > left:
                    return False
            # print(string, left, right)
            return left == right

        bfs = set([s])
        flag = False
        while bfs:
            res = set()
            bfs2 = set()
            for string in bfs:
                if isValid(string):
                    flag = True
                    res.add(string)
                if flag:
                    continue
                for i in range(len(string)):
                    if string[i] in '()':
                        bfs2.add(string[:i] + string[i + 1:])
            if flag:
                break
            bfs = bfs2
        return list(res)


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        """
        use bfs try to remove every '(' or ')' if we can
        """
        def isValid(string):
            left, right = 0, 0
            for c in string:
                if c == '(':
                    left += 1
                elif c == ')':
                    right += 1
                if right > left:
                    return False
            return left == right

        bfs = set([s])
        while bfs:
            valid = list(filter(isValid, bfs))
            if valid:
                return valid
            bfs = {string[:i] + string[i + 1:] for string in bfs for i in range(len(string)) if string[i] in '()'}
        return None

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