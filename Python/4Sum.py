"""
Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:

The solution set must not contain duplicate quadruplets.

Example:

Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
"""
from collections import defaultdict
class Solution:
    """
    wrong answer
    """
    def fourSum(self, nums, target: int):
        nums = sorted(nums)
        print(nums)
        two_sum_dict = defaultdict(set)
        for i in range(len(nums)-1):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, len(nums)):
                if nums[j] == nums[j-1]:
                    continue
                v = nums[i]+nums[j]
                two_sum_dict[v].add((nums[i],nums[j],i,j))
        print(two_sum_dict)
        two_sum_list = sorted(two_sum_dict.keys())
        print(two_sum_list)
        l, r = 0, len(two_sum_list)-1
        res_set = set()
        # tmp = []
        while l < r:
            sum_2 = two_sum_list[l] + two_sum_list[r]
            if sum_2 < target:
                l += 1
            elif sum_2 > target:
                r -= 1
            else:
                for v1,v2,i1,i2 in two_sum_dict[two_sum_list[l]]:
                    for v3,v4,i3,i4 in two_sum_dict[two_sum_list[r]]:
                        if i1 != i3 and i2 != i4:
                            tmp = sorted([v1,v2,v3,v4])
                            res_set.add(tuple(tmp))
                            # tmp.append([i1,i2,i3,i4])
                l += 1
                r -= 1
        res = [[v1,v2,v3,v4] for v1,v2,v3,v4 in res_set]
        return res

from collections import defaultdict
class Solution:
    def fourSum(self, nums, target: int):
        twoSums = defaultdict(list)
        res_set = set()
        length = len(nums)
        for i in range(length-1):
            for j in range(i+1, length):
                k = nums[i] + nums[j]
                twoSums[k].append({i,j})
        # print(twoSums)
        half = target//2
        for key,l1 in twoSums.items():
            if key <= half and target-key in twoSums:
                l2 = twoSums[target-key]
                # print('l1,l2',l1,l2)
                for p in l1:
                    for q in l2:
                        tmp = tuple(p | q)
                        # print('tmp',tmp)
                        if len(tmp) == 4:
                            res_set.add(tuple(sorted([nums[v] for v in tmp])))

        res = [list(v) for v in res_set]
        # for values in res_set:
        #     res.append([nums[v] for v in values])
        return res


s = Solution()
nums = [1, 0, -1, 0, -2, 2]
target = 0
print(s.fourSum(nums, target))

nums = [0,0,0,0]
target = 0
print(s.fourSum(nums, target))

nums = [-3,-2,-1,0,0,1,2,3]
target = 0
"""
Output
[[-3,0,0,3],[-3,0,1,2],
[-3,-2,2,3],
[-2,-1,0,3],
[-3,-1,1,3],
[-3,0,1,2],
[-2,-1,0,3],[-1,0,0,1],[-2,-1,1,2],[-2,0,0,2]]
Expected
[[-3,-2,2,3],[-3,-1,1,3],[-3,0,0,3],[-3,0,1,2],[-2,-1,0,3],[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
"""
print(s.fourSum(nums, target))

nums = [-4,-3,-2,-1,0,0,1,2,3,4]
target = 0
print(s.fourSum(nums, target))