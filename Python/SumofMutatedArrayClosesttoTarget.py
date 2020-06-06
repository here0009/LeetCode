"""
Given an integer array arr and a target value target, return the integer value such that when we change all the integers larger than value in the given array to be equal to value, the sum of the array gets as close as possible (in absolute difference) to target.

In case of a tie, return the minimum such integer.

Notice that the answer is not neccesarilly a number from arr.

 

Example 1:

Input: arr = [4,9,3], target = 10
Output: 3
Explanation: When using 3 arr converts to [3, 3, 3] which sums 9 and that's the optimal answer.
Example 2:

Input: arr = [2,3,5], target = 10
Output: 5
Example 3:

Input: arr = [60864,25176,27249,21296,20204], target = 56803
Output: 11361
 

Constraints:

1 <= arr.length <= 10^4
1 <= arr[i], target <= 10^5
"""
from bisect import bisect_left
class Solution:
    def findBestValue(self, arr, target: int) -> int:
        pass
        arr = sorted(arr)
        ava_target = target/len(arr)
        index = bisect_left(arr, ava_target)
        min_diff = float('inf')
        res = None
        print(target/len(arr))
        if index > 0:
            left = [arr[index-1]]
        else:
            left = [int(ava_target), int(ava_target)+1]
        if abs(sum(arr[i], arr[i]) - target) < min_diff:
            rse = left
        if index < len(arr):
            right = [arr[index]]
        else:
            right = [arr[index-1]]
        vals = left + right


class Solution_1:
    def findBestValue(self, arr, target: int) -> int:
        arr = [float('-inf')] + sorted(arr)
        # print(arr)
        total, i, length = 0, 1, len(arr)
        res_diff, res = float('inf'), arr[0]
        while i < length and total < target:
            v = (target - total) // (length - i)
            if abs(target - total - v * (length - i)) > abs(target - total - (v+1) * (length - i)):
                v += 1
            if v < arr[i-1]:
                break
            v = min(arr[i], v)
            diff = target - total - v * (length - i)
            # print('arr[i], diff, v, total', arr[i], diff, v, total)
            if diff == 0:
                return v
            total += arr[i]
            i += 1
            if diff < res_diff:
                res = v
        return res

class Solution:
    def findBestValue(self, arr, target: int) -> int:
        arr = [float('-inf')] + sorted(arr)
        # print(arr)
        total, i, length = 0, 1, len(arr)
        res_diff, res = float('inf'), arr[0]
        while i < length and total < target:
            v = round((target - total) / (length - i) - 0.0001) # if v is 0.5, we should round down
            if v < arr[i-1]:
                break
            v = min(arr[i], v)
            diff = target - total - v * (length - i)
            # print('arr[i], diff, v, total', arr[i], diff, v, total)
            if diff == 0:
                return v
            total += arr[i]
            i += 1
            if diff < res_diff:
                res = v
        return res

# https://leetcode.com/problems/sum-of-mutated-array-closest-to-target/discuss/463306/JavaC%2B%2BPython-Just-Sort-O(nlogn)
"""
we sort the input and compared A[i] with target one by one.

Sort the array A in decreasing order.
We try to make all values in A to be the min(A) (the last element)
If target >= min(A) * n, we doesn't hit our target yet.
We should continue to try a value bigger.
So we pop the min(A) value.
Consider that it won't be affected anymore,
we can remove it from target by target -= A.pop()
We continue doing step 2-4, until the next number is too big for target.
We split the the target evenly, depending on the number of element left in A
At this point, @bobalice help explain the round part:
if A is empty means its impossible to reach target so we just return maximum element.
If A is not empty, intuitively the answer should be the nearest integer to target / len(A).

Since we need to return the minimum such integer if there is a tie,
if target / len(A) has 0.5 we should round down,
"""
class Solution:
    def findBestValue(self, arr, target: int) -> int:
        arr= sorted(arr, reverse = True)
        maxA = arr[0]
        while arr and target > arr[-1]*len(arr):
            target -= arr.pop()
        return int(round(target / len(arr) - 0.01)) if arr else maxA

#  https://leetcode.com/problems/sum-of-mutated-array-closest-to-target/discuss/532804/Python-Binary-Search-Python-Really-Intuitive      
class Solution:
    def getRes(self,arr,t):
        nums = [t if num >= t else num for num in arr]
        return sum(nums)
    
    def findBestValue(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        l = 1
        h = max(arr)
        
        while l <= h:
            mid = (h-l)//2 + l
            curr = self.getRes(arr,mid)
            if curr == target:
                return mid
            elif curr < target:
                l = mid+1
            else:
                h = mid-1
        if abs(self.getRes(arr,l) - target) < abs(self.getRes(arr,h) - target):
            return l
        return h

s = Solution()
arr = [4,9,3]
target = 10
print(s.findBestValue(arr,target))
arr = [2,3,5]
target = 10
print(s.findBestValue(arr,target))
arr = [60864,25176,27249,21296,20204]
target = 56803
print(s.findBestValue(arr,target))
