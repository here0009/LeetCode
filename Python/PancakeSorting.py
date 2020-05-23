"""
Given an array A, we can perform a pancake flip: We choose some positive integer k <= A.length, then reverse the order of the first k elements of A.  We want to perform zero or more pancake flips (doing them one after another in succession) to sort the array A.

Return the k-values corresponding to a sequence of pancake flips that sort A.  Any valid answer that sorts the array within 10 * A.length flips will be judged as correct.

 

Example 1:

Input: [3,2,4,1]
Output: [4,2,4,3]
Explanation: 
We perform 4 pancake flips, with k values 4, 2, 4, and 3.
Starting state:       A = [3, 2, 4, 1]
After 1st flip (k=4): A = [1, 4, 2, 3]
After 2nd flip (k=2): A = [4, 1, 2, 3]
After 3rd flip (k=4): A = [3, 2, 1, 4]
After 4th flip (k=3): A = [1, 2, 3, 4], which is sorted. 
43, 34, ,3
Example 2:

Input: [1,2,3]
Output: []
Explanation: The input is already sorted, so there is no need to flip anything.
Note that other answers, such as [3, 3], would also be accepted.
 

Note:

1 <= A.length <= 100
A[i] is a permutation of [1, 2, ..., A.length]
"""
from collections import deque
class Solution_1:
    def pancakeSort(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        Thoughts:
        Wrong Answer
        """
        def flip(A,n):
            """
            flip the first n elements of A
            """
            res = []
            return A[:n][::-1] + A[n:]

        # flip_history = deque()
        while True:
            break_flag = False
            for i in range(len(A)-1,0,-1):
                print("i",i)
                if A[i-1] > A[i]:
                    if i == 1:
                        A = flip(A,2)
                    else:
                        A = flip(A, i+1)
                    print(A)
                    break_flag = True
            if not break_flag:
                break
        print(A)
        return 0


class Solution:
    def pancakeSort(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        Thoughts:
        find the maximum number in A, then switch it to the start of A, then switch it to the end.
        then the second maximum, third maximum and so on
        """
        res = []
        len_A = len(A)
        sorted_A = sorted(A, reverse = True)
        for i in range(len_A):
            k = (A.index(sorted_A[i]))
            if k+1 != len(A):
                if k+1 != 1:
                    res.append(k+1)
                if len(A) != 1:
                    res.append(len(A))
            A = A[k+1:]+A[:k][::-1]
            
            
        return res

s = Solution()
A = [3,2,4,1]
print(s.pancakeSort(A))
A = [1,2,3]
print(s.pancakeSort(A))