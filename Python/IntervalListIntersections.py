"""
Given two lists of closed intervals, each list of intervals is pairwise disjoint and in sorted order.

Return the intersection of these two interval lists.

(Formally, a closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.  The intersection of two closed intervals is a set of real numbers that is either empty, or can be represented as a closed interval.  For example, the intersection of [1, 3] and [2, 4] is [2, 3].)

 

Example 1:



Input: A = [[0,2],[5,10],[13,23],[24,25]], B = [[1,5],[8,12],[15,24],[25,26]]
Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
Reminder: The inputs and the desired output are lists of Interval objects, and not arrays or lists.
 

Note:

0 <= A.length < 1000
0 <= B.length < 1000
0 <= A[i].start, A[i].end, B[i].start, B[i].end < 10^9
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
"""
"""
Thoughts: save the interval tha get the long ending
"""
class Solution:
    def intervalIntersection(self, A, B):
        def intersect(a,b):
            ai,aj = a
            bi,bj = b
            resi,resj = max(ai,bi), min(aj,bj)
            if resi <= resj:
                self.res.append([resi,resj])

        flag = 0        
        self.res = []
        if len(A) == 0 or len(B) == 0:
            return self.res
        len_a, len_b = len(A), len(B)
        index_a, index_b = 0, 0
        while index_a < len_a and index_b < len_b:
            intersect(A[index_a],B[index_b])
            ai,aj = A[index_a]
            bi,bj = B[index_b]
            if aj <= bj:
                index_a += 1
            else:
                index_b += 1

        return self.res

s = Solution()
A = [[0,2],[5,10],[13,23],[24,25]]
B = [[1,5],[8,12],[15,24],[25,26]]
print(s.intervalIntersection(A,B))