"""
We define a harmonious array is an array where the difference between its maximum value and its minimum value is exactly 1.

Now, given an integer array, you need to find the length of its longest harmonious subsequence among all its possible subsequences.

Example 1:
Input: [1,3,2,2,5,2,3,7]
Output: 5
Explanation: The longest harmonious subsequence is [3,2,2,2,3].
Note: The length of the input array will not exceed 20,000.
"""
from collections import Counter
class Solution_1:
    def findLHS(self, nums) -> int:
        num_counter = Counter(nums)
        num_unique = sorted(num_counter.keys())
        if len(num_unique) <=1:
            return 0
        # print(num_counter)
        res = 0
        for i in range(1, len(num_unique)):
            p, q = num_unique[i-1], num_unique[i]
            if abs(p-q) == 1:
                res = max(res, num_counter[p]+num_counter[q])
        return res


from collections import Counter
class Solution:
    def findLHS(self, nums) -> int:
        num_counter = Counter(nums)
        res = 0
        for k in num_counter:
            if k+1 in num_counter:
                res = max(res, num_counter[k]+num_counter[k+1])
        return res

s = Solution()
nums = [1,3,2,2,5,2,3,7]
print(s.findLHS(nums))

nums = [1]
print(s.findLHS(nums))

nums = []
print(s.findLHS(nums))

nums = [1,2,3,4]
print(s.findLHS(nums))

nums = [1,1,1,1]
print(s.findLHS(nums))