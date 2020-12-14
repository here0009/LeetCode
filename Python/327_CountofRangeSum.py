"""
Given an integer array nums, return the number of range sums that lie in [lower, upper] inclusive.
Range sum S(i, j) is defined as the sum of the elements in nums between indices i and j (i ≤ j), inclusive.

Note:
A naive algorithm of O(n2) is trivial. You MUST do better than that.

Example:

Input: nums = [-2,5,-1], lower = -2, upper = 2,
Output: 3 
Explanation: The three ranges are : [0,0], [2,2], [0,2] and their respective sums are: -2, -1, 2.
 

Constraints:

0 <= nums.length <= 10^4
"""


# https://leetcode.com/problems/count-of-range-sum/discuss/77991/Short-and-simple-O(n-log-n)
from typing import List
class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        def mergeSort(left, right):
            mid = (left + right) //2
            if left == mid:
                return 0
            res = mergeSort(left, mid) + mergeSort(mid, right)
            i = j = mid
            for k in range(left, mid):
                while i < right and preSum[i] - preSum[k] < lower:
                    i += 1
                while j < right and preSum[j] - preSum[k] <= upper:
                    j += 1
                res += j-i
            preSum[left:right] = sorted(preSum[left:right])
            # print(left, right, mid, res, preSum)
            return res

        preSum = [0]
        for num in nums:
            preSum.append(preSum[-1] + num)
        res = mergeSort(0, len(preSum))
        return res


from typing import List
class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        def mergeSort(left, right):
            if left == right:
                return 0
            mid = (left + right) //2
            res = mergeSort(left, mid) + mergeSort(mid+1, right)
            i = j = mid+1
            for k in range(left, mid+1):
                while i <= right and preSum[i] - preSum[k] < lower:
                    i += 1
                while j <= right and preSum[j] - preSum[k] <= upper:
                    j += 1
                res += j-i
            preSum[left:right+1] = sorted(preSum[left:right+1])
            # print(left, right, mid, res, preSum)
            return res

        preSum = [0]
        for num in nums:
            preSum.append(preSum[-1] + num)
        length = len(preSum)
        res = mergeSort(0, length-1)
        return res

# https://leetcode.com/problems/count-of-range-sum/discuss/407655/Python-different-concise-solutions
class SegmentTreeNode:
    def __init__(self,low,high):
        self.low = low
        self.high = high
        self.left = None
        self.right = None
        self.cnt = 0        
        
class Solution: 
    def _bulid(self, left, right): 
        root = SegmentTreeNode(self.cumsum[left],self.cumsum[right])
        if left == right:
            return root
        
        mid = (left+right)//2
        root.left = self._bulid(left, mid)
        root.right = self._bulid(mid+1, right)
        return root
    
    def _update(self, root, val):
        if not root:
            return 
        if root.low<=val<=root.high:
            root.cnt += 1
            self._update(root.left, val)
            self._update(root.right, val)
                  
    def _query(self, root, lower, upper):
        if lower <= root.low and root.high <= upper:
            return root.cnt
        if upper < root.low or root.high < lower:
            return 0
        return self._query(root.left, lower, upper) + self._query(root.right, lower, upper)
        
    # prefix-sum + SegmentTree | O(nlogn)      
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        cumsum = [0]
        for n in nums:
            cumsum.append(cumsum[-1]+n)
            
        self.cumsum = sorted(list(set(cumsum))) # need sorted
        root = self._bulid(0,len(self.cumsum)-1)
        
        res = 0
        for csum in cumsum:
            res += self._query(root, csum-upper, csum-lower)
            self._update(root, csum)        
        return res
S = Solution()
nums = [-2,5,-1]
lower = -2
upper = 2
print(S.countRangeSum(nums, lower, upper))
