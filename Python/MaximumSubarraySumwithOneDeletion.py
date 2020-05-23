"""
Given an array of integers, return the maximum sum for a non-empty subarray (contiguous elements) with at most one element deletion. In other words, you want to choose a subarray and optionally delete one element from it so that there is still at least one element left and the sum of the remaining elements is maximum possible.

Note that the subarray needs to be non-empty after deleting one element.

 

Example 1:

Input: arr = [1,-2,0,3]
Output: 4
Explanation: Because we can choose [1, -2, 0, 3] and drop -2, thus the subarray [1, 0, 3] becomes the maximum value.
Example 2:

Input: arr = [1,-2,-2,3]
Output: 3
Explanation: We just choose [3] and it's the maximum sum.
Example 3:

Input: arr = [-1,-1,-1,-1]
Output: -1
Explanation: The final subarray needs to be non-empty. You can't choose [-1] and delete -1 from it, then get an empty subarray to make the sum equals to 0.
 

Constraints:

1 <= arr.length <= 10^5
-10^4 <= arr[i] <= 10^4
"""
"""
Thoughts:
record the start and end index of maxSum, then extend it, one gap was allowed
"""
class Solution_1:
    def maximumSum(self, arr):
        """
        it is not right for test case [11,-10,-11,8,7,-6,9,4,11,6,5,0]
        """
        tmp = arr[0]
        res = arr[0]
        min_val = 0
        for v in arr[1:]:
            if v > tmp+v: #new start, new min_val
                tmp = v
                min_val = 0
            else:
                if v < min_val: #v < min_val, v is new min_val, add previous min_val to tmp
                    tmp += min_val
                    min_val = v
                else:
                    tmp = tmp + v
            res = max(tmp, res)
            print(v, min_val, tmp, res)
        return res


class Solution_2:
    def maximumSum(self, arr):
        tmp = arr[0]
        res = arr[0]
        min_val = 0
        for v in arr[1:]:
            if v > tmp+v: #new start, new min_val
                tmp = v
                min_val = 0
            else:
                if v < min_val: #v < min_val, v is new min_val, add previous min_val to tmp
                    tmp += min_val
                    min_val = v
                else:
                    tmp = tmp + v
            res = max(tmp, res)
            print(v, min_val, tmp, res)
        return res

class Solution:
    def maximumSum(self, arr):
        """
        Thoughts: using dp to solve it, maintain two variables, one for total sum, one for total sum with one deletion
        """
        noDelSum = arr[0]
        oneDelSum = float('-inf')
        res = arr[0]
        for n in arr[1:]:
            oneDelSum = max(oneDelSum+n, noDelSum)
            noDelSum = max(n, noDelSum+n)
            res = max(res, oneDelSum, noDelSum)
        return res



s = Solution()
arr = [1,-2,0,3]
print(s.maximumSum(arr))

arr = [1,-2,-2,3]
print(s.maximumSum(arr))

arr = [-1,-1,-1,-1]
print(s.maximumSum(arr))


arr = [8,-1,6,-7,-4,5,-4,7,-6]
print(s.maximumSum(arr))

arr = [-5,-2,3,-5]
print(s.maximumSum(arr))

arr = [1,-4,-5,-2,5,0,-1,2]
print(s.maximumSum(arr))

arr = [11,-10,-11,8,7,-6,9,4,11,6,5,0]
print(s.maximumSum(arr))