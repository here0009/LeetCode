"""
Given an initial array arr, every day you produce a new array using the array of the previous day.

On the i-th day, you do the following operations on the array of day i-1 to produce the array of day i:

If an element is smaller than both its left neighbor and its right neighbor, then this element is incremented.
If an element is bigger than both its left neighbor and its right neighbor, then this element is decremented.
The first and last elements never change.
After some days, the array does not change. Return that final array.

 

Example 1:

Input: arr = [6,2,3,4]
Output: [6,3,3,4]
Explanation: 
On the first day, the array is changed from [6,2,3,4] to [6,3,3,4].
No more operations can be done to this array.
Example 2:

Input: arr = [1,6,3,4,3,5]
Output: [1,4,4,4,4,5]
Explanation: 
On the first day, the array is changed from [1,6,3,4,3,5] to [1,5,4,3,4,5].
On the second day, the array is changed from [1,5,4,3,4,5] to [1,4,4,4,4,5].
No more operations can be done to this array.
 

Constraints:

3 <= arr.length <= 100
1 <= arr[i] <= 100

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/array-transformation
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def transformArray(self, nums):
        length = len(nums)
        addOne = []
        minusOne = []
        while True:
            for i in range(1, length-1):
                if nums[i] < min(nums[i-1], nums[i+1]):
                    addOne.append(i)
                elif nums[i] > max(nums[i-1], nums[i+1]):
                    minusOne.append(i)
            if not minusOne and not addOne:
                return nums
            # print(nums, minusOne, addOne)
            for i in minusOne:
                nums[i] -= 1
            for i in addOne:
                nums[i] += 1
            minusOne, addOne = [], []
        return None

S = Solution()
nums = [6,2,3,4]
print(S.transformArray(nums))
nums = [1,6,3,4,3,5]
print(S.transformArray(nums))