class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i):
                if nums[i]+nums[j] == target:
                    solution = [i,j]
                    break
                
        return solution
        

s = Solution()
nums = [1,2,3,4,5]
target = 7
print(s.twoSum(nums, target))