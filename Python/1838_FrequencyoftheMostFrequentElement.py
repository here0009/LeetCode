"""
The frequency of an element is the number of times it occurs in an array.

You are given an integer array nums and an integer k. In one operation, you can choose an index of nums and increment the element at that index by 1.

Return the maximum possible frequency of an element after performing at most k operations.

 

Example 1:

Input: nums = [1,2,4], k = 5
Output: 3
Explanation: Increment the first element three times and the second element two times to make nums = [4,4,4].
4 has a frequency of 3.
Example 2:

Input: nums = [1,4,8,13], k = 5
Output: 2
Explanation: There are multiple optimal solutions:
- Increment the first element three times to make nums = [4,4,8,13]. 4 has a frequency of 2.
- Increment the second element four times to make nums = [1,8,8,13]. 8 has a frequency of 2.
- Increment the third element five times to make nums = [1,4,13,13]. 13 has a frequency of 2.
Example 3:

Input: nums = [3,9,6], k = 2
Output: 1
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 105
1 <= k <= 105
"""


from typing import List
from collections import deque
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:

        nums.sort()
        curr, res = 1, 1
        tmp = 0
        diff = [nums[i] - nums[i - 1] for i in range(1, len(nums))]
        print(diff)
        dq = deque([])
        for d in diff:
            while dq and tmp + d * curr > k:
                tmp -= dq.popleft()
                curr -= 1
            tmp += d * curr
            dq.append(d)
            curr += 1
            res = max(res, curr)
        return res


from typing import List
from collections import deque
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        res, curr = 0, 0
        dq = deque([])
        for num in nums:
            diff = 0 if not dq else num - dq[-1]
            curr += diff * len(dq)
            dq.append(num)
            while dq and curr > k:
                curr -= num - dq.popleft()
            res = max(res, len(dq))
        return res


from typing import List
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        left, right = 0, 1
        curr, res = 0, 0
        while right < len(nums):
            curr += (nums[right] - nums[right - 1]) * (right - left)
            while curr > k:
                curr -= nums[right] - nums[left]
                left += 1
            res = max(res, right - left + 1)
            right += 1
        return res


S = Solution()
nums = [1,2,4]
k = 5
print(S.maxFrequency(nums, k))
nums = [1,4,8,13]
k = 5
print(S.maxFrequency(nums, k))
nums = [3,9,6]
k = 2
print(S.maxFrequency(nums, k))
nums = [9930,9923,9983,9997,9934,9952,9945,9914,9985,9982,9970,9932,9985,9902,9975,9990,9922,9990,9994,9937,9996,9964,9943,9963,9911,9925,9935,9945,9933,9916,9930,9938,10000,9916,9911,9959,9957,9907,9913,9916,9993,9930,9975,9924,9988,9923,9910,9925,9977,9981,9927,9930,9927,9925,9923,9904,9928,9928,9986,9903,9985,9954,9938,9911,9952,9974,9926,9920,9972,9983,9973,9917,9995,9973,9977,9947,9936,9975,9954,9932,9964,9972,9935,9946,9966]
k = 3056
print(S.maxFrequency(nums, k))
# 输出：
# 72
# 预期：
# 73