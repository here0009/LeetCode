"""
Given an array of integers nums and an integer k. A subarray is called nice if there are k odd numbers on it.

Return the number of nice sub-arrays.

 

Example 1:

Input: nums = [1,1,2,1,1], k = 3
Output: 2
Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].
Example 2:

Input: nums = [2,4,6], k = 1
Output: 0
Explanation: There is no odd numbers in the array.
Example 3:

Input: nums = [2,2,2,1,2,2,1,2,2,2], k = 2
Output: 16
 

Constraints:

1 <= nums.length <= 50000
1 <= nums[i] <= 10^5
1 <= k <= nums.length
"""
from collections import deque
class Solution:
    def numberOfSubarrays(self, nums, k: int) -> int:
        dq = deque()
        odd = 0
        index = 0
        res = 0
        counts = []

        # print('nums',nums)
        while index < len(nums):
            left, right = 0, 0
            while odd < k and index < len(nums):
                n = nums[index]
                dq.append(n)
                index += 1
                if n % 2 == 1:
                    odd += 1
            if odd == k:
                right += 1
                while index < len(nums) and nums[index]%2 == 0:
                    dq.append(nums[index])
                    right += 1
                    index += 1
                # print(dq)
                while len(dq) > 0 :
                    n = dq.popleft()
                    left += 1
                    if n % 2 == 1:
                        odd -= 1
                        break
                res += left*right

        return res

s = Solution()
nums = [1,1,2,1,1]
k = 3
print(s.numberOfSubarrays(nums, k))

nums = [2,4,6]
k = 1
print(s.numberOfSubarrays(nums, k))

nums = [2,2,2,1,2,2,1,2,2,2]
k = 2
print(s.numberOfSubarrays(nums, k))

nums = [45627,50891,94884,11286,35337,46414,62029,20247,72789,89158,54203,79628,25920,16832,47469,80909]
k = 1
print(s.numberOfSubarrays(nums, k))
