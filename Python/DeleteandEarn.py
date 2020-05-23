"""
Given an array nums of integers, you can perform operations on the array.

In each operation, you pick any nums[i] and delete it to earn nums[i] points. After, you must delete every element equal to nums[i] - 1 or nums[i] + 1.

You start with 0 points. Return the maximum number of points you can earn by applying such operations.

Example 1:

Input: nums = [3, 4, 2]
Output: 6
Explanation: 
Delete 4 to earn 4 points, consequently 3 is also deleted.
Then, delete 2 to earn 2 points. 6 total points are earned.
 

Example 2:

Input: nums = [2, 2, 3, 3, 3, 4]
Output: 9
Explanation: 
Delete 3 to earn 3 points, deleting both 2's and the 4.
Then, delete 3 again to earn 3 points, and 3 again to earn 3 points.
9 total points are earned.
 

Note:

The length of nums is at most 20000.
Each element nums[i] is an integer in the range [1, 10000].
"""
class Solution:
    def deleteAndEarn(self, nums) -> int:
        """
        wrong answer, there can be lots of num meet the requirments between 2 nums
        """
        odds = 0
        even = 0
        for num in nums:
            if num % 2:
                odds += num
            else:
                even += num
        return max(odds, even)

from collections import Counter
class Solution:
    def deleteAndEarn(self, nums) -> int:
        num_counter = Counter(nums)
        using_num, no_using_num = 0, 0
        pre = -1
        for num in sorted(num_counter):
            if num == pre+1:
                no_using_num, using_num = max(no_using_num, using_num), no_using_num + num*num_counter[num]
            else:
                no_using_num, using_num = max(no_using_num, using_num), num*num_counter[num] + max(no_using_num, using_num)
            # print(using_num, no_using_num)
            pre = num
        return max(using_num, no_using_num)

s = Solution()
nums = [3, 4, 2]
print(s.deleteAndEarn(nums))
nums = [2, 2, 3, 3, 3, 4]
print(s.deleteAndEarn(nums))
nums = [8,10,4,9,1,3,5,9,4,10]
print(s.deleteAndEarn(nums))