"""
Given two integer arrays arr1 and arr2, return the minimum number of operations (possibly zero) needed to make arr1 strictly increasing.

In one operation, you can choose two indices 0 <= i < arr1.length and 0 <= j < arr2.length and do the assignment arr1[i] = arr2[j].

If there is no way to make arr1 strictly increasing, return -1.

 

Example 1:

Input: arr1 = [1,5,3,6,7], arr2 = [1,3,2,4]
Output: 1
Explanation: Replace 5 with 2, then arr1 = [1, 2, 3, 6, 7].
Example 2:

Input: arr1 = [1,5,3,6,7], arr2 = [4,3,1]
Output: 2
Explanation: Replace 5 with 3 and then replace 3 with 4. arr1 = [1, 3, 4, 6, 7].
Example 3:

Input: arr1 = [1,5,3,6,7], arr2 = [1,6,3,3]
Output: -1
Explanation: You can't make arr1 strictly increasing.
 

Constraints:

1 <= arr1.length, arr2.length <= 2000
0 <= arr1[i], arr2[i] <= 10^9
 
"""


from typing import List
class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        pre_v = -float('inf')
        len_arr1, len_arr2 = len(arr1), len(arr2)
        sub_nums = []
        res = 0
        # pre_v 
        for i in range(len_arr1 - 1):
            # print(i, arr2[i])
            if i < len_arr2:
                heapq.heappush(sub_nums, arr2[i])
            if arr1[i] >= arr1[i + 1]:  # not strictly increasing, replace arr1[i], arr1[i] should larger than arr1[i-1]
                while sub_nums and sub_nums[0] <= pre_v:
                    sub_nums.pop()
                if sub_nums:
                    res += 1
                    arr1[i] = sub_nums.pop()
                else:
                    return -1
            pre_v = arr1[i]
        return res


from bisect import bisect_left
class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        pre_v = -float('inf')
        len_arr1 = len(arr1)
        arr2.sort()
        res = 0
        for i in range(len_arr1 - 1):
            print(i, arr1, arr2)
            if arr1[i] >= arr1[i + 1] or arr1[i] <= pre_v:
                j = bisect_left(arr2, pre_v + 1)
                if j < len(arr2):
                    res += 1
                    arr1[i] = arr2[j]
                    arr2 = arr2[j + 1:]
                else:
                    return -1
            # if arr1[i] <= arr1[i - 1]:
            pre_v = arr1[i]
        return res


from bisect import bisect_right
class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        """
        Thougths: sort arr2 first
        use dict[swap] to record the min value we can get with a specific swap to keep the array increasing, return the min of dict.keys()
        """
        dp = {0: -float('inf')}
        arr2.sort()
        len_arr2 = len(arr2)
        for num in arr1:
            dp2 = dict()
            print(dp)
            for k, v in dp.items():
                if v < num:
                    dp2[k] = num
                else:
                    index = bisect_right(arr2, v)
                    if index < len_arr2:
                        dp2[k + 1] = arr2[index]
            dp = dp2
            print(dp)
        return min(dp.keys())



from bisect import bisect_right
from collections import defaultdict
class Solution_1:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        """
        Thougths: sort arr2 first
        use dict[swap] to record the min value we can get with a specific swap to keep the array increasing, return the min of dict.keys()
        bisect(lst, val)
        if val in lst, bisect_left will return the index of the left most val
        and bisect_right will right the index + 1 of the right most val
        """
        dp = {0: -float('inf')}
        arr2.sort()
        len_arr2 = len(arr2)
        for num in arr1:
            dp2 = defaultdict(lambda: float('inf'))
            for k, v in dp.items():  # for every k,v in dp we got to options, replace it with num with no swap or replace it with the min valid value in arr2
                if num > v:
                    dp2[k] = min(dp2[k], num)
                idx = bisect_right(arr2, v)
                if idx < len_arr2:
                    dp2[k + 1] = min(dp2[k + 1], arr2[idx])
            dp = dp2
            if not dp:
                return -1
            # print(dp)
        return min(dp.keys())



from bisect import bisect_right
from collections import defaultdict
class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        """
        similar to previous solution we can use dp(v, swap) to record the min swaps we need to get a v at each iteration
        """
        dp = {-float('inf'): 0}
        arr2.sort()
        len_arr2 = len(arr2)
        for num in arr1:
            dp2 = defaultdict(lambda: float('inf'))
            for k, v in dp.items():
                if num > k:
                    dp2[num] = min(dp2[num], v)
                idx = bisect_right(arr2, k)
                if idx < len_arr2:
                    dp2[arr2[idx]] = min(dp2[arr2[idx]], v + 1)
            dp = dp2
            # print(dp)
            if not dp:
                return -1
        return min(dp.values())


S = Solution_1()
arr1 = [1,5,3,6,7]
arr2 = [1,3,2,4]
print(S.makeArrayIncreasing(arr1, arr2))
arr1 = [1,5,3,6,7]
arr2 = [4,3,1]
print(S.makeArrayIncreasing(arr1, arr2))
arr1 = [1,5,3,6,7]
arr2 = [1,6,3,3]
print(S.makeArrayIncreasing(arr1, arr2))
arr1 = [0,11,6,1,4,3]
arr2 = [5,4,11,10,1,0]
print(S.makeArrayIncreasing(arr1, arr2))
# Output
# 4
# Expected
# 5