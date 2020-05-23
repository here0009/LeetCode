"""
There are N dominoes in a line, and we place each domino vertically upright.

In the beginning, we simultaneously push some of the dominoes either to the left or to the right.



After each second, each domino that is falling to the left pushes the adjacent domino on the left.

Similarly, the dominoes falling to the right push their adjacent dominoes standing on the right.

When a vertical domino has dominoes falling on it from both sides, it stays still due to the balance of the forces.

For the purposes of this question, we will consider that a falling domino expends no additional force to a falling or already fallen domino.

Given a string "S" representing the initial state. S[i] = 'L', if the i-th domino has been pushed to the left; S[i] = 'R', if the i-th domino has been pushed to the right; S[i] = '.', if the i-th domino has not been pushed.

Return a string representing the final state. 

Example 1:

Input: ".L.R...LR..L.."
Output: "LL.RR.LLRRLL.."
Example 2:

Input: "RR.L"
Output: "RR.L"
Explanation: The first domino expends no additional force on the second domino.
Note:

0 <= N <= 10^5
String dominoes contains only 'L', 'R' and '.'
"""
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        res = ''
        stack = []
        for d in dominoes:
            if not stack:
                if d == 'L':
                    res += d
                else:
                    stack.append(d)
            else:
                pre = stack[0]
                if d == 'L':
                    if pre == '.':
                        res += (len(stack)+1) * 'L'
                    elif pre == 'R':
                        k = (len(stack)-1)//2 + 1
                        if (len(stack)-1) % 2 == 1:
                            res += k*'R' + '.' + k*'L'
                        else:
                            res += k*'R' + k*'L'
                    stack = []
                elif d == 'R':
                    res += len(stack)*pre
                    stack = ['R'] #append new R
                else:
                    stack.append('.')
                    
        if stack:
            if stack[0] == 'R':
                res += len(stack)*'R'
            else:
                res += len(stack)*'.'
                
        return res

s = Solution()
# Input: ".L.R...LR..L.."
# Output: "LL.RR.LLRRLL.."
dominoes = ".L.R...LR..L.."
print(s.pushDominoes(dominoes))

dominoes = "RR.L"
# Input: "RR.L"
# Output: "RR.L"
print(s.pushDominoes(dominoes))