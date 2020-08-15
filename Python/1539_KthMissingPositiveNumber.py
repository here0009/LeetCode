"""
Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.

Find the kth positive integer that is missing from this array.

 

Example 1:

Input: arr = [2,3,4,7,11], k = 5
Output: 9
Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5th missing positive integer is 9.
Example 2:

Input: arr = [1,2,3,4], k = 2
Output: 6
Explanation: The missing positive integers are [5,6,7,...]. The 2nd missing positive integer is 6.
 

Constraints:

1 <= arr.length <= 1000
1 <= arr[i] <= 1000
1 <= k <= 1000
arr[i] < arr[j] for 1 <= i < j <= arr.length
"""


class Solution:
    def findKthPositive(self, arr, k: int) -> int:
        curr = 1
        for num in arr:
            if curr != num:
                while curr != num:
                    if k == 1:
                        return curr
                    curr += 1
                    k -= 1
            curr += 1
        return curr + k - 1



class Solution:
    def findKthPositive(self, arr, k: int) -> int:
        left, right = 0, len(arr)
        while left < right:
            mid = (left + right) //2
            if arr[mid] - mid <= k:
                left = mid + 1
            else:
                right = mid
        return left + k


class Solution:
    def findKthPositive(self, arr, k: int) -> int:
        left, right = 0, len(arr)
        # print("+++++++++")
        while left < right:
            
            mid = (left + right) //2
            # print(left, right, mid)
            # print(arr[mid], mid)
            if arr[mid] - mid > k:
                right = mid
            else:
                left = mid + 1
        return left + k

S = Solution()
arr = [2,3,4,7,11]
k = 5
print(S.findKthPositive(arr, k))
arr = [1,2,3,4]
k = 2
print(S.findKthPositive(arr, k))
# arr = [1,2,3,4]
# k = 3
# print(S.findKthPositive(arr, k))
