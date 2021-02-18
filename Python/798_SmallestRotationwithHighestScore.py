"""
 Given an array A, we may rotate it by a non-negative integer K so that the array becomes A[K], A[K+1], A{K+2], ... A[A.length - 1], A[0], A[1], ..., A[K-1].  Afterward, any entries that are less than or equal to their index are worth 1 point. 

For example, if we have [2, 4, 1, 3, 0], and we rotate by K = 2, it becomes [1, 3, 0, 2, 4].  This is worth 3 points because 1 > 0 [no points], 3 > 1 [no points], 0 <= 2 [one point], 2 <= 3 [one point], 4 <= 4 [one point].

Over all possible rotations, return the rotation index K that corresponds to the highest score we could receive.  If there are multiple answers, return the smallest such index K.

Example 1:
Input: [2, 3, 1, 4, 0]
Output: 3
Explanation:  
Scores for each K are listed below: 
K = 0,  A = [2,3,1,4,0],    score 2
K = 1,  A = [3,1,4,0,2],    score 3
K = 2,  A = [1,4,0,2,3],    score 3
K = 3,  A = [4,0,2,3,1],    score 4
K = 4,  A = [0,2,3,1,4],    score 3
So we should choose K = 3, which has the highest score.

 

Example 2:
Input: [1, 3, 0, 2, 4]
Output: 0
Explanation:  A will always have 3 points no matter how it shifts.
So we will choose the smallest K, which is 0.
Note:

A will have length at most 20000.
A[i] will be in the range [0, A.length].
"""


from typing import List
class Solution:
    def bestRotation(self, A: List[int]) -> int:
        """
        Thoughts:
        rounds[i] record the score we got shift i round
        instead of shift A, we can shift the index
        01234
        40123
        34012
        23401
        12340
        then we use bisect to check the score we can get for each round
        """
        len_A = len(A)
        rounds = [0] * len_A
        for i, v in enumerate(A):
            lst = list(reversed(list(range(i + 1, len_A)) + list(range(i + 1))))
            print(i, v, lst)
        pass



from typing import List
class Solution:
    def bestRotation(self, A: List[int]) -> int:
        """
        Thoughts:
        rounds[i] record the score we got shift i round
        instead of shift A, we can shift the index
        23140

        01234
        40123
        34012
        23401
        12340
        
        denote the original index as i and value as v, j as the index after shift
        j = (i - shift) % len_A, so shift = (i - j) % len_A
        
        j = 0, shift = i
        one more shit(i + 1), j is len_A - 1, because A[i] will be in the range [0, A.length], so that is valid
        
        j = v, shift = i - v
        one more shift(i - v + 1), j is v - 1 and that's not valid

        we denote left as i+1, right as i-v+1
        the shift between left to right is valid, if left >= right, then we should addhere end to begin, set round[0] as 1
        """
        len_A = len(A)
        rounds = [0] * len_A
        for i, v in enumerate(A):
            left = (i + 1) % len_A
            right = (i - v + 1) % len_A
            if left >= right:
                rounds[0] += 1
            rounds[left] += 1
            rounds[right] -= 1

        tmp = 0
        res = 0
        K = 0
        for i, v in enumerate(rounds):
            tmp += v
            if tmp > res:
                res = tmp
                K = i
        return K

S = Solution()
A = [2, 3, 1, 4, 0]
print(S.bestRotation(A))
A = [1, 3, 0, 2, 4]
print(S.bestRotation(A))