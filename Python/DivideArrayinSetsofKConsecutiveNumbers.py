"""
Given an array of integers nums and a positive integer k, find whether it's possible to divide this array into sets of k consecutive numbers
Return True if its possible otherwise return False.

 

Example 1:

Input: nums = [1,2,3,3,4,4,5,6], k = 4
Output: true
Explanation: Array can be divided into [1,2,3,4] and [3,4,5,6].
Example 2:

Input: nums = [3,2,1,2,3,4,3,4,5,9,10,11], k = 3
Output: true
Explanation: Array can be divided into [1,2,3] , [2,3,4] , [3,4,5] and [9,10,11].
Example 3:

Input: nums = [3,3,2,2,1,1], k = 3
Output: true
Example 4:

Input: nums = [1,2,3,4], k = 3
Output: false
Explanation: Each array should be divided in subarrays of size 3.
 

Constraints:

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^9
1 <= k <= nums.length
"""
from collections import Counter
class Solution:
    def isPossibleDivide(self, nums, k: int) -> bool:
        length = len(nums)
        nums_counts = Counter(nums)
        if length % k != 0:
            return False
        keys = sorted(nums_counts.keys())
        min_v_index = 0
        counts = 0
        len_keys = len(keys)
        # print(keys)
        # print(nums_counts)
        while counts < length:
            while min_v_index < len_keys and nums_counts[keys[min_v_index]] <= 0:
                min_v_index += 1
            tmp_v = keys[min_v_index]
            # print(tmp_v)
            for i in range(k):
                if tmp_v in nums_counts and  nums_counts[tmp_v] > 0:
                    nums_counts[tmp_v] -= 1
                    tmp_v += 1
                    counts += 1
                else:
                    # print(tmp_v, nums_counts[tmp_v])
                    return False

        return True

from collections import Counter
class Solution:
    def isPossibleDivide(self, nums, k: int) -> bool:
        counts = Counter(nums)
        keys = sorted(counts.keys())
        for n in keys:
            if counts[n] > 0:
                v = counts[n]
                for i in range(n,n+k):
                    if i not in counts or counts[i] < v:
                        return False
                    counts[i] -= v
        return True


s = Solution()
nums = [1,2,3,3,4,4,5,6]
k = 4
print(s.isPossibleDivide(nums,k))

# nums = [3,2,1,2,3,4,3,4,5,9,10,11]
# k = 3
print(s.isPossibleDivide(nums,k))

nums = [3,3,2,2,1,1]
k = 3
print(s.isPossibleDivide(nums,k))


nums = [1,2,3,4]
k = 3
print(s.isPossibleDivide(nums,k))


nums = [5,6,7,8,9,6,7,8,9,10,11,12,13,14,15,12,13,14,15,19]
k = 5
print(s.isPossibleDivide(nums,k))
"""
Output:
true
Expected:
false
"""