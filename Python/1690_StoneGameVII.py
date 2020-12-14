"""
Alice and Bob take turns playing a game, with Alice starting first.

There are n stones arranged in a row. On each player's turn, they can remove either the leftmost stone or the rightmost stone from the row and receive points equal to the sum of the remaining stones' values in the row. The winner is the one with the higher score when there are no stones left to remove.

Bob found that he will always lose this game (poor Bob, he always loses), so he decided to minimize the score's difference. Alice's goal is to maximize the difference in the score.

Given an array of integers stones where stones[i] represents the value of the ith stone from the left, return the difference in Alice and Bob's score if they both play optimally.

 

Example 1:

Input: stones = [5,3,1,4,2]
Output: 6
Explanation: 
- Alice removes 2 and gets 5 + 3 + 1 + 4 = 13 points. Alice = 13, Bob = 0, stones = [5,3,1,4].
- Bob removes 5 and gets 3 + 1 + 4 = 8 points. Alice = 13, Bob = 8, stones = [3,1,4].
- Alice removes 3 and gets 1 + 4 = 5 points. Alice = 18, Bob = 8, stones = [1,4].
- Bob removes 1 and gets 4 points. Alice = 18, Bob = 12, stones = [4].
- Alice removes 4 and gets 0 points. Alice = 18, Bob = 12, stones = [].
The score difference is 18 - 12 = 6.
Example 2:

Input: stones = [7,90,5,1,100,10,10,2]
Output: 122
 

Constraints:

n == stones.length
2 <= n <= 1000
1 <= stones[i] <= 1000
"""


from typing import List
from functools import lru_cache
import sys
sys.setrecursionlimit(10**6)
class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        """
        TLE 58/64
        """
        @lru_cache(None)
        def dp(i, j):
            """
            the max score  can get from stones[i: j], that is preSum[i : j+1], maximize 1st score
            """
            # print('i,j',i, j)
            if i == j or i == j - 1:
                return 0, 0
            b1, a1 = dp(i + 1, j)
            b2, a2 = dp(i, j - 1)
            a1 += preSum[j] - preSum[i + 1]
            a2 += preSum[j - 1] - preSum[i]
            if a1 - b1 >= a2 - b2:
                # print(a1, b1)
                return a1, b1
            else:
                # print(a2, b2)
                return a2, b2
        preSum = [0]
        for stone in stones:
            preSum.append(preSum[-1] + stone)
        a, b = dp(0, len(stones))
        # print(a, b)
        return a - b

from typing import List
from functools import lru_cache
import sys
sys.setrecursionlimit(10**6)
class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        """
        TLE 58/64
        """
        @lru_cache(None)
        def dp(i, j):
            """
            the max score  can get from stones[i: j], that is preSum[i : j+1], maximize 1st score
            """
            # print('i,j',i, j)
            if i == j or i == j - 1:
                return 0
            k1 = -dp(i + 1, j)
            k2 = -dp(i, j - 1)
            k1 += preSum[j] - preSum[i + 1]
            k2 += preSum[j - 1] - preSum[i]
            if k1 >= k2:
                return k1
            else:
                return k2

        preSum = [0]
        for stone in stones:
            preSum.append(preSum[-1] + stone)
        k = dp(0, len(stones))
        # print(a, b)
        return k


class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:

        def dp(i, j):
            """
            the max score  can get from stones[i: j], that is preSum[i : j+1], maximize 1st score
            """
            if (i, j) in self.memo:
                return self.memo[(i, j)]
            if i == j or i == j - 1:
                return 0
            k1 = -dp(i + 1, j)
            if k1 == 0:
                self.memo[(i, j)] = preSum[j] - preSum[i + 1]
                return self.memo[(i, j)]
            k1 += preSum[j] - preSum[i + 1]
            k2 = -dp(i, j - 1)
            k2 += preSum[j - 1] - preSum[i]
            self.memo[(i, j)] = max(k1, k2)
            return self.memo[(i, j)]

        preSum = [0]
        for stone in stones:
            preSum.append(preSum[-1] + stone)
        self.memo = dict()
        k = dp(0, len(stones))
        # print(a, b)
        return k

class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:

        def calc(i, j):
            """
            the max score  can get from stones[i: j], that is preSum[i : j+1], maximize 1st score
            """
            if i >= j - 1:
                return 0
            if dp[i][j] != 0:
                return dp[i][j]
            k1 = -calc(i + 1, j)
            k2 = -calc(i, j - 1)
            k2 += preSum[j - 1] - preSum[i]
            k1 += preSum[j] - preSum[i + 1]
            dp[i][j] = max(k1, k2)
            return dp[i][j]

        preSum = [0]
        for stone in stones:
            preSum.append(preSum[-1] + stone)
        len_s = len(stones)
        dp = [[0] * (len_s + 1) for _ in range(len_s + 1)]
        calc(0, len_s)
        return dp[0][len_s]


