"""
n passengers board an airplane with exactly n seats. The first passenger has lost the ticket and picks a seat randomly. But after that, the rest of passengers will:

Take their own seat if it is still available, 
Pick other seats randomly when they find their seat occupied 
What is the probability that the n-th person can get his own seat?

 

Example 1:

Input: n = 1
Output: 1.00000
Explanation: The first person can only get the first seat.
Example 2:

Input: n = 2
Output: 0.50000
Explanation: The second person has a probability of 0.5 to get the second seat (when first person gets the first seat).
 

Constraints:

1 <= n <= 10^5
"""
class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        """
        wrong answer
        """

        def f(n):
            """
            f(n) stands for the probability of the preson causing the nth person choose the wrong seat, it equals to  the person choose the desired seat directly, that is 1/n, or choose the seat of the next person, and the next person choose wrong too, it is f(n-1)*1/n
            """
            if n == 1:
                return 0
            else:
                return (1+f(n-1))/n
        
        return 1-f(n)


class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        prob,acc_prob = 1/n,1/n 
        #prob record the probability that person choose the right seat, 
        #and acc_prob is the accumulation of probability that the specific i-th seat is not chosen. (they are the same for a not chosen seat)
        #If i-th seat is not chosen yet, person i will definitely chose it, the probability is 1-acc_prob.
        #Otherwise i-th person will choose a wrong seat, the seats that unchosen is n-i, 
        #so the accumuation probability for the remaining seats are += (1-prob)/(n-i)
        i = 1
        while i < n:
            prob = (1-acc_prob)
            acc_prob += (1-prob)/(n-i)
            i += 1
        return prob

"""
https://leetcode.com/problems/airplane-seat-assignment-probability/discuss/497903/The-top-answer-is-wrong.-Here-is-the-correct-proof.

Let f(n) be the probability that the n-th passenger will get his own seat.
If the 1st passenger get the 1st seat, then everyone will get their own seats, so the n-th passenger gets his own seat with probability: 1/n
If the 1st passenger get the 2nd seat, with probability 1/n, then n-1 seats left. Here, the 2nd passenger faces the same situation of the 1st passenger, he can just randomly choose a seat. So it is the same question but n becomes n-1. In this situation, the probability that the n-th passenger gets his seat is f(n-1). So the final probability is f(n-1)*(1/n)
If the 1st passenger get the 3rd seat, ..., the probability is f(n-2)*(1/n)
...
....
......
Then f(n) = 1/n + f(n-1)*(1/n)+ f(n-2)*(1/n) + ... + f(2)*(1/n)
Let's solve this recursive formula:
nf(n) = 1+ f(n-1)+ f(n-2) + ... + f(2) ...... Equation 1
(n-1)f(n-1) = 1+ f(n-2)+ ... + f(2) ...... Equation 2
Use Equation 1 - Equation 2
nf(n) - (n-1)f(n-1) = f(n-1)
so
f(n) = f(n-1) when n>=3
We already know f(2)=0.5
So f(n) = 0.5 when n>=2
"""

s = Solution()
for i in range(1,10):
    print(i, s.nthPersonGetsNthSeat(i))

# i = 3
# print(i, s.nthPersonGetsNthSeat(i))
# Output
# 0.66667
# Expected
# 0.50000

i = 4
# Output
# 0.55556
# Expected
# 0.50000