"""
You are given a 0-indexed integer array nums consisting of n non-negative integers.

You are also given an array queries, where queries[i] = [xi, yi]. The answer to the ith query is the sum of all nums[j] where xi <= j < n and (j - xi) is divisible by yi.

Return an array answer where answer.length == queries.length and answer[i] is the answer to the ith query modulo 109 + 7.

 

Example 1:

Input: nums = [0,1,2,3,4,5,6,7], queries = [[0,3],[5,1],[4,2]]
Output: [9,18,10]
Explanation: The answers of the queries are as follows:
1) The j indices that satisfy this query are 0, 3, and 6. nums[0] + nums[3] + nums[6] = 9
2) The j indices that satisfy this query are 5, 6, and 7. nums[5] + nums[6] + nums[7] = 18
3) The j indices that satisfy this query are 4 and 6. nums[4] + nums[6] = 10
Example 2:

Input: nums = [100,200,101,201,102,202,103,203], queries = [[0,7]]
Output: [303]
 

Constraints:

n == nums.length
1 <= n <= 5 * 104
0 <= nums[i] <= 109
1 <= queries.length <= 1.5 * 105
0 <= xi < n
1 <= yi <= 5 * 104

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sum-of-special-evenly-spaced-elements-in-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


from typing import List
class Solution:
    """
    TLE
    """
    def solve(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        res = []
        len_n = len(nums)
        preSum = [0]
        for num in nums:
            preSum.append(preSum[-1] + num)
        M = 10**9 + 7
        for x, y in queries:
            tmp = 0
            if y == 1:
                tmp = preSum[-1] - preSum[x]
            else:
                for k in range(x, len_n, y):
                    tmp += nums[k]
            res.append(tmp % M)
        return res

# https://leetcode-cn.com/problems/sum-of-special-evenly-spaced-elements-in-array/solution/gen-ju-ti-shi-lai-by-goldfish_hcy-7ykz/
from typing import List
from math import floor, sqrt
class Solution:
    def solve(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        M = 10**9 + 7
        sqrt_n = floor(sqrt(n))
        preSum = [[0] * n for _ in range(sqrt_n + 1)]
        for i in range(1, sqrt_n + 1):
            for j in range(n - 1, n - i - 1, -1):
                preSum[i][j] = nums[j]
            for j in range(n - i - 1, -1, -1):
                preSum[i][j] = preSum[i][i + j] + nums[j]
        res = []
        for x, y in queries:
            tmp = 0
            if y < sqrt_n:
                tmp = preSum[y][x]
            else:
                for k in range(x, n, y):
                    tmp += nums[k]
            res.append(tmp % M)
        return res



S = Solution()
nums = [0,1,2,3,4,5,6,7]
queries = [[0,3],[5,1],[4,2]]
print(S.solve(nums, queries))
nums = [100,200,101,201,102,202,103,203]
queries = [[0,7]]
print(S.solve(nums, queries))
nums = [1123,9873123,83745634,78649234,872842342,234239847]
queries = [[0,1],[3,4],[3,2]]
print(S.solve(nums, queries))
# 输出：
# [279351296,872842342,872842342]
# 预期结果：
# [279351296,78649234,312889081]