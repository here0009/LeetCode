"""
Given a string of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. The valid operators are +, - and *.

Example 1:

Input: "2-1-1"
Output: [0, 2]
Explanation: 
((2-1)-1) = 0 
(2-(1-1)) = 2
Example 2:

Input: "2*3-4*5"
Output: [-34, -14, -10, -10, 10]
Explanation: 
(2*(3-(4*5))) = -34 
((2*3)-(4*5)) = -14 
((2*(3-4))*5) = -10 
(2*((3-4)*5)) = -10 
(((2*3)-4)*5) = 10
"""
class Solution:
    def diffWaysToCompute(self, string: str):
        signs = '+-*'
        def cal(string):
            # print(string)
            res =[]
            if not set(signs) & set(string):
                return [int(string)]
            
            for i in range(len(string)):
                s = string[i]
                if s in signs:
                    left = cal(string[:i])
                    right = cal(string[i+1:])
                    for l in left:
                        for r in right:
                            if s == '+':
                                res.append(l+r)
                            elif s == '-':
                                res.append(l-r)
                            else:
                                res.append(l*r)
            return res

        return cal(string)

S = Solution()
string = "2-1-1"
print(S.diffWaysToCompute(string))
string ="2*3-4*5"
print(S.diffWaysToCompute(string))