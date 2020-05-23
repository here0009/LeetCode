"""
The set S originally contains numbers from 1 to n. But unfortunately, due to the data error, one of the numbers in the set got duplicated to another number in the set, which results in repetition of one number and loss of another number.

Given an array nums representing the data status of this set after the error. Your task is to firstly find the number occurs twice and then find the number that is missing. Return them in the form of an array.

Example 1:
Input: nums = [1,2,2,4]
Output: [2,3]
Note:
The given array size will in the range [2, 10000].
The given array's numbers won't have any order.
"""
class Solution_1:
    def findErrorNums(self, nums):
        res = [0,0]
        exist = [0]*(len(nums)+1)

        for num in nums:
            exist[num]+=1

        for i in range(1,len(nums)+1):
            if exist[i] == 2:
                res[0] = i
            if exist[i] == 0:
                res[1] = i
        return res

class Solution:
    def findErrorNums(self, nums):
        sum_set_nums = sum(set(nums))
        dup = sum(nums) - sum_set_nums
        miss = sum([i for i in range(1,len(nums)+1)]) - sum_set_nums
        return [dup,miss]


s = Solution()
nums = [1,2,2,4]
print(s.findErrorNums(nums))

