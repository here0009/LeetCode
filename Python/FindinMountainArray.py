"""
(This problem is an interactive problem.)

You may recall that an array A is a mountain array if and only if:

A.length >= 3
There exists some i with 0 < i < A.length - 1 such that:
A[0] < A[1] < ... A[i-1] < A[i]
A[i] > A[i+1] > ... > A[A.length - 1]
Given a mountain array mountainArr, return the minimum index such that mountainArr.get(index) == target.  If such an index doesn't exist, return -1.

You can't access the mountain array directly.  You may only access the array using a MountainArray interface:

MountainArray.get(k) returns the element of the array at index k (0-indexed).
MountainArray.length() returns the length of the array.
Submissions making more than 100 calls to MountainArray.get will be judged Wrong Answer.  Also, any solutions that attempt to circumvent the judge will result in disqualification.

 

Example 1:

Input: array = [1,2,3,4,5,3,1], target = 3
Output: 2
Explanation: 3 exists in the array, at index=2 and index=5. Return the minimum index, which is 2.
Example 2:

Input: array = [0,1,2,4,2,1], target = 3
Output: -1
Explanation: 3 does not exist in the array, so we return -1.
 

Constraints:

3 <= mountain_arr.length() <= 10000
0 <= target <= 10^9
0 <= mountain_arr.get(index) <= 10^9
"""
# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
class MountainArray:
    def get(self, index: int) -> int:
        pass

    def length(self) -> int:
        pass

class Solution:
    """
    two much word
    """

    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        self.array = dict()
        self.arr_len = len(mountain_arr)
        self.mountain_arr = mountain_arr
        mid = self.arr_len // 2
        def findPeak(l,r):
            if r - l < 3:
                return max(self.getRange(l,r,mountain_arr))
            while l < r:
                mid = (l+r)//2
                if mountain_arr[mid] = max(self.getRange(mid-1,mid+2,mountain_arr)):
                    return mid
                elif mountain[mid+1] > mountain[mid]:
                    return findPeak(mid+1, r)
                else:
                    return findPeak(l, mid-1)

    
    def getRange(l, r, mountain_arr):
        for i in range(l,r):
            res = []
            if i in self.array:
                res.append(self.array[i])
            else:
                self.array[i] = mountain_arr.get(i)
                res.append(self.array[i])
            return res

    def getIndex(i, mountain_arr):
        if i in self.array:
            return self.array[i]
        else:
            self.array[i] = mountain_arr.get(i)
            return self.array[i]

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        l, r = 0, mountain_arr.length()-1
        while l < r:
            mid = (l+r) // 2
            if mountain_arr.get(mid) < mountain_arr.get(mid+1):
                l = mid + 1
            else:
                r = mid
        peak = l
        print(peak)
        l, r  = 0, peak
        while l <= r:
            mid = (l+r)//2
            if mountain_arr.get(mid) < target:
                l = mid + 1
            elif mountain_arr.get(mid) > target:
                r = mid - 1
            else:
                return mid

        l, r = peak, mountain_arr.length()-1
        while l <= r:
            mid = (l+r)//2
            if mountain_arr.get(mid) < target:
                r = mid - 1
            elif mountain_arr.get(mid) > target:
                l = mid+1
            else:
                return mid

        return -1
            