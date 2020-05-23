"""
Given an array nums sorted in ascending order, return true if and only if you can split it into 1 or more subsequences such that each subsequence consists of consecutive integers and has length at least 3.

 

Example 1:

Input: [1,2,3,3,4,5]
Output: True
Explanation:
You can split them into two consecutive subsequences : 
1, 2, 3
3, 4, 5

Example 2:

Input: [1,2,3,3,4,4,5,5]
Output: True
Explanation:
You can split them into two consecutive subsequences : 
1, 2, 3, 4, 5
3, 4, 5

Example 3:

Input: [1,2,3,4,4,5]
Output: False
 

Constraints:

1 <= nums.length <= 10000
"""
class Solution:
    """
    TLE
    """
    def isPossible(self, nums) -> bool:
        res_list = []
        for n in nums:
            for i in range(len(res_list)-1, -1, -1):
                if res_list[i][-1] == n-1:
                    res_list[i].append(n)
                    break
            else:
                res_list.append([n])
        # print(res_list)
        for l in res_list:
            if len(l) < 3:
                return False
        return True

"""
Using two list start and end to record the start and end num of consecutive list
then binary search n in end for n in nums.
if end[index-1] equals to n-1, update it to n.
if index == 0 or end[index-1] != n-1, append new list to start end end
check if all end[i]-start[i] >=2 in list start and end
"""
from bisect import bisect_left
class Solution:
    def isPossible(self, nums) -> bool:
        start = []
        end = []
        for n in nums:
            index = bisect_left(end, n)
            if index != 0 and end[index-1] == n-1: 
                end[index-1] = n
            else:
                start.append(n)
                end.append(n)

        return all(end[i]- start[i] >=2 for i in range(len(end)))

s = Solution()
nums = [1,2,3,3,4,5]
print(s.isPossible(nums))

nums = [1,2,3,3,4,4,5,5]
print(s.isPossible(nums))

nums = [1,2,3,4,4,5]
print(s.isPossible(nums))

nums = [1,2,3,4,6,7,8,9,10,11]
print(s.isPossible(nums))