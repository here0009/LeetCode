"""
You have one chocolate bar that consists of some chunks. Each chunk has its own sweetness given by the array sweetness.

You want to share the chocolate with your K friends so you start cutting the chocolate bar into K+1 pieces using K cuts, each piece consists of some consecutive chunks.

Being generous, you will eat the piece with the minimum total sweetness and give the other pieces to your friends.

Find the maximum total sweetness of the piece you can get by cutting the chocolate bar optimally.

 

Example 1:

Input: sweetness = [1,2,3,4,5,6,7,8,9], K = 5
Output: 6
Explanation: You can divide the chocolate to [1,2,3], [4,5], [6], [7], [8], [9]
Example 2:

Input: sweetness = [5,6,7,8,9,1,2,3,4], K = 8
Output: 1
Explanation: There is only one way to cut the bar into 9 pieces.
Example 3:

Input: sweetness = [1,2,2,1,2,2,1,2,2], K = 2
Output: 5
Explanation: You can divide the chocolate to [1,2,2], [1,2,2], [1,2,2]
 

Constraints:

0 <= K < sweetness.length <= 10^4
1 <= sweetness[i] <= 10^5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/divide-chocolate
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


from functools import lru_cache
class Solution:
    def maximizeSweetness(self, sweetness, K: int) -> int:
        """
        TLE
        """
        @lru_cache(None)
        def dp(i, k):
            
            """
            max val we can get cut sweetness[i:] to k pieces
            """
            res = -float('inf')
            if length - i < k or k <= 0:
                return res
            if k == 1:
                return sum(sweetness[i:])
            if length - i == k:
                return min(sweetness[i:])
            tmp = 0
            for j in range(i+1, length-k+2):
                tmp += sweetness[j-1]
                res = max(res, min(tmp, dp(j, k-1)))
            # print(i, k, res)
            return res

        length = len(sweetness)
        return dp(0, K+1)


from functools import lru_cache
class Solution:
    def maximizeSweetness(self, sweetness, K: int) -> int:
        @lru_cache(None)
        def dp(i, k):
            print(i, k)
            
            """
            max val we can get cut sweetness[i:] to k pieces
            """
            res = -float('inf')
            if length - i < k or k <= 0:
                return res
            if k == 1:
                return preSum[-1] - preSum[i]
            curr = 0
            for j in range(i+1, length-k+2):
                curr += sweetness[j-1]
                tmp = min(curr, dp(j, k-1))
                if tmp < res:
                    break
                else:
                    res = tmp
            # print(i, k, res)
            return res

        length = len(sweetness)
        preSum = [0]
        # print(len(sweetness))
        for sweet in sweetness:
            preSum.append(preSum[-1]+sweet)
        return dp(0, K+1)


from functools import lru_cache
class Solution:
    def maximizeSweetness(self, sweetness, K: int) -> int:
        """
        TLE
        """
        def dp(i, k):
            if (i, k) in memo:
                return memo[(i,k)]
            """
            max val we can get cut sweetness[i:] to k pieces
            """
            res = -float('inf')
            if length - i < k or k <= 0:
                return res
            if k == 1:
                return preSum[-1] - preSum[i]
            curr = 0
            for j in range(i+1, length-k+2):
                curr += sweetness[j-1]
                tmp = min(curr, dp(j, k-1))
                if tmp < res:
                    break
                else:
                    res = tmp
            # print(i, k, res)
            memo[(i,k)] = res
            return res

        length = len(sweetness)
        preSum = [0]
        memo = dict()
        # print(len(sweetness))
        for sweet in sweetness:
            preSum.append(preSum[-1]+sweet)
        return dp(0, K+1)


class Solution:
    def maximizeSweetness(self, sweetness, K: int) -> int:
        def check(n):
            counts = 0
            curr = 0
            for sweet in sweetness:
                curr += sweet
                if curr >= n:
                    counts += 1
                    if counts >= K+1:
                        return True
                    curr = 0
            return counts >= K+1

        if K == 0:
            return sum(sweetness)
        left, right = 0, sum(sweetness)//K
        while left < right:
            mid = (left + right)//2
            if check(mid):
                left = mid+1
            else:
                right = mid
        return left -1 


class Solution:
    def maximizeSweetness(self, sweetness, K: int) -> int:
        def check(n):
            counts = 0
            curr = 0
            for sweet in sweetness:
                curr += sweet
                if curr >= n:
                    counts += 1
                    if counts >= K+1:
                        return True
                    curr = 0
            return counts >= K+1

        if K == 0:
            return sum(sweetness)
        left, right = min(sweetness), sum(sweetness)//K
        while left <= right:
            mid = (left + right)//2
            if check(mid):
                res = mid
                left = mid+1
            else:
                right = mid-1
        return res


S = Solution()
sweetness = [1,2,3,4,5,6,7,8,9]
K = 5
print(S.maximizeSweetness(sweetness, K))
sweetness = [5,6,7,8,9,1,2,3,4]
K = 8
print(S.maximizeSweetness(sweetness, K))
sweetness = [1,2,2,1,2,2,1,2,2]
K = 2
print(S.maximizeSweetness(sweetness, K))
sweetness = [1,2,2,1,2,2,1,2,2]
K = 2
print(S.maximizeSweetness(sweetness, K))