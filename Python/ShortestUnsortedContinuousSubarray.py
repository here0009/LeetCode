class Solution:
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0 or len(nums) == 1:
            return 0
        else:
            max_value = nums[0]
            max_index = 0
            right_index = 0
            for i in range(len(nums)):
                if nums[i] >= max_value:
                    max_value = nums[i]
                    max_index = i
                else:
                    #nums[i] < max_value and i > max_index, unsorted, so right_index is i, inculde i
                    if i > max_index:
                        right_index = i

            min_value = nums[-1]
            min_index = len(nums)-1
            left_index = len(nums)-1
            for j in range(len(nums)-1, -1, -1):
                if nums[j] <= min_value:
                    min_value = nums[j]
                    min_index = j
                else:
                    #nums[j] > min_value and j < min_index, unsorted, so left_index is j, inculde i
                    if j < min_index:
                        left_index = j
        # print(right_index, nums[right_index])
        # print(left_index, nums[left_index])
        if right_index - left_index + 1  < 0:
            return 0
        else:
            return right_index - left_index + 1

s = Solution()
print(s.findUnsortedSubarray([1,2,3,4]))
print(s.findUnsortedSubarray([5,1,2,3,4]))
print(s.findUnsortedSubarray([1,2,3,4,0]))
print(s.findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15]))
print(s.findUnsortedSubarray([1,2,3,3,3]))