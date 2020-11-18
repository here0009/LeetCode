"""
Given an integer array arr, in one move you can select a palindromic subarray arr[i], arr[i+1], ..., arr[j] where i <= j, and remove that subarray from the given array. Note that after removing a subarray, the elements on the left and on the right of that subarray move to fill the gap left by the removal.

Return the minimum number of moves needed to remove all numbers from the array.

 

Example 1:

Input: arr = [1,2]
Output: 2
Example 2:

Input: arr = [1,3,4,1,5]
Output: 3
Explanation: Remove [4] then remove [1,3,1] then remove [5].
 

Constraints:

1 <= arr.length <= 100
1 <= arr[i] <= 20

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/palindrome-removal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""



'''
动态规划
dp(s)表示s最少经过多少次删除可以变成一个回文，最后答案就是dp(s) + 1

现在看怎么求dp(s), 看最后一个字符，要么出现在最后剩余的回文中，要么就不在最后剩余的回文中
如果最后一个字符要保留下来，那必然要和前面一个相同的字符位置i配在一起，然后把
中间的一段通过删除变成回文，这样就找到了一个规模更小的子问题，另外因为是最后
一个字符保留了下来，那i位置前面的段只能删掉，前面段删掉需要的删除操作次数
就是dp(s[:i]) + 1, 又是一个子问题，i的位置可能有多个，取总删除次数最少的一个

如果最后一个字符不保留下来，那直接把最后一个字符删掉，然后把s[:-1]变成一个回文
dp[s] = 1 + dp[s[:-1]]

最后dp[s]是两种情况取较小值

'''

# 作者：hao-shou-bu-juan
# 链接：https://leetcode-cn.com/problems/palindrome-removal/solution/python-dong-tai-gui-hua-by-hao-shou-bu-juan-20/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

from typing import List, Tuple
from functools import lru_cache
class Solution:
    # 返回最少经过多少次删除可以让s变成一个回文
    @lru_cache(None)
    def solve(self, s: Tuple[int]):
        if len(s) == 0 or len(s) == 1:
            return 0

        ans = 1 + self.solve(s[:-1])

        ch = s[-1]
        for i in range(len(s)- 1):
            if s[i] == ch:
                if i != 0:
                    ans = min(ans, (1 + self.solve(tuple(s[:i]))) + self.solve(tuple(s[i+1:-1:1])))
                else:
                    ans = min(ans, self.solve(tuple(s[i+1:-1:1])))
        return ans

    def minimumMoves(self, arr: List[int]) -> int:
        return self.solve(tuple(arr)) + 1


# 作者：barry0828
# 链接：https://leetcode-cn.com/problems/palindrome-removal/solution/easy-to-understand-dp-solution-with-detailed-comme/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
class Solution:
    def minimumMoves(self, arr):
        
        # dp[i][j] means the minimum number of moves needed to find palindrome [i,j]
        dp = [[0] * len(arr) for _ in range(len(arr))] # create a 2d dp array to store the solutions 
        
        # solve the two-chars palindrome, if there is only one left in the arr , then the single char has to be a palindrome
        for i in range(len(arr) - 1):
            if arr[i] != arr[i+1]:
                dp[i][i+1] = 1
        
        # create a interval [i,j]
        for l in range(2, len(arr)): #length of the palindrome,l increases and so this is an expanding interval, so the last solution must be dp[i+1][j-1]
            for i in range(len(arr) - l): 
                j = i + l      # left pointer
                tmin = len(arr) #initialize it to the potential max value
                # to find the element k which needs to be removed in order to find the palindrome
                for k in range(i, j):
                    if tmin > dp[i][k] + dp[k+1][j]:
                        tmin = dp[i][k] + dp[k+1][j]
                if arr[i] == arr[j]:#discover one palindrome
                    dp[i][j] = min(dp[i+1][j-1], tmin+1)#compare with last solution and the resulting solution

                else:
                    dp[i][j] = tmin + 1 #if not find, continue to remove elements
       
        return dp[0][len(arr) - 1] + 1
        # dp[0][len(arr) - 1] means the number of moves to iterate through the arr and the "+1" means the move to remove the 1st element of the arr





# 作者：intoloop
# 链接：https://leetcode-cn.com/problems/palindrome-removal/solution/python-dong-tai-gui-hua-by-intoloop-8/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
class Solution:
    def minimumMoves(self, arr: List[int]) -> int:
        n = len(arr)
        @functools.lru_cache(None)
        def dp(i, j):
            if i > j: return 0
            res = 1 + min(dp(i + 1, j), dp(i, j - 1))
            if arr[i] == arr[j]:
                res=min(dp(i + 1, j - 1) if j > i + 2 else 1,res)
            for k in range(i, j):
                if arr[k] == arr[i]:
                    res = min(res, dp(i, k) + dp(k + 1, j))
                elif arr[k] == arr[j]:
                    res = min(res, dp(i, k - 1) + dp(k, j))
            return res

        return dp(0, n - 1)




# 作者：bubbleskye
# 链接：https://leetcode-cn.com/problems/palindrome-removal/solution/python-by-bubbleskye/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
class Solution:
    def minimumMoves(self, arr: List[int]) -> int:
        # dp[i][j]删除arr[i:j+1]这一段所需要进行的操作次数
        # if arr[i]==arr[j]: dp[i][j]=dp[i+1][j-1]
        # else: dp[i][j]=min(dp[i][k]+dp[k+1][j])
        dp=[[float("inf") for _ in range(len(arr))] for _ in range(len(arr))]                
        for j in range(len(arr)):
            for i in range(j,-1,-1):
                if i==j:
                    dp[i][j]=1
                elif i+1==j:
                    dp[i][j]= 1+int(arr[i]!=arr[j])
                else:
                    for k in range(i, j):
                        dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j])
                    if arr[i]==arr[j]:
                        dp[i][j]=min(dp[i][j],dp[i+1][j-1])
        return dp[0][-1]


from functools import lru_cache
class Solution:
    def minimumMoves(self, arr) -> int:
        @lru_cache(None)
        def dp(i,j):
            """
            return the min deletion to delete arr[i:j+1]
            """
            if i > j:
                return 0
            if i == j:
                return 1
            res = 1 + min(dp(i+1,j), dp(i,j-1))
            if arr[i] == arr[j]:
                res = min(res, dp(i+1, j-1) if j-i > 2 else 1)
                # return res
            for k in range(i+1, j):
                if arr[i] == arr[k]:
                    res = min(res, dp(i, k) + dp(k+1, j))
                elif arr[j] == arr[k]:
                    res = min(res, dp(i, k-1) + dp(k, j))
            return res

        return dp(0, len(arr)-1)

class Solution:
    def minimumMoves(self, arr) -> int:
        @lru_cache(None)
        def dp(i,j):
            """
            return how many deletions makes arr[i:j+1] a palindrome
            """
            if j-i < 1:
                return 0
            res = 1 + dp(i, j-1)
            letter = arr[j]
            if arr[i] == letter:
                res = min(res, dp(i+1, j-1))
            for k in range(i+1, j):
                if arr[k] == letter:
                    res = min(res, 1+dp(i, k-1)+dp(k+1, j-1)) # plus one for delete arr[k] ~ arr[j]
            return res

        return dp(0, len(arr)-1)+1

S = Solution()
arr = [1,2]
print(S.minimumMoves(arr))
arr = [1,3,4,1,5]
print(S.minimumMoves(arr))
arr = [16,13,13,10,12]
print(S.minimumMoves(arr))
# 输出：
# 3
# 预期结果：
# 4
arr = [1,4,1,1,2,3,2,1]
print(S.minimumMoves(arr))
# 输出：
# 3
# 预期结果：
# 2

class Solution:
    def minimumMoves(self, arr: List[int]) -> int:
        n=len(arr)
        dp=[[1 for i in range(n)] for j in range(n)]#dp[k][k]=1
        val_idx={}
        for gap in range(1,n):
            for i in range(n):
                if i+gap>=n:
                    break
                j=i+gap
                dp[i][j]=float('inf') if arr[i]!=arr[j] else dp[i+1][j-1]
                for k in range(i,j):
                    if arr[i]==arr[k]:#k可以解释为分割位置
                        dp[i][j]=min(dp[i][j],dp[i][k]+dp[k+1][j])
        return dp[0][n-1]


class Solution:
    def minimumMoves(self, arr: List[int]) -> int:
        from functools import lru_cache
        @lru_cache(None)
        def F(s, e):
            if e <= s:
                return 0
            if e - s <= 2 and arr[s] == arr[e - 1]:
                return 1
            res = e - s
            for i in range(s, e)[::-1]:
                if arr[s] == arr[i]:
                    res = min(res, max(1, F(s + 1, i)) + F(i + 1, e))
            return res
        return F(0, len(arr))