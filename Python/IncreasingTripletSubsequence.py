"""
Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.

Formally the function should:

Return true if there exists i, j, k 
such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 else return false.
Note: Your algorithm should run in O(n) time complexity and O(1) space complexity.

Example 1:

Input: [1,2,3,4,5]
Output: true
Example 2:

Input: [5,4,3,2,1]
Output: false
"""
class Solution:
    def increasingTriplet(self, nums) -> bool:
        if len(nums) < 3:
            return False
        incrs = [nums[0]]
        for num in nums[1:]:
            # print(incrs)
            if num > incrs[-1]:
                incrs.append(num)
            else:
                index = len(incrs)-1
                while index >= 0 and num <= incrs[index]:
                    index -= 1
                incrs[index+1] = num
            if len(incrs) > 2:
                return True
        return False

class Solution:
    def increasingTriplet(self, nums) -> bool:
        first = second = float('inf')
        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            else:
                return True
        return False

s = Solution()
# nums = [1,2,3,4,5]
# print(s.increasingTriplet(nums))
# nums = [5,4,3,2,1]
# print(s.increasingTriplet(nums))

# nums = []
# print(s.increasingTriplet(nums))

nums = [2,5,2,3,4,5]
print(s.increasingTriplet(nums))
