"""
Given two numbers arr1 and arr2 in base -2, return the result of adding them together.

Each number is given in array format:  as an array of 0s and 1s, from most significant bit to least significant bit.  For example, arr = [1,1,0,1] represents the number (-2)^3 + (-2)^2 + (-2)^0 = -3.  A number arr in array format is also guaranteed to have no leading zeros: either arr == [0] or arr[0] == 1.

Return the result of adding arr1 and arr2 in the same format: as an array of 0s and 1s with no leading zeros.

 

Example 1:

Input: arr1 = [1,1,1,1,1], arr2 = [1,0,1]
Output: [1,0,0,0,0]
Explanation: arr1 represents 11, arr2 represents 5, the output represents 16.
 

Note:

1 <= arr1.length <= 1000
1 <= arr2.length <= 1000
arr1 and arr2 have no leading zeros
arr1[i] is 0 or 1
arr2[i] is 0 or 1
"""
class Solution:
    def addNegabinary(self, arr1, arr2):
        def arrtoint(arr):
            res = 0
            arr = arr[::-1]
            for i,k in enumerate(arr):
                if k:
                    res += (-2)**i
            return res
        def inttoneg2(n):
            if n == 0:
                return [0]
            res = []
            while n :
                if n % 2 == 1:
                    res.append(1)
                    n -= 1
                else:
                    res.append(0)
                n = n // -2
            return res[::-1]
        # print (arrtoint(arr1), arrtoint(arr2))
        target = arrtoint(arr1)+arrtoint(arr2)
        # print(target)
        return inttoneg2(target)

s = Solution()
arr1 = [1,1,1,1,1]
arr2 = [1,0,1]
print(s.addNegabinary(arr1, arr2))

arr1 = [0]
arr2 = [0]
print(s.addNegabinary(arr1, arr2))


arr1 = [1]
arr2 = [1]
print(s.addNegabinary(arr1, arr2))