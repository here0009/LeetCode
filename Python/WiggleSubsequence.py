"""
A sequence of numbers is called a wiggle sequence if the differences between successive numbers strictly alternate between positive and negative. The first difference (if one exists) may be either positive or negative. A sequence with fewer than two elements is trivially a wiggle sequence.

For example, [1,7,4,9,2,5] is a wiggle sequence because the differences (6,-3,5,-7,3) are alternately positive and negative. In contrast, [1,4,7,2,5] and [1,7,4,5,5] are not wiggle sequences, the first because its first two differences are positive and the second because its last difference is zero.

Given a sequence of integers, return the length of the longest subsequence that is a wiggle sequence. A subsequence is obtained by deleting some number of elements (eventually, also zero) from the original sequence, leaving the remaining elements in their original order.

Example 1:

Input: [1,7,4,9,2,5]
Output: 6
Explanation: The entire sequence is a wiggle sequence.
Example 2:

Input: [1,17,5,10,13,15,10,5,16,8]
Output: 7
Explanation: There are several subsequences that achieve this length. One is [1,17,10,13,10,16,8].
Example 3:

Input: [1,2,3,4,5,6,7,8,9]
Output: 2
Follow up:
Can you do it in O(n) time?
"""
class Solution:
    def wiggleMaxLength(self, nums) -> int:
        # print(nums)
        
        length = len(nums)
        
        if length < 2:
            return length
        elif length == 2:
            return 2 if nums[0] != nums[1] else 1
        
        res = [nums[0]]
        
        index = 1
        while index < length and nums[index] == nums[0]:
            index += 1
        if index == length:
            return 1
        else:
            res.append(nums[index])
            index += 1
        
        flag = 'increasing' if res[1] > res[0] else 'decreasing'
        while index < length:
            if flag == 'increasing':
                if nums[index] > res[-1]:
                    res[-1] = nums[index]
                elif nums[index] < res[-1]:
                    res.append(nums[index])
                    flag = 'decreasing'
            elif flag == 'decreasing':
                if nums[index] < res[-1]:
                    res[-1] = nums[index]
                elif nums[index] > res[-1]:
                    res.append(nums[index])
                    flag = 'increasing'
            index += 1
        # print(res)
        return len(res)

class Solution:
    def wiggleMaxLength(self, nums) -> int:
        """
        All consequetive increases are counted only once.
        up = down + 1
        Similarly all consequetive decreases are counted only once
        down = up + 1
        """
        if not nums:
            return 0
        up, down = 1,1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                up = down + 1
            elif nums[i] < nums[i-1]:
                down = up + 1
        return max(up, down)


S = Solution()
nums = [1,7,4,9,2,5]
print(S.wiggleMaxLength(nums))
nums = [1,17,5,10,13,15,10,5,16,8]
print(S.wiggleMaxLength(nums))
nums = [1,2,3,4,5,6,7,8,9]
print(S.wiggleMaxLength(nums))
nums = [0,0]
print(S.wiggleMaxLength(nums))