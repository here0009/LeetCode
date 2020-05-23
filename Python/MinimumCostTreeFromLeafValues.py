"""
Given an array arr of positive integers, consider all binary trees such that:

Each node has either 0 or 2 children;
The values of arr correspond to the values of each leaf in an in-order traversal of the tree.  (Recall that a node is a leaf if and only if it has 0 children.)
The value of each non-leaf node is equal to the product of the largest leaf value in its left and right subtree respectively.
Among all possible binary trees considered, return the smallest possible sum of the values of each non-leaf node.  It is guaranteed this sum fits into a 32-bit integer.

 

Example 1:

Input: arr = [6,2,4]
Output: 32
Explanation:
There are two possible trees.  The first has non-leaf node sum 36, and the second has non-leaf node sum 32.

    24            24
   /  \\          /  \
  12   4        6    8
 /  \\               / \
6    2             2   4
 

Constraints:

2 <= arr.length <= 40
1 <= arr[i] <= 15
It is guaranteed that the answer fits into a 32-bit signed integer (ie. it is less than 2^31).
"""

from collections import deque
class Solution_1:
    def mctFromLeafValues(self, arr) -> int:
        """
        Thoughts: Hoffman tree
        wrong, the arr is inorder traverse of the leaf nodes
        """
        res = 0
        arr = deque(sorted(arr))
        left = arr.popleft()
        while len(arr) > 1:
            mid = arr.popleft()
            right = arr[0]
            if left <= right: #drop left
                res += left*mid
                left = mid
            else: #drop 
                res += mid*right
                mid = max(mid,right)
            print(arr,res,p*q)
        return res

class Solution:
    def mctFromLeafValues(self, arr) -> int:
        """
        Thoughts: a node in an arr can only merge with its two neighbors, when the merge happens, two became one, and the value of the larger was taken, and the product of the two nodes was added to the res.
        return the res
        Using a stack to keep a mountain shaped structure, the valley multiply to its min adjenct neighbor, and then droped. Repeat this process until only two nodes in the stack
        """
        stack = [float('inf')]
        res = 0
        for num in arr:
            while num > stack[-1]:
                v = stack.pop()
                res += min(num, stack[-1])*v
            stack.append(num)
        while len(stack) > 2: #now stack is a decreasing list
            v = stack.pop()
            res += v*stack[-1]
        return res


from collections import deque
class Solution:
    def mctFromLeafValues(self, arr) -> int:
        res = 0
        while len(arr) > 1:
            min_index = arr.index(min(arr))
            if min_index == 0:
                res += arr[min_index] * arr[1]
            elif min_index == len(arr) - 1:
                res += arr[min_index] * arr[min_index-1]
            else:
                res += arr[min_index] * min(arr[min_index-1], arr[min_index+1])
            arr.pop(min_index)
        return res
             
s = Solution()
arr = [6,2,4]
print(s.mctFromLeafValues(arr))

arr = [7,12,8,10]
print(s.mctFromLeafValues(arr))
"""
Output
256
Expected
284
"""
