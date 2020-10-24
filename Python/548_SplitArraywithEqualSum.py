"""
Given an array with n integers, you need to find if there are triplets (i, j, k) which satisfies following conditions:

0 < i, i + 1 < j, j + 1 < k < n - 1
Sum of subarrays (0, i - 1), (i + 1, j - 1), (j + 1, k - 1) and (k + 1, n - 1) should be equal.
where we define that subarray (L, R) represents a slice of the original array starting from the element indexed L to the element indexed R.
Example:
Input: [1,2,1,2,1,2,1]
Output: True
Explanation:
i = 1, j = 3, k = 5. 
sum(0, i - 1) = sum(0, 0) = 1
sum(i + 1, j - 1) = sum(2, 2) = 1
sum(j + 1, k - 1) = sum(4, 4) = 1
sum(k + 1, n - 1) = sum(6, 6) = 1
Note:
1 <= n <= 2000.
Elements in the given array will be in range [-1,000,000, 1,000,000].

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/split-array-with-equal-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def splitArray(self, nums) -> bool:
        n = len(nums)
        if n < 7:
            return False
        
        presum = [0 for _ in range(n+1)]
        for i in range(n):
            presum[i+1] = presum[i]+nums[i]
            
        def binarySplit(l, r):
            s = set()
            for i in range(l+1, r-1):
                if presum[r]-presum[i+1]==presum[i]-presum[l]:
                    s.add(presum[i]-presum[l])
            return s
        
        max_diff = max(nums)-min(nums)
        for i in range(1, n-1):
            if abs((presum[n] -presum[i+1] )-(presum[i]-presum[0]))>max_diff:
                continue
            left = binarySplit(0, i)
            right = binarySplit(i+1, n)
            if len(left & right) > 0:
                return True
        return False


class Solution:
    def splitArray(self, nums) -> bool:
        def delteOneSum(i, j):
            """
            split nums[i:j] to two halves, if left_sum == right_sum, add the sum to res, return all possible sums
            """
            res = set()
            if j - i < 3:
                return res
            for k in range(i+1, j-1):
                left = preSum[k] - preSum[i]
                right = preSum[j] - preSum[k+1]
                if left == right:
                    res.add(left)
            return res

        length = len(nums)
        max_diff = max(nums) - min(nums)
        if length < 7:
            return False
        preSum = [0]
        for num in nums:
            preSum.append(preSum[-1]+num)

        for k in range(3, length-3):
            left_total = preSum[k] - preSum[0]
            right_total = preSum[length] - preSum[k+1]
            if abs(left_total - right_total) > max_diff:
                continue
            left_sums = delteOneSum(0, k)
            right_sums = delteOneSum(k+1, length)
            # print(left_sums, right_sums, left_total, right_total)
            if left_sums & right_sums:
                return True
        return False



S = Solution()
nums = [1,2,1,2,1,2,1]
print(S.splitArray(nums))
