"""
Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
"""
class Solution_1:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # res_set = set()
        res = [[]]
        for num in nums:
            # print(num)
            for pre in res:
                tmp = pre.append(num)
                if tmp not in res:
                    print(tmp)
                    res = res + tmp
                # print(res)
        print(res)
        return 0

class Solution_2:
    def subsetsWithDup(self, nums):
        # res_set = {()}
        res_set = set()
        res_string = {''}
        # print(res_set)
        for num in nums:
            elements = {s+','+ str(num) for s in res_string}
            print(elements)
            res_set |= {tuple(s.split(',')) for s in elements}
            res_string = {','.join(s) for s in res_set}
        print(res_set)
        print(res_string)
        return res_set

class Solution_3:
    def subsetsWithDup(self, nums):
        # res_set = {()}
        res_set = set()
        res_list = [[]]
        # print(res_set)
        for num in nums:
            elements = [sorted(l+[num]) for l in res_list] + res_list
            res_set |= {tuple(l) for l in elements}
            res_list = [list(s) for s in res_set]
            # print(elements)
            # print(res_set)
            # print(res_list)
        return res_list


class Solution_4:
    def subsetsWithDup(self, nums):
        """
        use a counter and update it
        """
        # res_set = {()}
        res_set = set()
        res_list = [[]]
        # print(res_set)
        for num in nums:
            elements = [l+[num] for l in res_list] + res_list
            res_set |= {tuple(l) for l in elements}
            res_list = [list(s) for s in res_set]
            # print(elements)
            # print(res_set)
            # print(res_list)
        return res_list

class Solution_5:
    def subsetsWithDup(self, nums):
        res_set = set()
        res_list = [[]]
        nums = sorted(nums)
        for num in nums:
            elements = [l+[num] for l in res_list] + res_list
            res_set |= {tuple(l) for l in elements}
            res_list = [list(s) for s in res_set]
        return res_list

# class Solution:
#     def subsetsWithDup(self, nums):
#         res_set = set()
#         res_list = [[]]
#         nums = sorted(nums)
#         for i in range(len(nums):
#             if i == 0 or nums[i-1] != nums[i]:
#                 elements = [l+[num] for l in res_list] + res_list
#                 res_set |= {tuple(l) for l in elements}
#                 res_list = [list(s) for s in res_set]
#         return res_list



class Solution_6:
    def subsetsWithDup(self, nums):
        def dfs(index, path):
            res.append(path)
            # print(index, path)
            for i in range(index, len(nums)):
                # if i == index or nums[i] != nums[i-1]:
                if i > index and nums[i] == nums[i-1]:
                    continue
                dfs(i+1, path+[nums[i]])
        
        res = []
        nums = sorted(nums)
        dfs(0,[])
        return res

class Solution_8:
    def subsetsWithDup(self, nums):
        def dfs(index, path):
            res.append(path)
            for i in range(index, len(nums)):
                if i > index and nums[i] == nums[i-1]:
                    continue
                dfs(i+1, path+[nums[i]])

        res = []
        nums.sort()
        dfs(0, [])
        return res

class Solution_7:
    def subsetsWithDup(self, nums):
        res = []
        nums.sort()
        self.dfs(nums, 0, [], res)
        return res
        
    def dfs(self, nums, index, path, res):
        res.append(path)
        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i-1]:
                continue
            self.dfs(nums, i+1, path+[nums[i]], res)


        


class Solution:
    def subsetsWithDup(self, nums):
        #if S[i] is same to S[i - 1], then it needn't to be added to all of the subset, just add it to the last l subsets which are created by adding S[i - 1]
        nums = sorted(nums)
        res = [[]]
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i-1]: #add nums[i] to all the list in res
                pre_len = len(res) 
            for j in range(len(res)-pre_len, len(res)): #if nums[i] == nums[i-1], add nums[i] to the previous added list in res
                res.append(res[j] + [nums[i]])
        return res


class Solution:
    def subsetsWithDup(self, nums):
        nums = sorted(nums)
        res = [[]]
        curr = []
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i-1]:
                curr = [[nums[i]]+l for l in res]
            else:
                curr = [[nums[i]]+l for l in curr]
            res += curr
        return res

s = Solution_6()
test = [1,2,2]
print(s.subsetsWithDup(test))

test = [4,4,4,1,4]
"""
Output
[[4,4,1],[4,4,4,1],[1,4],[4,4,4,4],[1],[4,4,1,4],[4,4],[4,4,4,1,4],[4,4,4],[4],[4,1,4],[],[4,1]]
Expected
[[],[1],[1,4],[1,4,4],[1,4,4,4],[1,4,4,4,4],[4],[4,4],[4,4,4],[4,4,4,4]]
"""
print(s.subsetsWithDup(test))