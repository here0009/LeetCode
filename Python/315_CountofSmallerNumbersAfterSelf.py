"""
You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].

 

Example 1:

Input: nums = [5,2,6,1]
Output: [2,1,1,0]
Explanation:
To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.
 

Constraints:

0 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
"""


from typing import List
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        """
        mergesort can only got the total number, because we sorted num, we cannot find the result for each elemnt, try fenwick tree
        """
        def mergeSort(left, right):
            mid = (left + right)//2
            if left == mid:
                return 0
            res = mergeSort(left, mid) + mergeSort(mid, right)
            i = left
            for k in range(mid, right):
                while i < mid and nums[i] < nums[k]:
                    i += 1
                res += mid - i
            nums[left:right] = sorted(nums[left:right])
            return res

        return mergeSort(0, len(nums))



from typing import List
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        def getSum(x):
            res = 0
            while x != 0:
                res += counts[x]
                x -= x &- x
            return res

        def update(x):
            while x < length:
                counts[x] += 1
                x += x&-x


        val_dict = {v:i+1 for i,v in enumerate(sorted(set(nums)))}
        length = len(val_dict) +1
        
        # val_dict = dict()
        # unique_vals = sorted(set(nums))
        # length = len(unique_vals)+1
        # for i,v in enumerate(unique_vals):
        #     val_dict[v] = i+1
        counts = (length)*[0]
        res = []
        for num in nums[::-1]:
            index = val_dict[num]
            res.append(getSum(index-1))
            update(index)
        return res[::-1]

# https://leetcode.com/problems/count-of-smaller-numbers-after-self/discuss/76584/Mergesort-solution
from typing import List
from bisect import bisect_left, insort
class Solution_1:
    def countSmaller(self, nums: List[int]) -> List[int]:
        sorted_lst = []
        res = []
        for num in nums[::-1]:
            res.append(bisect_left(sorted_lst, num))
            insort(sorted_lst, num)
        return res[::-1]

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        def mergeSort(lst):
            if len(lst) <= 1:
                return lst
            half = len(lst)//2
            left, right = mergeSort(lst[:half]), mergeSort(lst[half:])
            for i in range(len(lst)-1, -1, -1):
                if not right or (left and nums[left[-1]] > nums[right[-1]]):
                    res[left[-1]] += len(right)
                    lst[i] = left.pop()
                else:
                    lst[i] = right.pop()
            return lst

        res = [0]*len(nums)
        mergeSort(list(range(len(nums))))
        return res

class SegmentTreeNode:
    def __init__(self, low, high):
        self.low = low
        self.high = high
        self.left = None
        self.right = None
        self.count = 0


class Solution:
    def _build(self, left, right):
        root = SegmentTreeNode(self.sorted_nums[left], self.sorted_nums[right])
        if left == right:
            return root
        mid = (left + right)//2
        root.left = self._build(left, mid)
        root.right = self._build(mid+1, right)
        return root

    def _update(self,node, val):
        if not node:
            return
        if node.low <= val <= node.high:
            node.count += 1
            self._update(node.left, val)
            self._update(node.right, val)

    def _query(self, node, lower, upper):
        # if not node: #we do not build None as left and right children, so no need for this
        #     return 0
        if lower <= node.low and node.high <= upper:
            return node.count
        if node.low > upper or node.high < lower:
            return 0 
        return self._query(node.left, lower, upper) + self._query(node.right, lower, upper)


    def countSmaller(self, nums: List[int]) -> List[int]:
        self.sorted_nums = sorted(set(nums))
        tree = self._build(0, len(self.sorted_nums)-1) if self.sorted_nums else None
        res = []
        for num in nums[::-1]:
            res.append(self._query(tree, float('-inf'), num-1))
            self._update(tree, num)
        # print(res)
        return res[::-1]


S = Solution()
nums = [5,2,6,1]
print(S.countSmaller(nums))

nums =[-1,-1]
print(S.countSmaller(nums))

nums =[]
print(S.countSmaller(nums))