"""
Given an array consisting of n integers, find the contiguous subarray whose length is greater than or equal to k that has the maximum average value. And you need to output the maximum average value.

Example 1:
Input: [1,12,-5,-6,50,3], k = 4
Output: 12.75
Explanation:
when length is 5, maximum average value is 10.8,
when length is 6, maximum average value is 9.16667.
Thus return 12.75.
Note:
1 <= k <= n <= 10,000.
Elements of the given array will be in range [-10,000, 10,000].
The answer with the calculation error less than 10-5 will be accepted.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-average-subarray-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


from collections import defaultdict
class Solution:
    def findMaxAverage(self, nums, k: int) -> float:
        """
        TLE
        """
        preSum = [0]
        for num in nums:
            preSum.append(preSum[-1] + num)
        length = len(nums)
        # print(preSum)
        dp = defaultdict(lambda :float('-inf'))
        for d in range(k, length+1):
            for i in range(length-d+1):
                dp[d] = max(dp[d], preSum[i+d] - preSum[i])
        # print(dp)
        return max(v/k for k,v in dp.items())

'''
二分法找平均数的可能值，如果选择了一个平均值之后，序列中所有数值减去这个待选平均值之后，
有长度大于等于k的子数组和是大于0的，说明待选值偏小，反之偏大
'''
# 作者：hao-shou-bu-juan
# 链接：https://leetcode-cn.com/problems/maximum-average-subarray-ii/solution/python-er-fen-cha-zhao-ping-jun-zhi-by-hao-shou-bu/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        def check(avg):
            data = [val-avg for val in nums]
            n = len(data)

            prefix_sum = [0 for _ in range(n)]
            prefix_sum[0] = data[0]
            for i in range(1, n):
                prefix_sum[i] = data[i] + prefix_sum[i-1]

            min_prefix_sum = [0 for _ in range(n)]
            min_prefix_sum[0] = min(0, prefix_sum[0])
            for i in range(1, n):
                min_prefix_sum[i] = min(prefix_sum[i], min_prefix_sum[i-1])

            ans = prefix_sum[k-1]
            for end in range(k, n):
                ans = max(ans, prefix_sum[end] - min_prefix_sum[end - k])

            return ans

        l, r = min(nums), max(nums)
        while abs(l - r) >= 10 ** -4:
            #print(l, r)

            mid = l + (r-l) / 2
            if check(mid) > 0:
                l = mid
            else:
                r = mid

        return l


# 作者：zWang64
# 链接：https://leetcode-cn.com/problems/maximum-average-subarray-ii/solution/python3xiang-jie-ji-bai-100-by-zwang64/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float: 
        def check(avg):
            # 如果是求长度等于 k 的区间的区间和：
            # 使用滑动窗口，维护首尾前缀和（见643.最大平均子段和）
            # 这一题是大于等于 k
            # 我们需要知道以 end 结尾，长度大于等于 k 的区间中最大的区间和
            # 多维护一个 start_sum 的最小值即可
            # end_sum - min_sum 即为所求区间和最大值 
            end_sum = sum(num - avg for num in nums[:k])
            start_sum = min_start_sum = 0
            for end in range(k, len(nums)):
                if end_sum >= min_start_sum:
                    return True
                end_sum += nums[end] - avg
                start_sum += nums[end-k] - avg
                min_start_sum = min(min_start_sum, start_sum)
            return end_sum >= min_start_sum 
        # 二分法
        l, r = min(nums), max(nums)
        while r - l > 1e-5:
            mid = (l+r) / 2
            if check(mid):  # 存在符合条件的区间，其平均值大于等于 mid，下界向上收缩
                l = mid 
            else:
                r = mid 
        return l


class Solution:
    def findMaxAverage(self, nums, k: int) -> float:
        def check(avg):
            nums2 = [num - avg for num in nums]
            curr = sum(nums2[:k])
            if curr >= 0:
                return True
            preSum, minPreSum = 0, 0
            for end in range(k, length):
                preSum += nums2[end-k]
                minPreSum = min(minPreSum, preSum)
                curr += nums2[end]
                if curr - minPreSum >= 0:
                    return True
            return False

        length = len(nums)
        left, right = min(nums), max(nums)
        while right - left >= 1e-5:
            mid = (left + right)/2
            if check(mid):
                left = mid
            else:
                right = mid
        return left


S = Solution()
nums = [1,12,-5,-6,50,3]
k = 4
print(S.findMaxAverage(nums, k))