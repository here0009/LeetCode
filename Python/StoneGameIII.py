"""
Alice and Bob continue their games with piles of stones. There are several stones arranged in a row, and each stone has an associated value which is an integer given in the array stoneValue.

Alice and Bob take turns, with Alice starting first. On each player's turn, that player can take 1, 2 or 3 stones from the first remaining stones in the row.

The score of each player is the sum of values of the stones taken. The score of each player is 0 initially.

The objective of the game is to end with the highest score, and the winner is the player with the highest score and there could be a tie. The game continues until all the stones have been taken.

Assume Alice and Bob play optimally.

Return "Alice" if Alice will win, "Bob" if Bob will win or "Tie" if they end the game with the same score.

 

Example 1:

Input: values = [1,2,3,7]
Output: "Bob"
Explanation: Alice will always lose. Her best move will be to take three piles and the score become 6. Now the score of Bob is 7 and Bob wins.
Example 2:

Input: values = [1,2,3,-9]
Output: "Alice"
Explanation: Alice must choose all the three piles at the first move to win and leave Bob with negative score.
If Alice chooses one pile her score will be 1 and the next move Bob's score becomes 5. The next move Alice will take the pile with value = -9 and lose.
If Alice chooses two piles her score will be 3 and the next move Bob's score becomes 3. The next move Alice will take the pile with value = -9 and also lose.
Remember that both play optimally so here Alice will choose the scenario that makes her win.
Example 3:

Input: values = [1,2,3,6]
Output: "Tie"
Explanation: Alice cannot win this game. She can end the game in a draw if she decided to choose all the first three piles, otherwise she will lose.
Example 4:

Input: values = [1,2,3,-1,-2,-3,7]
Output: "Alice"
Example 5:

Input: values = [-1,-2,-3]
Output: "Tie"
 

Constraints:

1 <= values.length <= 50000
-1000 <= values[i] <= 1000
"""
from functools import lru_cache
class Solution:
    def stoneGameIII(self, stoneValue) -> str:
        length = len(stoneValue)
        
        @lru_cache(None)
        def dp(index,flag):
            #return the max value for alice start from index
            if index == length:
                return 0,0
            res_a, res_b = -float('inf'),-float('inf')
            if flag == 'A':
                next_flag = 'B'
            else:
                next_flag = 'A'
            for i in range(1,4):
                if index+i > length:
                    break
                next_a, next_b = dp(index+i,next_flag)
                if flag == 'A':
                    if sum(stoneValue[index:index+i])+next_a > res_a:
                        res_a = sum(stoneValue[index:index+i])+next_a
                        res_b = next_b
                else:
                    if sum(stoneValue[index:index+i])+next_b > res_b:
                        res_b = sum(stoneValue[index:index+i])+next_b
                        res_a = next_a
            return res_a, res_b

        Alice_score,Bob_score = dp(0,'A')
        # print(Alice_score, Bob_score, sum(stoneValue))
        if Alice_score > Bob_score:
            return 'Alice'
        elif Alice_score < Bob_score:
            return 'Bob'
        else:
            return 'Tie'


from functools import lru_cache
class Solution:
    """
    more concise one
    """
    def stoneGameIII(self, stoneValue) -> str:
        @lru_cache(None)
        def dp(index,flag):
            #return the max value for alice or bob start from index according to flag
            if index == length:
                return 0,0
            res_a, res_b = -float('inf'),-float('inf')
            for i in range(1,4):
                if index+i > length:
                    break
                if flag == 'A':
                    next_a, next_b = dp(index+i,'B')
                    tmp_a = sum(stoneValue[index:index+i])+next_a
                    if  tmp_a > res_a:
                        res_a,res_b = tmp_a,next_b
                else:
                    next_a, next_b = dp(index+i,'A')
                    tmp_b = sum(stoneValue[index:index+i])+next_b
                    if tmp_b > res_b:
                        res_a,res_b = next_a,tmp_b
            return res_a, res_b

        length = len(stoneValue)
        Alice_score,Bob_score = dp(0,'A')
        print(Alice_score, Bob_score, sum(stoneValue))
        if Alice_score > Bob_score:
            return 'Alice'
        elif Alice_score < Bob_score:
            return 'Bob'
        else:
            return 'Tie'


