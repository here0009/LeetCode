"""
Given 2n balls of k distinct colors. You will be given an integer array balls of size k where balls[i] is the number of balls of color i. 

All the balls will be shuffled uniformly at random, then we will distribute the first n balls to the first box and the remaining n balls to the other box (Please read the explanation of the second example carefully).

Please note that the two boxes are considered different. For example, if we have two balls of colors a and b, and two boxes [] and (), then the distribution [a] (b) is considered different than the distribution [b] (a) (Please read the explanation of the first example carefully).

We want to calculate the probability that the two boxes have the same number of distinct balls.

 

Example 1:

Input: balls = [1,1]
Output: 1.00000
Explanation: Only 2 ways to divide the balls equally:
- A ball of color 1 to box 1 and a ball of color 2 to box 2
- A ball of color 2 to box 1 and a ball of color 1 to box 2
In both ways, the number of distinct colors in each box is equal. The probability is 2/2 = 1
Example 2:

Input: balls = [2,1,1]
Output: 0.66667
Explanation: We have the set of balls [1, 1, 2, 3]
This set of balls will be shuffled randomly and we may have one of the 12 distinct shuffles with equale probability (i.e. 1/12):
[1,1 / 2,3], [1,1 / 3,2], [1,2 / 1,3], [1,2 / 3,1], [1,3 / 1,2], [1,3 / 2,1], [2,1 / 1,3], [2,1 / 3,1], [2,3 / 1,1], [3,1 / 1,2], [3,1 / 2,1], [3,2 / 1,1]
After that we add the first two balls to the first box and the second two balls to the second box.
We can see that 8 of these 12 possible random distributions have the same number of distinct colors of balls in each box.
Probability is 8/12 = 0.66667
Example 3:

Input: balls = [1,2,1,2]
Output: 0.60000
Explanation: The set of balls is [1, 2, 2, 3, 4, 4]. It is hard to display all the 180 possible random shuffles of this set but it is easy to check that 108 of them will have the same number of distinct colors in each box.
Probability = 108 / 180 = 0.6
Example 4:

Input: balls = [3,2,1]
Output: 0.30000
Explanation: The set of balls is [1, 1, 1, 2, 2, 3]. It is hard to display all the 60 possible random shuffles of this set but it is easy to check that 18 of them will have the same number of distinct colors in each box.
Probability = 18 / 60 = 0.3
Example 5:

Input: balls = [6,6,6,6,6,6]
Output: 0.90327
 

Constraints:

1 <= balls.length <= 8
1 <= balls[i] <= 6
sum(balls) is even.
Answers within 10^-5 of the actual value will be accepted as correct.
"""






from functools import reduce
from math import factorial
from itertools import product
class Solution:
    #  from: https://leetcode.com/problems/probability-of-a-two-boxes-having-the-same-number-of-distinct-balls/discuss/661757/Python-10-Lines-90-Multionomial-coefficients-explained
    def multinomial(self, n):
        def multiply(a,b):
            return a*b
        return factorial(sum(n))/reduce(multiply, [factorial(i) for i in n])
  
    def getProbability(self, balls):

        k, n, Q = len(balls), sum(balls)// 2, 0 # sum(balls) is even
        arrays = [range(0, i+1) for i in balls]
        t = list(product(*arrays))  # t is sorted, so t[i] with t[-i-1] is the array, sum(t[i] + t[-i-1]) is equal to sum(balls)
        # print('balls', balls)
        # print('arrays', arrays)
        # print('t', t)
        # print(len(t))
        for i in range(len(t)):
            if sum(t[i]) == n and t[i].count(0) == t[-i-1].count(0):
                # print(t[i],t[-i-1])
                Q += self.multinomial(t[i]) * self.multinomial(t[-i-1]) 

        return Q / self.multinomial(list(balls))


from functools import reduce
from itertools import product
from math import factorial
class Solution:
    def getProbability(self, balls) -> float:
        def pmt(nums):
            """
            return the permutations of num in nums, pmt of [1,2,3] is sum(nums)!//(2!3!)
            """
            def mul(a,b):
                return a*b
            return factorial(sum(nums))//reduce(mul, [factorial(i) for i in nums])

        half_sum = sum(balls)//2
        Q = 0
        arrays = [range(i+1) for i in balls]
        # print(arrays)
        combs = list(product(*arrays))  # combs is sorted, so combs[i] with combs[-i-1] is the arrays, sum(combs[i] + combs[-i-1]) is equal to sum(balls), we can use a for loop to replce this
        # print(combs)
        for i in range(len(combs)):
            if sum(combs[i]) == half_sum and combs[i].count(0) == combs[-i-1].count(0):
                Q += pmt(combs[i]) * pmt(combs[-i-1])
        # print(pmt(balls))
        return Q/pmt(balls)



S = Solution_1()
balls = [1,1]
print(S.getProbability(balls))
balls = [2,1,1]
print(S.getProbability(balls))
balls = [3,5]
print(S.getProbability(balls))
balls = [1,2,1,2]
print(S.getProbability(balls))
balls = [3,2,1]
print(S.getProbability(balls))
balls = [6,6,6,6,6,6]
print(S.getProbability(balls))