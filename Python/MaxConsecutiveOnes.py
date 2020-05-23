"""
Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
Note:

The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000
"""
class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if sum(nums) == 0:
            return 0
        start_flag = False
        res = 0
        len_nums = len(nums)
        for index, num in enumerate(nums):
            if start_flag:
                if num == 0:
                    end_index = index
                    tmp = end_index - start_index
                    if tmp > res:
                        res = tmp
                    start_flag = False

            else:
                if num == 1:
                    start_flag = True
                    start_index = index

            if index == len_nums-1:
                end_index = index
                if num ==  1:
                    tmp = end_index - start_index + 1
                else:
                    tmp = end_index - start_index
                if tmp > res:
                    res = tmp   
        return res

class Solution_1:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        Run results of solution 1:
        ['11', '111']
        3
        ['1']
        1
        ['', '', '1']
        1
        ['', '1', '']
        1
        ['', '']
        0
        """
        num_string = ''.join([str(num) for num in nums])
        trans_num_list = num_string.split('0')
        print(trans_num_list)
        return max([len(num) for num in trans_num_list])

class Solution_2:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        print(bytearray(nums))
        print( bytearray(nums).split(b'\x00'))
        return max([len(i) for i in bytearray(nums).split(b'\x00')])        

s = Solution_2()
test = [1,1,0,1,1,1]
print(s.findMaxConsecutiveOnes(test))
test = [1]
print(s.findMaxConsecutiveOnes(test))
test = [0,0,1]
print(s.findMaxConsecutiveOnes(test))
test = [0,1,0]
print(s.findMaxConsecutiveOnes(test))
test = [0]
print(s.findMaxConsecutiveOnes(test))

