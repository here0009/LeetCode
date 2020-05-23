"""
A zero-indexed array A of length N contains all integers from 0 to N-1. Find and return the longest length of set S, where S[i] = {A[i], A[A[i]], A[A[A[i]]], ... } subjected to the rule below.

Suppose the first element in S starts with the selection of element A[i] of index = i, the next element in S should be A[A[i]], and then A[A[A[i]]]… By that analogy, we stop adding right before a duplicate element occurs in S.

 

Example 1:

Input: A = [5,4,0,3,1,6,2]
Output: 4
Explanation: 
A[0] = 5, A[1] = 4, A[2] = 0, A[3] = 3, A[4] = 1, A[5] = 6, A[6] = 2.

One of the longest S[K]:
S[0] = {A[0], A[5], A[6], A[2]} = {5, 6, 2, 0}
 

Note:

N is an integer within the range [1, 20,000].
The elements of A are all distinct.
Each element of A is an integer within the range [0, N-1].
"""
class Solution_1:
    def arrayNesting(self, nums) -> int:
        nums_set = set()
        res = 0
        for i in range(len(nums)):
            if i in nums_set:
                continue
            index = i
            tmp_set = {index}
            while True:
                tmp_num = nums[index]
                if tmp_num in tmp_set:
                    break
                tmp_set.add(tmp_num)
                index = tmp_num
            res = max(res,len(tmp_set))
            # print(tmp_set)
            nums_set = nums_set |tmp_set
        return res

class Solution:
    def arrayNesting(self, nums) -> int:
        len_nums = len(nums)
        seen = [False]*len_nums
        res = 0
        for i in range(len_nums):
            counts = 0
            index = i
            while not seen[index]:
                seen[index] = True
                index = nums[index]
                counts += 1
            res = max(counts, res)
        return res


s = Solution()
nums = [5,4,0,3,1,6,2]
print(s.arrayNesting(nums))

nums = [0]
print(s.arrayNesting(nums))