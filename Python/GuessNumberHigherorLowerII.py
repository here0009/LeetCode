"""
We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I'll tell you whether the number I picked is higher or lower.

However, when you guess a particular number x, and you guess wrong, you pay $x. You win the game when you guess the number I picked.

Example:

n = 10, I pick 8.

First round:  You guess 5, I tell you that it's higher. You pay $5.
Second round: You guess 7, I tell you that it's higher. You pay $7.
Third round:  You guess 9, I tell you that it's lower. You pay $9.

Game over. 8 is the number I picked.

You end up paying $5 + $7 + $9 = $21.
Given a particular n ≥ 1, find out how much money you need to have to guarantee a win.
"""


class Solution:
    """
    Thoughts: the min guess time is the same, log2N, so when n is the largest number, the max money you have to pay. (wrong idea)

    the guess time is not important, the penalty money is imporatant, so we need to find a break point that got the equal penalty money on both sides.
    """
    def getMoneyAmount(self, n: int) -> int:
        def guessN(target):
            res = 0
            start, end = 1, n
            # target = n
            while start <= end:
                mid = (start + end) //2
                # print(mid)
                if mid < target:
                    start = mid + 1
                    res += mid
                elif mid > target:
                    end = mid - 1
                    res += mid
                else:
                    return res

        for i in range(1,n):
            print(i, guessN(i))
                
        
class Solution:
    def getMoneyAmount(self, n: int) -> int:
        """
        the guess time is not important, the penalty money is imporatant, so we need to find a break point that got the equal penalty money on both sides.
        just try the break point the got similar sum on both sides.
        It looks difficult to came up with the solution, try hint methond: dp
        use cost[i][j] to record the penalty money for start with i, end with j.
        cost[i][i] will be 0
        """
        cost = [[0]*(n+1) for _ in range(n+1)]
        for low in range(n,0,-1):
            for high in range(low+1, n+1):
                cost[low][high] = min(x + max(cost[low][x-1], cost[x+1][high]) for x in range(low,high))
        # for row in cost:
        #     print(row)
        return cost[1][n]




s = Solution()
print(s.getMoneyAmount(10))