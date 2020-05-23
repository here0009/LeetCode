"""
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

Note:

Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice.
Example:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
"""
class Solution_1:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        end = len(numbers)-1
        start = 1
        for index, num in enumerate(numbers):
            # print(index)
            find_index = self.find_num(numbers, target-num, index+1, end)
            if find_index != -1:
                return [index+1, find_index+1]

        
    def find_num(self, numbers, target, start, end):
        """
        return index if target was find, else return -1
        """
        # print(start, end)
        if end - start < 2:
            if numbers[start] == target:
                return start
            elif numbers[end] == target:
                return end
            else:
                return -1
        middle = (start + end) //2
        if target < numbers[middle]:
            return self.find_num(numbers, target, start, middle)
        elif target > numbers[middle]:
            return self.find_num(numbers, target, middle, end)
        else:
            return middle


class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l, r = 0, len(numbers)-1
        while l < r:
            # print(l, r)
            s = numbers[l] + numbers[r]
            if s == target:
                return [l+1, r+1]
            elif s < target:
                l += 1
            else:
                r -= 1

s = Solution()
numbers = [2,7,11,15]
target = 9

print(s.twoSum(numbers, target))

numbers = [2,3,4]
target = 6
print(s.twoSum(numbers, target))