from typing import List
class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        preSum = [0]
        for stone in stones:
            preSum.append(preSum[-1] + stone)
        len_s = len(stones)
        dp = [[0] * (len_s + 1) for _ in range(len_s + 1)]
        # print(preSum)
        # dp[len_s-1][len_s] = 0
        for i in range(len_s - 1, -1, -1):
            for j in range(i + 1, len_s + 1):
                dp[i][j] = max(preSum[j] - preSum[i + 1] - dp[i + 1][j], preSum[j - 1] - preSum[i] - dp[i][j - 1])
        # for row in dp:
        #     print(row)
        return dp[0][len_s]


S = Solution()
stones = [5,3,1,4,2]
print(S.stoneGameVII(stones))
stones = [7,90,5,1,100,10,10,2]
print(S.stoneGameVII(stones))
stones = [213,513,451,959,859,919,345,59,5,544,820,742,739,638,375,20,652,929,323,673,285,517,315,659,951,452,107,66,468,374,977,453,76,215,540,371,528,85,672,238,302,551,327,819,817,437,952,558,218,907,715,603,615,946,198,319,685,79,86,561,284,97,607,276,902,652,977,774,212,784,568,543,711,917,561,533,850,383,36,230,149,108,205,222,340,348,350,256,238,316,810,931,128,954,102,624,790,891,648,258,371,241,425,656,450,678,918,30,520,944,307,840,755,642,445,658,514,261,63,542,258,368,339,377,596,866,831,665,875,133,60,123,56,708,640,755,265,845,42,189,878,682,359,802,552,88,982,9,496,751,515,791,198,911,714,505,878,789,755,816,118,298,373,912,236,597,301,466,366,622,473,181,859,78,332,330,559,749,973,635,873,426,935,277,187,893,612,526,165,331,817,776,983,791,784,916,634,464,134,517,527,289,476,405,541,80,934,445,165,449,952,7,167,91,427,638,126,225,481,346,455,215,50,407,380,46,506,631,576,688,665,328,922,497,513,291,35,988,752,857,195,318,185,365,86,644,90,812,322,765,631,72,442,89,977,812,21,637,227,16,58,883,339,677,739,96,33,374,760,747,655,43,593,809,491,610,354,758,474,836,309,418,234,129,479,163,962,844,854,996,824,54,277,786,434,215,930,123,670,303,921,365,50,160,600,856,561,623,4,336,586,673,313,423,728,893,970,880,828,19,311,241,239,116,742,116,78,635,563,916,315,353,107,302,317,131,499,994,869,633,587,168,708,569,669,125,84,565,40,41,426,286,528,562,789,126,489,181,492,90,129,347,697,158,67,571,472,529,691,370,579,189,568,665,334,449,492,324,807,132,692,917,474,13,944,365,848,786,879,866,527,709,173,611,604,123,447,988,301,489,682,218,315,585,842,255,598,753,26,787,136,756,482,932,706,540,593,689,578,926,103,736,499,908,123,885,360,790,845,759,648,480,458,330,15,53,631,749,73,568,468,864,206,437,377,341,288,844,64,133,507,204,11,15,99,616,265,360,22,628,498,977,106,244,620,591,312,644,163,109,264,396,653,214,992,455,350,136,551,821,144,64,836,596,902,786,990,661,479,219,370,176,505,384,495,680,472,413,838,906,859,109,429,419,697,261,162,667,989,40,549,380,46,166,898,826,261,95,748,197,514,370,547,730,309,132,264,330,385,664,87,20,492,774,198,635,347,181,718,194,483,846,773,882,752,795,660,615,572,78,557,123,239,577,482,556,349,875,943,732,82,58,151,120,164,150,563,722,576,592,527,775,395,733,951,434,987,262,696,548,55,375,771,908,522,546,399,825,683,788,776,409,460,486,358,129,830,918,308,91,50,257,881,336,115,923,977,537,747,817,731,164,948,899,879,121,29,885,157,275,113,51,576,733,176,843,66,221,842,323,199,718,663,391,369,490,160,107,752,820,12,492,513,747,34,454,60,420,574,399,193,527,832,240,787,350,730,793,575,432,73,226,77,191,916,9,258,545,947,975,259,867,756,148,132,46,144,849,854,715,504,842,387,132,211,475,127,596,521,603,774,518,930,769,640,729,839,39,361,471,708,467,865,797,915,255,242,314,917,791,124,901,606,831,400,225,443,80,310,978,787,480,532,427,855,962,876,450,182,648,386,973,228,882,202,131,638,67,563,178,234,758,622,972,996,38,528,190,150,395,692,812,947,686,308,461,62,775,641,997,616,348,483,119,417,7,783,998,167,153,948,491,86,296,51,432,399,292,591,806,514,239,926,124,373,345,925,608,812,675,115,919,223,96,980,365,372,259,616,390,674,322,721,693,111,960,976,707,9,1,474,167,555,154,429,541,270,686,915,508,27,493,656,691,716,836,277,330,600,55,301,75,500,558,49,320,263,225,102,288,835,575,173,836,597,429,288,664,397,814,441,100,279,538,752,483,846,527,374,216,379]
# print(len(stones))
# print(S.stoneGameVII(stones))