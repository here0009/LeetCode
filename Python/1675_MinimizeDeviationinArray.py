"""
You are given an array nums of n positive integers.

You can perform two types of operations on any element of the array any number of times:

If the element is even, divide it by 2.
For example, if the array is [1,2,3,4], then you can do this operation on the last element, and the array will be [1,2,3,2].
If the element is odd, multiply it by 2.
For example, if the array is [1,2,3,4], then you can do this operation on the first element, and the array will be [2,2,3,4].
The deviation of the array is the maximum difference between any two elements in the array.

Return the minimum deviation the array can have after performing some number of operations.

 

Example 1:

Input: nums = [1,2,3,4]
Output: 1
Explanation: You can transform the array to [1,2,3,2], then to [2,2,3,2], then the deviation will be 3 - 2 = 1.
Example 2:

Input: nums = [4,1,5,20,3]
Output: 3
Explanation: You can transform the array after two operations to [4,2,5,5,3], then the deviation will be 5 - 2 = 3.
Example 3:

Input: nums = [2,10,8]
Output: 3
 

Constraints:

n == nums.length
2 <= n <= 105
1 <= nums[i] <= 109
"""


import heapq
from typing import List
class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        """

        """
        def geBound(num):
            """
            return the lower and upper bound of num
            """
            if num % 2 == 1:
                return (num, num*2)
            else:
                return (num //(num & -num), num)

        pq = []
        for num in nums:
            pq.append(geBound(num))
        heapq.heapify(pq)
        max_v = max([v for v, _ in pq])
        res = max_v - pq[0][0]
        while (pq[0][0] < pq[0][1]):  # we can still try to enlarge the min value
            min_v, bound = heapq.heappop(pq)
            min_v *= 2
            max_v = max(max_v, min_v)
            heapq.heappush(pq, (min_v, bound))
            res = min(res, max_v - pq[0][0])
        return res

S = Solution()
nums = [1,2,3,4]
print(S.minimumDeviation(nums))
nums = [4,1,5,20,3]
print(S.minimumDeviation(nums))
nums = [2,10,8]
print(S.minimumDeviation(nums))