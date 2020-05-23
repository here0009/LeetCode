class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        len_num = len(nums)
        num_counts = dict()
        for num in nums:
            if num in num_counts:
                num_counts[num] += 1
            else:
                num_counts[num] = 1
            if num_counts[num] >= len_num/2:
                return num

s = Solution()
input_nums = [2,2,1,1,1,2,2]
print(s.majorityElement(input_nums))