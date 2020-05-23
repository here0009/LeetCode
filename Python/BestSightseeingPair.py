"""
Given an array A of positive integers, A[i] represents the value of the i-th sightseeing spot, and two sightseeing spots i and j have distance j - i between them.

The score of a pair (i < j) of sightseeing spots is (A[i] + A[j] + i - j) : the sum of the values of the sightseeing spots, minus the distance between them.

Return the maximum score of a pair of sightseeing spots.

Example 1:

Input: [8,1,5,2,6]
Output: 11
Explanation: i = 0, j = 2, A[i] + A[j] + i - j = 8 + 5 + 0 - 2 = 11
 

Note:

2 <= A.length <= 50000
1 <= A[i] <= 1000
"""
class Solution:
    def maxScoreSightseeingPair(self, A) -> int:
        # start_score = []
        start_score = 0 + A[0]
        res = start_score + A[1] - 1
        for i in range(1, len(A)):
            # print("start_score",start_score)
            end_score = A[i]-i
            # print("end_score",end_score)
            res = max(start_score+end_score, res)
            # print("res",res)
            start_score = max(start_score, A[i]+i) 
        return res

s = Solution()
# A = [8,1,5,2,6]
# print(s.maxScoreSightseeingPair(A))

# A = [2,2,2]
# print(s.maxScoreSightseeingPair(A))

A = [1,3,5]
print(s.maxScoreSightseeingPair(A))