from functools import lru_cache
class Solution:
    def stoneGameIII(self, stoneValue) -> str:
        def dp(index,flag):
            #return the max value for alice or bob start from index according to flag
            if index in memo:
                return memo[index]
            res_a, res_b = -float('inf'),-float('inf')
            for i in range(1,4):
                if index+i > length:
                    break
                if flag == 'A':
                    next_b, next_a = dp(index+i,'B')
                    tmp_a = sum(stoneValue[index:index+i])+next_a
                    if  tmp_a > res_a:
                        res_a,res_b = tmp_a,next_b
                else:
                    next_a, next_b = dp(index+i,'A')
                    tmp_b = sum(stoneValue[index:index+i])+next_b
                    if tmp_b > res_b:
                        res_a,res_b = next_a,tmp_b

            if flag == 'A':
                memo[index] = (res_a, res_b)
            else:
                memo[index] = (res_b, res_a)

            return memo[index]

        length = len(stoneValue)
        memo = {length:(0,0)}
        Alice_score,Bob_score = dp(0,'A')
        print(Alice_score, Bob_score, sum(stoneValue))
        if Alice_score > Bob_score:
            return 'Alice'
        elif Alice_score < Bob_score:
            return 'Bob'
        else:
            return 'Tie'


from functools import lru_cache
class Solution:
    def stoneGameIII(self, stoneValue) -> str:
        @lru_cache(None)
        def dp(index):
            #return the max value for alice or bob start from index
            if index >= length:
                return 0
            res = -float('inf')
            for i in range(1,4):
                if index+i > length:
                    break 
                # tmp = acc_A[-1]-acc_A[index+i]-dp(index+i) #total minus b is a
                # res = max(res, sum(stoneValue[index:index+i])+tmp)
                res = max(res, acc_A[-1]-acc_A[index]-dp(index+i))
            return res

        length = len(stoneValue)
        acc_A = [0]
        curr_sum = 0
        for i in range(length):
            curr_sum += stoneValue[i]
            acc_A.append(curr_sum)
        # print(acc_A) #acc_A[i] = sum(stoneValue[:i])

        Alice_score = dp(0)
        Bob_score = acc_A[-1] - Alice_score
        # print(Alice_score, Bob_score, sum(stoneValue))
        if Alice_score > Bob_score:
            return 'Alice'
        elif Alice_score < Bob_score:
            return 'Bob'
        else:
            return 'Tie'

"""
https://leetcode.com/problems/stone-game-iii/discuss/564266/C%2B%2BPython-Easy-and-Concise-Solution-with-Minimax-Algorithm
"""
class Solution:
    def stoneGameIII(self, stoneValue) -> str:
        seen = {}

        def maxWin(idx):

            if idx == len(stoneValue):
                return 0
            if idx in seen:
                return seen[idx]
            
            myStone = 0
            res = float('-inf')
            for i in range(idx, min(idx + 3, len(stoneValue))):
                myStone += stoneValue[i]
                res = max(res, myStone - maxWin(i+1))
            seen[idx] = res
            print(idx,res)
            return res
        
        res = maxWin(0)
        if res > 0:
            return 'Alice'
        elif res < 0:
            return 'Bob'
        else:
            return 'Tie'


class Solution:
    """
    dp bottom up
    """
    def stoneGameIII(self, stoneValue) -> str:
        length = len(stoneValue)
        acc_A = [0]
        curr_sum = 0
        for i in range(length):
            curr_sum += stoneValue[i]
            acc_A.append(curr_sum)

        dp = [-float('inf')]*length + 3*[0] #dp[index] represents the max score we can get at index, so dp[length-1] = stoneValue[-1], dp[length] to dp[length+3] will be 0, but they would be used in  the calculation
        for index in range(length-1, -1, -1):
            for j in range(1,4):
                dp[index] = max(dp[index], acc_A[-1]-acc_A[index]-dp[index+j])

        # print(dp)
        Alice_score, Bob_score = dp[0], acc_A[-1]-dp[0]
        return ['Tie','Alice', 'Bob'] [(Alice_score > Bob_score) - (Alice_score < Bob_score)] 

S = Solution()
values = [1,2,3,7]
print(S.stoneGameIII(values))
values = [1,2,3,-9]
print(S.stoneGameIII(values))
values = [1,2,3,6]
print(S.stoneGameIII(values))
values = [1,2,3,-1,-2,-3,7]
print(S.stoneGameIII(values))
values = [-1,-2,-3]
print(S.stoneGameIII(values))
values = [-7,17,-2,-13,-6,-7,-13,11,-3,15,0,-11,-5,1,2,13,-14,-16,1,-8,6,-2,-14]
print(S.stoneGameIII(values))
# Output
# "Bob"
# Expected
# "Alice