"""
There are several cards arranged in a row, and each card has an associated number of points The points are given in the integer array cardPoints.

In one step, you can take one card from the beginning or from the end of the row. You have to take exactly k cards.

Your score is the sum of the points of the cards you have taken.

Given the integer array cardPoints and the integer k, return the maximum score you can obtain.

 

Example 1:

Input: cardPoints = [1,2,3,4,5,6,1], k = 3
Output: 12
Explanation: After the first step, your score will always be 1. However, choosing the rightmost card first will maximize your total score. The optimal strategy is to take the three cards on the right, giving a final score of 1 + 6 + 5 = 12.
Example 2:

Input: cardPoints = [2,2,2], k = 2
Output: 4
Explanation: Regardless of which two cards you take, your score will always be 4.
Example 3:

Input: cardPoints = [9,7,7,9,7,7,9], k = 7
Output: 55
Explanation: You have to take all the cards. Your score is the sum of points of all cards.
Example 4:

Input: cardPoints = [1,1000,1], k = 1
Output: 1
Explanation: You cannot take the card in the middle. Your best score is 1. 
Example 5:

Input: cardPoints = [1,79,80,1,1,1,200,1], k = 3
Output: 202
 

Constraints:

1 <= cardPoints.length <= 10^5
1 <= cardPoints[i] <= 10^4
1 <= k <= cardPoints.length
"""
from functools import lru_cache
class Solution:
    def maxScore(self, cardPoints, k: int) -> int:
        """
        Time Limit Exceeded
        """

        @lru_cache(None)
        def dp(start, end, length):
            # print(start, end, length)
            if end-start == length:
                return preSum[end] - preSum[start]
            if end-start < length or length <= 0:
                return 0
            return max(cardPoints[start]+dp(start+1, end, length-1), dp(start, end-1, length-1)+cardPoints[end-1])

        preSum = [0]
        for c in cardPoints:
            preSum.append(preSum[-1] + c)
        # print(preSum)

        return dp(0, len(cardPoints),k)

from functools import lru_cache
class Solution:
    def maxScore(self, cardPoints, k: int) -> int:
        """
        TLE
        """
        @lru_cache(None)
        def dp(start, end, length):
            if end-start+1 == length:
                return sum(cardPoints[start:end+1])
            if length == 1:
                return max(cardPoints[start], cardPoints[end])
            return max(dp(start+1, end, length-1)+cardPoints[start], dp(start, end-1, length-1)+cardPoints[end])

        return dp(0, len(cardPoints)-1,k)


class Solution:
    def maxScore(self, cardPoints, k: int) -> int:
        """
        find the max sum of cards on both ends is equal to find the min sum of a subarry, the length of which is len(cardPoints)-k
        """
        size = len(cardPoints)-k
        tmp = sum(cardPoints[:size])
        res = tmp
        for i in range(len(cardPoints)-size):
            tmp = tmp - cardPoints[i] + cardPoints[i+size]
            res = min(res, tmp)
        return sum(cardPoints) - res


class Solution:
    def maxScore(self, cardPoints, k: int) -> int:
        score = sum(cardPoints[:k])
        index = 1
        res = score
        while index <= k:
            score = score - cardPoints[k-index] + cardPoints[-index] #remove the rightmost left, add the leftmost right
            index += 1
            res = max(res, score)
        return res


S = Solution()
cardPoints = [1,2,3,4,5,6,1]
k = 3
print(S.maxScore(cardPoints, k))
cardPoints = [2,2,2]
k = 2
print(S.maxScore(cardPoints, k))
cardPoints = [9,7,7,9,7,7,9]
k = 7
print(S.maxScore(cardPoints, k))
cardPoints = [1,1000,1]
k = 1
print(S.maxScore(cardPoints, k))
cardPoints = [1,79,80,1,1,1,200,1]
k = 3
print(S.maxScore(cardPoints, k))

cardPoints = [100,40,17,9,73,75]
k = 3
print(S.maxScore(cardPoints, k))

cardPoints = [1,2,3,4,5,6,1]
k = 3
print(S.maxScore(cardPoints, k))