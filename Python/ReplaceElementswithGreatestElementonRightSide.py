"""
Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

After doing so, return the array.

 

Example 1:

Input: arr = [17,18,5,4,6,1]
Output: [18,6,6,6,1,-1]
 

Constraints:

1 <= arr.length <= 10^4
1 <= arr[i] <= 10^5
"""


class Solution:
    def replaceElements(self, arr):
        stack = [(0,float('inf'))]
        length = len(arr)
        res = []
        for i, v in enumerate(arr):
            while stack and v > stack[-1][1]:
                stack.pop()
            stack.append((i, v))
        # print(stack)

        for j in range(1, len(stack)):
            res.extend([stack[j][1]]*(stack[j][0] - stack[j-1][0]))
        res.append(-1)
        return res


class Solution:
    def replaceElements(self, arr):
        max_v, length = float('-inf') , len(arr)
        for i in range(length-1, -1, -1):
            arr[i], max_v = max_v, max(max_v, arr[i])
        arr[-1] = -1
        return arr

S = Solution()
arr = [17,18,5,4,6,1]
print(S.replaceElements(arr))
arr = [1]
print(S.replaceElements(arr))