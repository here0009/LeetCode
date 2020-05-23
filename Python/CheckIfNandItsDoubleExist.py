"""
Given an array arr of integers, check if there exists two integers N and M such that N is the double of M ( i.e. N = 2 * M).

More formally check if there exists two indices i and j such that :

i != j
0 <= i, j < arr.length
arr[i] == 2 * arr[j]
 

Example 1:

Input: arr = [10,2,5,3]
Output: true
Explanation: N = 10 is the double of M = 5,that is, 10 = 2 * 5.
Example 2:

Input: arr = [7,1,14,11]
Output: true
Explanation: N = 14 is the double of M = 7,that is, 14 = 2 * 7.
Example 3:

Input: arr = [3,1,7,11]
Output: false
Explanation: In this case does not exist N and M, such that N = 2 * M.
 

Constraints:

2 <= arr.length <= 500
-10^3 <= arr[i] <= 10^3
"""
from collections import Counter
class Solution:
    def checkIfExist(self, arr) -> bool:
        arr_counter = Counter(arr)
        if (0 in arr_counter and arr_counter[0] > 1) or (1 in arr_counter and arr_counter[1]>1):
            return True
        for n in arr_counter:
            if n == 0 or n == 1:
                continue
            if 2*n in arr_counter:
                return True
        return False

S = Solution()
arr = [10,2,5,3]
print(S.checkIfExist(arr))
arr = [7,1,14,11]
print(S.checkIfExist(arr))
arr = [3,1,7,11]
print(S.checkIfExist(arr))
arr =[-2,0,10,-19,4,6,0]
print(S.checkIfExist(arr))