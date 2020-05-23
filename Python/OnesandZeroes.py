"""
In the computer world, use restricted resource you have to generate maximum benefit is what we always want to pursue.

For now, suppose you are a dominator of m 0s and n 1s respectively. On the other hand, there is an array with strings consisting of only 0s and 1s.

Now your task is to find the maximum number of strings that you can form with given m 0s and n 1s. Each 0 and 1 can be used at most once.

Note:

The given numbers of 0s and 1s will both not exceed 100
The size of given string array won't exceed 600.
 

Example 1:

Input: Array = {"10", "0001", "111001", "1", "0"}, m = 5, n = 3
Output: 4

Explanation: This are totally 4 strings can be formed by the using of 5 0s and 3 1s, which are “10,”0001”,”1”,”0”
 

Example 2:

Input: Array = {"10", "0", "1"}, m = 1, n = 1
Output: 2

Explanation: You could form "10", but then you'd have nothing left. Better form "0" and "1".
 
"""
class Solution:
    def findMaxForm(self, strs, m: int, n: int) -> int:
        
        def dfs(i,j):
            pass
        self.res = 0
        len_n = len(strs)
        visited = [0]*len_n

from collections import Counter
from collections import defaultdict
class Solution_1:
    def findMaxForm(self, strs, m: int, n: int) -> int:
        memo = defaultdict(int)
        memo[(0,0)] = 0
        for string in strs:
            s_counter = Counter(string)
            zeros, ones = s_counter['0'], s_counter['1']
            memo2 = dict()
            for (z,o) in memo:
                z2, o2 = z+zeros, o+ones
                if z2 <= m and o2 <= n:
                    # print('z',z2,o2,zeros,ones)
                    memo2[(z2, o2)] = memo[(z,o)] + 1
            for (z,o) in memo2:
                if (z,o) not in memo or memo2[(z,o)] > memo[(z,o)]:
                    memo[(z,o)] = memo2[(z,o)]
            # memo.update(memo2)
            if zeros <= m and ones <= n:
                memo[(zeros, ones)] = max(memo[(zeros, ones)], 1)
        # print(memo)
        return max(memo.values())

from collections import Counter
class Solution:
    def findMaxForm(self, strs, m: int, n: int) -> int:
        """
        dp[i] to record the min 1s and 0s to get cover i string
        """
        dp = [(0,0)]
        for string in strs:
            s_counter = Counter(string)
            zeros, ones = s_counter['0'], s_counter['1']
            z, o = dp[-1][0]+zeros, dp[-1][1]+ones
            if z <= m and o <= n:
                dp.append((z,o))
            for i in range(len(dp)-1,0,-1): #update dp from end to begin, because we need the previous dp information, update from begin to end, will erase that information
                z, o = dp[i-1][0]+zeros, dp[i-1][1]+ones
                if z <= dp[i][0] and o <= dp[i][1]:
                    dp[i] = (z, o)
            print(dp)
        return len(dp)-1





s = Solution()

# Array = ["10", "0001", "111001", "1", "0"]
# m = 5
# n = 3
# print(s.findMaxForm(Array, m, n))

# Array = ["10", "0", "1"]
# m = 1
# n = 1
# print(s.findMaxForm(Array, m, n))


# Array = ["10","0001","111001","1","0"]
# m = 3
# n = 4
# print(s.findMaxForm(Array, m, n))
# """
# Output
# 2
# Expected
# 3
# """

# Array = ["00","000"]
# m = 1
# n = 10
# print(s.findMaxForm(Array, m, n))
# """
# Output
# 1
# Expected
# 0
# """

# Array = ["0","11","1000","01","0","101","1","1","1","0","0","0","0","1","0","0110101","0","11","01","00","01111","0011","1","1000","0","11101","1","0","10","0111"]
# m = 9
# n = 80
# print(s.findMaxForm(Array, m, n))
# """
# Output
# 16
# Expected
# 17
# """

Array = ["111","1000","1000","1000"]
m = 9
n = 3
print(s.findMaxForm(Array, m, n))
# Output
# 1
# Expected
# 3
# need to record min m and min n