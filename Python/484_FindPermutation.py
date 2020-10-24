"""
By now, you are given a secret signature consisting of character 'D' and 'I'. 'D' represents a decreasing relationship between two numbers, 'I' represents an increasing relationship between two numbers. And our secret signature was constructed by a special integer array, which contains uniquely all the different number from 1 to n (n is the length of the secret signature plus 1). For example, the secret signature "DI" can be constructed by array [2,1,3] or [3,1,2], but won't be constructed by array [3,2,4] or [2,1,3,4], which are both illegal constructing special string that can't represent the "DI" secret signature.

On the other hand, now your job is to find the lexicographically smallest permutation of [1, 2, ... n] could refer to the given secret signature in the input.

Example 1:
Input: "I"
Output: [1,2]
Explanation: [1,2] is the only legal initial spectial string can construct secret signature "I", where the number 1 and 2 construct an increasing relationship.
Example 2:
Input: "DI"
Output: [2,1,3]
Explanation: Both [2,1,3] and [3,1,2] can construct the secret signature "DI", 
but since we want to find the one with the smallest lexicographical permutation, you need to output [2,1,3]
Note:

The input string will only contain the character 'D' and 'I'.
The length of input string is a positive integer and will not exceed 10,000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-permutation
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def findPermutation(self, s: str):
        n = len(s) + 1
        vals = list(range(1, n+1))
        index = 0
        stack = []
        res = []
        s += 'I'
        for c in s:
            if c == 'I':
                res.append(vals[index])
                res.extend(stack[::-1])
                stack = []
            elif c == 'D':
                stack.append(vals[index])
            index += 1
        res.extend(stack[::-1])
        return res

class Solution:
    def findPermutation(self, s: str):
        v = 1
        stack = []
        res = []
        s += 'I'
        for c in s:
            if c == 'I':
                res.append(v)
                res.extend(stack[::-1])
                stack = []
            elif c == 'D':
                stack.append(v)
            v += 1
        res.extend(stack[::-1])
        return res

class Solution_1:
    def findPermutation(self, s: str):
        """
        two pointers, remeber the values need to be reversed (when meet D)
        wrong answer
        """
        pre = 'D'
        res = []
        i, j = 1, 2
        for c in s:
            if c == 'I':
                if pre == 'D': # pre is D or the 1st I
                    res.extend(list(range(i,j))[::-1])
                i = j
                j += 1
                res.append(i)
            elif c == 'D':
                j += 1
            pre = c
            print(c, res)
        return res

S = Solution()
s = 'II'
print(S.findPermutation(s))
s = 'DI'
print(S.findPermutation(s))
s = 'ID'
print(S.findPermutation(s))
s = 'DDDI'
print(S.findPermutation(s))
s = ''
print(S.findPermutation(s))
s = "DDIIDI"
print(S.findPermutation(s))