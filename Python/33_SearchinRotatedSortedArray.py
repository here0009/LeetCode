"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
"""

from typing import List
class Solution:
    def search(self, nums, target: int) -> int:
        left, right = 0, len(nums)-1
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        while left < right:
            mid = (left + right) //2
            # print(left, right, mid)
            for i in (left, right, mid):
                if nums[i] == target:
                    return i
            if nums[mid] > target:
                if nums[left] < nums[right]:
                    right = mid - 1
                else:
                    left = mid + 1 
            elif nums[mid] < target:
                if nums[left] < nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1

# https://leetcode.com/problems/search-in-rotated-sorted-array/discuss/14419/Pretty-short-C%2B%2BJavaRubyPython
class Solution(object):
   def search(self, nums, target):
       lo, hi = 0, len(nums) - 1
       while lo <= hi:
           mid = (lo+hi) // 2
           if nums[mid] == target:
               return mid
           if nums[0] <= target < nums[mid] or target < nums[mid] < nums[0] or nums[mid] < nums[0] <= target:
               hi = mid - 1
           else:
               lo = mid + 1
       return -1

# https://leetcode.com/problems/search-in-rotated-sorted-array/discuss/14437/Python-binary-search-solution-O(logn)-48ms
class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            # if found target value, return the index
            if nums[mid] == target:
                return mid
            
            # determine it's left rotated or right rotated
            """
            No rotated:
            1 2 3 4 5 6 7
                 mid
                 
            left rotated: pivot at the left side of the origin sorted array, A[mid] >= A[left]
            3 4 5 6 7 1 2
                 mid
            search in A[left] ~ A [mid] if A[left] <= target < A[mid] else, search right side
            
            right rotated: pivot at the right side of the origin sorted array, A[mid] < A[left]
            6 7 1 2 3 4 5
                 mid          
            search in A[mid] ~ A[right] if A[mid] < target <= A[right] else, search left side
            """
            if nums[mid] >= nums[left]: # left rotated
                # in ascending order side
                if nums[left] <= target  < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else: # right rotated
                # in ascending order side
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        # cannot find the target value
        return -1

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''           
            [7,8,9,10,11,1,2,3,4,5,6]
        '''
        lo, hi = 0, len(nums)
        while lo < hi:
            mid = (lo+hi)//2
            if nums[mid] == target: return mid
            elif nums[mid] < target:
                if nums[mid] < nums[lo] and nums[lo] <= target:
                    hi = mid
                else:
                    lo = mid + 1
            elif nums[mid] > target:
                if nums[mid] >= nums[lo] and nums[lo] > target:
                    lo = mid + 1
                else:
                    hi = mid
        return -1

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        do not know the defination of roation, 
        in my opinion, the rotation of [0,1,2,4,5,6,7] shoud be [7,6,5,4,2,1,0] ?
        according to the question, I should think of the list after roation is still two increasing list, and with its max and min value inside

        the property of the rotated list is the key to solve this question
        """
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left + right)//2
            if nums[mid] == target:
                return mid
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid-1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1

# https://leetcode.com/problems/search-in-rotated-sorted-array/discuss/14435/Clever-idea-making-it-simple
def search(self, nums, target):
        lo, hi = 0, len(nums)

        while lo < hi:
            mid = (lo + hi) / 2
            
            if (nums[mid] < nums[0]) == ( target < nums[0]):
                if (nums[mid] < target):
                    lo = mid + 1
                elif (nums[mid] > target):
                    hi = mid
                else:
                    return mid
            elif target < nums[0]:
                lo = mid + 1
            else:
                hi = mid

        return -1

class Solution:
    def search(self, nums: 'List[int]', target: int) -> int:
        L, H = 0, len(nums)
        while L < H:
            M = (L+H) // 2
            if target < nums[0] < nums[M]: # -inf
                L = M+1
            elif target >= nums[0] > nums[M]: # +inf
                H = M
            elif nums[M] < target:
                L = M+1
            elif nums[M] > target:
                H = M
            else:
                return M
        return -1

        
S = Solution()
nums = [4,5,6,7,0,1,2]
target = 0
print(S.search(nums, target))
nums = [4,5,6,7,0,1,2]
target = 3
print(S.search(nums, target))
nums = [1,0]
target = 1
print(S.search(nums, target))
nums = [4,5,6,7,0,1,2]
target = 5
print(S.search(nums, target))