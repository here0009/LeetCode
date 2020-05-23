class Solution_1:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        low = 0
        high = len(nums)-1
        if target <= nums[0]:
            return low
        elif target >= nums[high]:
            return high
        else:
            return self.searchRange(nums, low, high, target)

    
    def searchRange(self, nums, low, high, target):
        if nums[low] == target:
            return low
        elif high - low == 1: #only two elements, the smaller one is not equal, return the larger one
            return high
        else:
            middle = (high - low)//2
            if target == nums[middle]:
                return middle
            elif target < nums[middle]:
                return self.searchRange(nums, low, middle-1, target)
            else:
                return self.searchRange(nums, middle+1, high, target)


class Solution_1:
    def searchInsert(self, nums, target):
        if nums[0] >= target:
            return 0
        for i in range(1,len(nums)):
            if nums[i] == target:
                return i
            if nums[i-1] < target and nums[i] > target:
                return i
        return len(nums)

class Solution:
    def searchInsert(self, nums, target):

        def bisearch(left, right):
            # print(left,right)
            if nums[left] >= target:
                return left
            if nums[right] < target:
                return right+1
            middle = (left + right) //2
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                return bisearch(middle+1, right)
            else:
                return bisearch(left, middle-1)

        return bisearch(0, len(nums)-1)


s = Solution()
numbers = [1,3,5,6]
t = 5
print(s.searchInsert(numbers, t))
t = 2
print(s.searchInsert(numbers, t))
t = 7
print(s.searchInsert(numbers, t))
t = 0
print(s.searchInsert(numbers, t))