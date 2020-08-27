"""
Given a string that contains only digits 0-9 and a target value, return all possibilities to add binary operators (not unary) +, -, or * between the digits so they evaluate to the target value.

Example 1:

Input: num = "123", target = 6
Output: ["1+2+3", "1*2*3"] 
Example 2:

Input: num = "232", target = 8
Output: ["2*3+2", "2+3*2"]
Example 3:

Input: num = "105", target = 5
Output: ["1*0+5","10-5"]
Example 4:

Input: num = "00", target = 0
Output: ["0+0", "0-0", "0*0"]
Example 5:

Input: num = "3456237490", target = 9191
Output: []
 

Constraints:

0 <= num.length <= 10
num only contain digits.
"""


class Solution:
    def addOperators(self, num: str, target: int):
        def dfs(index, total, last, path):
            if index == length:
                if total == target:
                    res.append(path)
                    return
            for j in range(index, length):
                n = int(num[index:j+1])
                if index == 0:
                    dfs(j+1, n, n, str(n))
                else:
                    dfs(j+1, total+n, n, path+'+'+str(n))
                    dfs(j+1, total-n, -n, path+'-'+str(n))
                    dfs(j+1, total-last+last*n, last*n, path+'*'+str(n))
                if n == 0:
                    break
        
        length = len(num)
        res = []
        dfs(0, 0, 0, '')
        return res

S = Solution()
num = "123"
target = 6
print(S.addOperators(num, target))
num = "232"
target = 8
print(S.addOperators(num, target))
num = "105"
target = 5
print(S.addOperators(num, target))
num = "00"
target = 0
print(S.addOperators(num, target))
num = "3456237490"
target = 9191
print(S.addOperators(num, target))

