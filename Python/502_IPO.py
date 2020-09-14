"""
Suppose LeetCode will start its IPO soon. In order to sell a good price of its shares to Venture Capital, LeetCode would like to work on some projects to increase its capital before the IPO. Since it has limited resources, it can only finish at most k distinct projects before the IPO. Help LeetCode design the best way to maximize its total capital after finishing at most k distinct projects.

You are given several projects. For each project i, it has a pure profit Pi and a minimum capital of Ci is needed to start the corresponding project. Initially, you have W capital. When you finish a project, you will obtain its pure profit and the profit will be added to your total capital.

To sum up, pick a list of at most k distinct projects from given projects to maximize your final capital, and output your final maximized capital.

Example 1:
Input: k=2, W=0, Profits=[1,2,3], Capital=[0,1,1].

Output: 4

Explanation: Since your initial capital is 0, you can only start the project indexed 0.
             After finishing it you will obtain profit 1 and your capital becomes 1.
             With capital 1, you can either start the project indexed 1 or the project indexed 2.
             Since you can choose at most 2 projects, you need to finish the project indexed 2 to get the maximum capital.
             Therefore, output the final maximized capital, which is 0 + 1 + 3 = 4.
Note:
You may assume all numbers in the input are non-negative integers.
The length of Profits array and Capital array will not exceed 50,000.
The answer is guaranteed to fit in a 32-bit signed integer.
"""



class Solution:
    def findMaximizedCapital(self, k: int, W: int, Profits, Capital) -> int:
        """
        TLE
        """
        def dfs(k, W):
            self.res = max(self.res, W)
            if k == 0 or sum(visited) == length:
                return
            for i in range(length):
                if not visited[i] and Capital[i] <= W:
                    visited[i] = 1
                    dfs(k-1, W+Profits[i])
                    visited[i] = 0

        length = len(Profits)
        visited = [0]*length
        self.res = 0
        dfs(k, W)
        return self.res


import heapq
class Solution:
    def findMaximizedCapital(self, k: int, W: int, Profits, Capital) -> int:
        """
        since you can get more profit if you got more capital, we can find the most profitable project that we can get. then find others 
        """
        pq = []
        heapq.heapify(pq)
        index = 0
        length = len(Capital)
        projects = sorted(zip(Capital, Profits))
        for _ in range(k):

            while index < length:
                c, p = projects[index]
                if c <= W:
                    heapq.heappush(pq, -p)
                    index += 1
                else:
                    break
            # print(index, pq)
            if pq:
                W -= heapq.heappop(pq)
            else:
                break
        return W


import heapq
class Solution:
    def findMaximizedCapital(self, k, W, Profits, Capital):
        heap = []
        projects = sorted(zip(Profits, Capital), key=lambda l: l[1])
        i = 0
        for _ in range(k):
            while i < len(projects) and projects[i][1] <= W:
                heapq.heappush(heap, -projects[i][0])
                i += 1
            if heap: W -= heapq.heappop(heap)
        return W

S = Solution()
k=2
W=0
Profits=[1,2,3]
Capital=[0,1,1]
print(S.findMaximizedCapital(k, W, Profits, Capital))

k = 10
W = 0
Profits = [1,2,3]
Capital = [0,1,2]
print(S.findMaximizedCapital(k, W, Profits, Capital))
# Output
# 0
# Expected
# 6

k = 2
W = 0
Profits = [1,2,3]
Capital = [0,9,10]
print(S.findMaximizedCapital(k, W, Profits, Capital))