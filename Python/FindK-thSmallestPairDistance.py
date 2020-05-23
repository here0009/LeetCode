"""
Given an integer array, return the k-th smallest distance among all the pairs. The distance of a pair (A, B) is defined as the absolute difference between A and B.

Example 1:
Input:
nums = [1,3,1]
k = 1
Output: 0 
Explanation:
Here are all the pairs:
(1,3) -> 2
(1,1) -> 0
(3,1) -> 2
Then the 1st smallest distance pair is (1,1), and its distance is 0.
Note:
2 <= len(nums) <= 10000.
0 <= nums[i] < 1000000.
1 <= k <= len(nums) * (len(nums) - 1) / 2.
"""
class Solution:
    def smallestDistancePair(self, nums, k: int) -> int:
        """
        TLE
        """
        n = len(nums)
        nums = sorted(nums)
        lo, hi = 0, nums[-1]-nums[0]
        res = 0
        while lo < hi:
            mid = (lo+hi)//2
            counts = 0
            for i in range(n-1):
                j = n-1
                while nums[j]-nums[i] > mid:
                    j -= 1
                counts += j-i
                if counts >= k: #already statisfy, try to minimize mid
                    break
            if counts < k:
                lo = mid+1
            else:
                hi = mid
        return lo


class Solution_1:
    def smallestDistancePair(self, nums, k):
        def possible(guess):
            #Is there k or more pairs with distance <= guess?
            count = left = 0
            for right, x in enumerate(nums):
                while x - nums[left] > guess: #if nums[i]-nums[left] > guess, nums[i+1]-nums[left] is also > guess
                    left += 1 
                count += right - left
            return count >= k

        nums.sort()
        lo = 0
        hi = nums[-1] - nums[0]
        while lo < hi:
            mi = (lo + hi) // 2
            if possible(mi):
                hi = mi
            else:
                lo = mi + 1

        return lo

class Solution:
    def smallestDistancePair(self, nums, k: int) -> int:
        n = len(nums)
        nums = sorted(nums)
        lo, hi = 0, nums[-1]-nums[0]
        res = 0
        while lo < hi:
            mid = (lo+hi)//2
            left,counts = 0,0
            for right in range(n):
                while nums[right]-nums[left] > mid:
                    left += 1
                counts += right -left #the counts of nums[right]-nums[left] <= mid
                if counts >= k: #already statisfy, try to minimize mid
                    break
            if counts < k:
                lo = mid+1
            else:
                hi = mid
        return lo

class Solution:
    def smallestDistancePair(self, nums, k: int) -> int:
        n = len(nums)
        nums = sorted(nums)
        lo, hi = 0, nums[-1]-nums[0]
        res = 0
        while lo < hi:
            mid = (lo+hi)//2
            right,counts = 0,0
            for left in range(n):
                while right < n and nums[right]-nums[left] <= mid:
                    right += 1
                counts += right -left-1 #the counts of nums[right]-nums[left] <= mid
            if counts < k:
                lo = mid+1
            else:
                hi = mid
        return lo


S = Solution()
nums = [1,3,1]
k = 1
print(S.smallestDistancePair(nums,k))

nums = [1,6,1]
k = 3
print(S.smallestDistancePair(nums,k))

nums = [1,1,1]
k = 2
print(S.smallestDistancePair(nums,k))

nums = [9,10,7,10,6,1,5,4,9,8]
k = 18
print(S.smallestDistancePair(nums,k))
# Output
# 9
# Expected
# 2