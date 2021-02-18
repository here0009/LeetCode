"""
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums, return the minimum element of this array.

 

Example 1:

Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.
Example 2:

Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
Example 3:

Input: nums = [11,13,15,17]
Output: 11
Explanation: The original array was [11,13,15,17] and it was rotated 4 times. 
 

Constraints:

n == nums.length
1 <= n <= 5000
-5000 <= nums[i] <= 5000
All the integers of nums are unique.
nums is sorted and rotated between 1 and n times.

original list is 

       /
      /
     / 
    /
   /
  /
 / 
/

after rotate, like this
\for slash
       /
      /
     /
    /
   /
         \
          \
           \
its start is larger than end
if start < end, means we are in left part, just return start
if mid > end, go to right part
if mid < end, go to left part

"""


class Solution_2:
    def findMin(self, nums) -> int:
        print(nums)
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return min(nums)

        # print(nums[0])
        # print(nums[-1])
        # print(nums[len(nums)//2])
        mid = len(nums)//2
        left,mid_num,right = nums[0],nums[mid],nums[-1]
        if left == min(left,mid_num,right):
            return left
        if mid_num == max(left,mid_num,right):
            return self.findMin(nums[mid+1:])
        if mid_num == min(left,mid_num,right):
            return self.findMin(nums[:mid+1])

class Solution_1:
    def findMin(self, nums) -> int:

        if len(nums) < 3:
            return min(n)

        mid = len(nums)//2
        left,mid_num,right = nums[0],nums[mid],nums[-1]
        #left will be larger than right, unless it is the smallest value
        if left < right:
            return left
        if mid_num > right:
            return self.findMin(nums[mid+1:])
        if mid_num < right:
            return self.findMin(nums[:mid+1])

class Solution:
    def findMin(self, nums) -> int:
        l,r = 0, len(nums)-1
        while l < r:
            mid = (r+l)//2
            if nums[l] < nums[r]:
                return nums[l]
            if nums[mid] > nums[r]:
                l = mid+1
            elif nums[mid] < nums[r]:
                r = mid
        return nums[l]

s = Solution()
# nums = [3,4,5,1,2]
# print(s.findMin(nums))

# nums = [4,5,6,7,0,1,2]
# print(s.findMin(nums))

# nums = [3,1,2]
# print(s.findMin(nums))

nums = [57,58,59,62,63,66,68,72,73,74,75,76,77,78,80,81,86,95,96,97,98,100,101,102,103,110,119,120,121,123,125,126,127,132,136,144,145,148,149,151,152,160,161,163,166,168,169,170,173,174,175,178,182,188,189,192,193,196,198,199,200,201,202,212,218,219,220,224,225,229,231,232,234,237,238,242,248,249,250,252,253,254,255,257,260,266,268,270,273,276,280,281,283,288,290,291,292,294,295,298,299,4,10,13,15,16,17,18,20,22,25,26,27,30,31,34,38,39,40,47,53,54]

print(s.findMin(nums))
