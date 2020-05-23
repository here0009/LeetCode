"""
Given an array A of positive lengths, return the largest perimeter of a triangle with non-zero area, formed from 3 of these lengths.

If it is impossible to form any triangle of non-zero area, return 0.

 

Example 1:

Input: [2,1,2]
Output: 5
Example 2:

Input: [1,2,1]
Output: 0
Example 3:

Input: [3,2,3,4]
Output: 10
Example 4:

Input: [3,6,2,3]
Output: 8
 

Note:

3 <= A.length <= 10000
1 <= A[i] <= 10^6
"""
class Solution_1:
    def largestPerimeter(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        
        def findLargestPeri(sub_A):
            if len(sub_A) == 3:
                if sub_A[0] >= sub_A[1] + sub_A[2]:
                    return 0
                else:
                    return sum(sub_A[0:3])
                
            if sub_A[0] < sub_A[1] + sub_A[2]:
                return sum(sub_A[0:3])
            else:
                return findLargestPeri(sub_A[1:])

        A = sorted(A, reverse = True)
        return findLargestPeri(A)

class Solution:
    def largestPerimeter(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        A = sorted(A, reverse = True)
        for i in range(0, len(A)-2):
            if A[i] < A[i+1] + A[i+2]:
                return sum(A[i:i+3])
        return 0

s = Solution()
A = [2,1,2]
print(s.largestPerimeter(A))

A = [1,2,1]
print(s.largestPerimeter(A))

A = [3,2,3,4]
print(s.largestPerimeter(A))

A = [3,6,2,3]
print(s.largestPerimeter(A))

A = [1,1,1]
print(s.largestPerimeter(A))