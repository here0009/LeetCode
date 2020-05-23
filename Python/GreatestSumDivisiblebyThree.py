"""
Given an array nums of integers, we need to find the maximum possible sum of elements of the array such that it is divisible by three.

 

Example 1:

Input: nums = [3,6,5,1,8]
Output: 18
Explanation: Pick numbers 3, 6, 1 and 8 their sum is 18 (maximum sum divisible by 3).
Example 2:

Input: nums = [4]
Output: 0
Explanation: Since 4 is not divisible by 3, do not pick any number.
Example 3:

Input: nums = [1,2,3,4,4]
Output: 12
Explanation: Pick numbers 1, 3, 4 and 4 their sum is 12 (maximum sum divisible by 3).
 

Constraints:

1 <= nums.length <= 4 * 10^4
1 <= nums[i] <= 10^4
"""
from collections import defaultdict
class Solution:
    def maxSumDivThree(self, nums) -> int:
        remains_dict = defaultdict(list)
        for n in nums:
            r = n%3
            remains_dict[r].append(n)
        for key in remains_dict:
            remains_dict[key] = sorted(remains_dict[key])
        total = sum(nums)
        total_r = total%3
        print(total, total_r)
        if total_r == 1:
            minus_num = float('inf')
            if len(remains_dict[1])>0:
                minus_num = remains_dict[1][0]
            if len(remains_dict[2])>1:
                minus_num = min(minus_num, remains_dict[2][0]+remains_dict[2][1])
            total -= minus_num
        elif total_r == 2:
            minus_num = float('inf')
            if len(remains_dict[1])>1:
                minus_num = remains_dict[1][0]+remains_dict[1][1]
            if len(remains_dict[2])>0:
                # print('K')
                minus_num = min(minus_num, remains_dict[2][0])
            # print(minus_num)
            total -= minus_num
        # print(remains_dict)
        return total

s = Solution()
# nums = [3,6,5,1,8]
# print(s.maxSumDivThree(nums))

# nums = [4]
# print(s.maxSumDivThree(nums))

# nums = [1,2,3,4,4]
# print(s.maxSumDivThree(nums))

nums = [2,6,2,2,7]
print(s.maxSumDivThree(nums))