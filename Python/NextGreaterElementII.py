"""
Given a circular array (the next element of the last element is the first element of the array), print the Next Greater Number for every element. The Next Greater Number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, output -1 for this number.

Example 1:
Input: [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2; 
The number 2 can't find next greater number; 
The second 1's next greater number needs to search circularly, which is also 2.
Note: The length of given array won't exceed 10000.
"""
class Solution_1:
    def nextGreaterElements(self, nums):
        if not nums:
            return []
        res = [0]*len(nums)
        stack = [(float('inf'),-1)]
        for i,v in enumerate(nums):
            while stack[-1][0] < v:
                value,index = stack.pop()
                res[index] = v
            stack.append((v,i))
  
        max_v,max_i = stack[1]
        nums2 = nums[:max_i+1] + [float('inf')] #from beginning to the max_value of nums
        nums2 = nums2[::-1]

        while len(stack) > 1: #except inf
            v,i = stack.pop()
            while nums2[-1] <= v:
                nums2.pop()
            if nums2[-1] == float('inf'):
                res[i] = -1
            else:
                res[i] = nums2[-1]
        return res

class Solution:
    def nextGreaterElements(self, nums):
        if not nums:
            return []
        res = [-1]*len(nums)
        stack = []
        for i in range(len(nums)):
            while stack and nums[stack[-1]] < nums[i]:
                res[stack.pop()] = nums[i]
            stack.append(i)
        # print(stack)
        nums2 = nums[:stack[0]+1][::-1] #from max value to begin
        # print(nums2)
        while stack and nums2:
            while nums2 and nums2[-1] <= nums[stack[-1]]:
                nums2.pop()
            if nums2:
                res[stack.pop()] = nums2[-1]
            else:
                res[stack.pop()] = -1
        return res


S = Solution()
nums = [1,2,1]
print(S.nextGreaterElements(nums))

nums = [1,2,3,2,1]
print(S.nextGreaterElements(nums))
# Output
# [2,3,-1,3,3]
# Expected
# [2,3,-1,3,2]

nums = [1,1,1,1,1]
print(S.nextGreaterElements(nums))

nums = [100,1,11,1,120,111,123,1,-1,-100]
# Output
# [120,11,120,120,123,123,-1,11,1,1]
# Expected
# [120,11,120,120,123,123,-1,100,100,100]
print(S.nextGreaterElements(nums))