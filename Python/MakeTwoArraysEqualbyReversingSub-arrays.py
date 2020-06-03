"""
Given two integer arrays of equal length target and arr.

In one step, you can select any non-empty sub-array of arr and reverse it. You are allowed to make any number of steps.

Return True if you can make arr equal to target, or False otherwise.

 

Example 1:

target = [1,2,3,4]
arr = [2,4,1,3]

target = [7]
arr = [7]

target = [1,12]
arr = [12,1]

target = [3,7,9]
arr = [3,7,11]

target = [1,1,1,1,1]
arr = [1,1,1,1,1]

Output: true
 

Constraints:

target.length == arr.length
1 <= target.length <= 1000
1 <= target[i] <= 1000
1 <= arr[i] <= 1000
"""


from collections import Counter
class Solution:
    def canBeEqual(self, target, arr) -> bool:
        t_counter = Counter(target)
        a_counter = Counter(arr)
        return t_counter == a_counter

S = Solution()
target = [1,2,3,4]
arr = [2,4,1,3]
print(S.canBeEqual(target, arr))
target = [7]
arr = [7]
print(S.canBeEqual(target, arr))
target = [1,12]
arr = [12,1]
print(S.canBeEqual(target, arr))
target = [3,7,9]
arr = [3,7,11]
print(S.canBeEqual(target, arr))
target = [1,1,1,1,1]
arr = [1,1,1,1,1]
print(S.canBeEqual(target, arr))