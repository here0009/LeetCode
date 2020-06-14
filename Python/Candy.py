"""
There are N children standing in a line. Each child is assigned a rating value.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
What is the minimum candies you must give?

Example 1:

Input: [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
Example 2:

Input: [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
             The third child gets 1 candy because it satisfies the above two conditions.
"""


class Solution:
    """
    Thoughts: Decreasing stack
    wrong answer
    """
    def candy(self, ratings) -> int:
        print(ratings)
        stack = []
        res = 0
        start = 1
        for n in ratings:
            print(n, stack, res, start)
            if stack and n >= stack[-1]:
                res += (len(stack) + start) * len(stack)//2
                if n > stack[-1]:
                    start = 3  # start from 2
                elif n == stack[-1]:
                    start = 1  # start from 1
                stack = [n]
            else:
                stack.append(n)
        print(stack, res, start)
        res += (len(stack) + start) * len(stack)//2
        return res


class Solution:
    def candy(self, ratings) -> int:
        length = len(ratings)
        res = [1] * length
        lbase, rbase = 1, 1
        for i in range(1, length):
            if ratings[i] > ratings[i-1]:
                lbase += 1
            else:
                lbase = 1
            res[i] = lbase
        for i in range(length - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                rbase += 1
            else:
                rbase = 1
            res[i] = max(res[i], rbase)
        # print(res)
        return sum(res)

class Solution:
    def candy(self, ratings):
        res = len(ratings) * [1]
        for i in xrange(1, len(ratings)):  # from left to right
            if ratings[i] > ratings[i-1]:
                res[i] = res[i-1] + 1
        for i in xrange(len(ratings)-1, 0, -1):  # from right to left
            if ratings[i-1] > ratings[i]:
                res[i-1] = max(res[i-1], res[i]+1)
        return sum(res)
S = Solution()
ratings = [1,0,2]
print(S.candy(ratings))

ratings = [1,2,2]
print(S.candy(ratings))

ratings = [1,3,2,2,1]
print(S.candy(ratings))
# Output
# 9
# Expected
# 7