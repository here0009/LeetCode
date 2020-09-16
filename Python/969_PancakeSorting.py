"""
Given an array of integers arr, sort the array by performing a series of pancake flips.

In one pancake flip we do the following steps:

Choose an integer k where 1 <= k <= arr.length.
Reverse the sub-array arr[1...k].
For example, if arr = [3,2,1,4] and we performed a pancake flip choosing k = 3, we reverse the sub-array [3,2,1], so arr = [1,2,3,4] after the pancake flip at k = 3.

Return the k-values corresponding to a sequence of pancake flips that sort arr. Any valid answer that sorts the array within 10 * arr.length flips will be judged as correct.

 

Example 1:

Input: arr = [3,2,4,1]
Output: [4,2,4,3]
Explanation: 
We perform 4 pancake flips, with k values 4, 2, 4, and 3.
Starting state: arr = [3, 2, 4, 1]
After 1st flip (k = 4): arr = [1, 4, 2, 3]
After 2nd flip (k = 2): arr = [4, 1, 2, 3]
After 3rd flip (k = 4): arr = [3, 2, 1, 4]
After 4th flip (k = 3): arr = [1, 2, 3, 4], which is sorted.
Notice that we return an array of the chosen k values of the pancake flips.
Example 2:

Input: arr = [1,2,3]
Output: []
Explanation: The input is already sorted, so there is no need to flip anything.
Note that other answers, such as [3, 3], would also be accepted.
 

Constraints:

1 <= arr.length <= 100
1 <= arr[i] <= arr.length
All integers in arr are unique (i.e. arr is a permutation of the integers from 1 to arr.length).
"""


class Solution:
    def pancakeSort(self, A):
        k = len(A)-1
        res = []
        sort_A = sorted(A)
        while sort_A:
            if A == sort_A:
                return res
            max_num = sort_A.pop()
            index = A.index(max_num)
            # print(index, max_num)
            if index != k: #flip the max num to the beginning, then filp it to the positon
                if index == 0:
                    res.append(k+1) #remove the largest one
                    A = A[1:k+1][::-1]
                else:
                    res.append(index+1)
                    A = A[:index+1][::-1] + A[index+1:]
                    res.append(k+1)
                    A = A[1:k+1][::-1]
            k -= 1
            # print(A, res)
        return res
# https://leetcode.com/problems/pancake-sorting/discuss/214215/Python-recursive-solution
class Solution:
    def pancakeSort(self, A):
        if len(A) == 1:
            return []
        max_id = A.index(max(A))
        A = A[:max_id+1][::-1] + A[max_id+1:]
        A = A[::-1]
        return [max_id+1, len(A)] + self.pancakeSort(A[:-1])

S = Solution()
A = [3,2,4,1]
print(S.pancakeSort(A))
A = [1,2,3]
print(S.pancakeSort(A))
