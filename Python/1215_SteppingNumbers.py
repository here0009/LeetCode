"""
A Stepping Number is an integer such that all of its adjacent digits have an absolute difference of exactly 1. For example, 321 is a Stepping Number while 421 is not.

Given two integers low and high, find and return a sorted list of all the Stepping Numbers in the range [low, high] inclusive.

 

Example 1:

Input: low = 0, high = 21
Output: [0,1,2,3,4,5,6,7,8,9,10,12,21]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/stepping-numbers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution:
    def countSteppingNumbers(self, low: int, high: int):
        def dfs(n):
            if n > high:
                return
            if n >= low:
                self.res.add(n)
            d = n%10
            # print(n, d)
            if d != 0:
                dfs(n*10+d-1)
            if d != 9:
                dfs(n*10+d+1)

        self.res = set()
        if low == 0:
            self.res.add(0)
        for i in range(1, 10):
            dfs(i)
        return sorted(list(self.res))


S = Solution()
low = 0
high = 21
print(S.countSteppingNumbers(low, high))

low =0
high = 1000
print(S.countSteppingNumbers(low, high))
