"""
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""
import copy
class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        for num in nums:
            tmp = copy.deepcopy(res)
            for tmp_list in tmp:
                tmp_list.append(num)
            # tmp = [res_list.append(num) for res_list in res]
            res.extend(tmp)
        return res

class Solution_1:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """    
        oup = [[]]
        
        for num in nums:
            oup.extend([prev+[num] for prev in oup])
            
        return oup

class Solution_2:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """    
        oup = [[]]
        
        for num in nums:
            oup.extend([prev.append(num) for prev in oup])
            # can + but can not append, + returns a new list, while append modify the original one
        return oup

s = Solution_2()
test = [1]
print(s.subsets(test))
test = [1,2,3]
print(s.subsets(test))