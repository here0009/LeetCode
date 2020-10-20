"""
A group of friends went on holiday and sometimes lent each other money. For example, Alice paid for Bill's lunch for $10. Then later Chris gave Alice $5 for a taxi ride. We can model each transaction as a tuple (x, y, z) which means person x gave person y $z. Assuming Alice, Bill, and Chris are person 0, 1, and 2 respectively (0, 1, 2 are the person's ID), the transactions can be represented as [[0, 1, 10], [2, 0, 5]].

Given a list of transactions between a group of people, return the minimum number of transactions required to settle the debt.

Note:

A transaction will be given as a tuple (x, y, z). Note that x ≠ y and z > 0.
Person's IDs may not be linear, e.g. we could have the persons 0, 1, 2 or we could also have the persons 0, 2, 6.
Example 1:

Input:
[[0,1,10], [2,0,5]]

Output:
2

Explanation:
Person #0 gave person #1 $10.
Person #2 gave person #0 $5.

Two transactions are needed. One way to settle the debt is person #1 pays person #0 and #2 $5 each.
Example 2:

Input:
[[0,1,10], [1,0,1], [1,2,5], [2,0,5]]

Output:
1

Explanation:
Person #0 gave person #1 $10.
Person #1 gave person #0 $1.
Person #1 gave person #2 $5.
Person #2 gave person #0 $5.

Therefore, person #1 only need to give person #0 $4, and all debt is settled.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/optimal-account-balancing
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


from collections import Counter
import heapq
class Solution:
    def minTransfers(self, transactions) -> int:
        """
        wrong answer for the test case transactions = [[10,11,6],[12,13,7],[14,15,2],[14,16,2],[14,17,2],[14,18,2]]
        it is better to diminish the plus-minus pairs which got the same absolute values
        """
        account = Counter()
        for p, q, m in transactions:
            account[p] += m
            account[q] -= m
        res = 0
        print(account)
        minus, plus = [], []
        for v in account.values():
            if v < 0:
                heapq.heappush(minus, v)
            elif v > 0:
                heapq.heappush(plus, -v)
        while minus and plus:
            print(minus, plus)
            m = heapq.heappop(minus)
            p = -heapq.heappop(plus)
            rmd = m + p
            res += 1
            if rmd > 0:
                heapq.heappush(plus, -rmd)
            elif rmd < 0:
                heapq.heappush(minus, rmd)
        return res


from collections import Counter
class Solution:
    def minTransfers(self, transactions) -> int:
        """
        try all the possible routes, find the minimum transfers
        """
        def dfs(index, res):
            if res >= self.res:
                return
            while index < length and vals[index] == 0:
                index += 1
            if index == length:
                self.res = min(self.res, res)
            for j in range(index+1, length):
                if vals[j] * vals[index] < 0:
                    vals[j] += vals[index] # in this step we, put the profit/debet of index to j, (transfer all index's money to j, so now vals[index] is 0, but we do not to change it in vals), and we can skip index, only need to consider j in the future steps.
                    dfs(index+1, res+1)
                    vals[j] -= vals[index]

        account = Counter()
        for p, q, m in transactions:
            account[p] += m
            account[q] -= m
        vals = list(account.values())
        length = len(vals)
        self.res = float('inf')
        dfs(0, 0)
        return self.res

# from collections import defaultdict
# class Solution:
#     def minTransfers(self, transactions) -> int:
#         person = defaultdict(int)
#         for x, y, z in transactions:
#             person[x] -= z
#             person[y] += z
#         accounts = list(person.values())
#         self.res = float("inf")

#         def dfs(i, cnt):
#             print(i,cnt, accounts)
#             if cnt >= self.res: 
#                 return 
#             while i < len(accounts) and accounts[i] == 0: 
#                 i += 1
#             if i == len(accounts):
#                 self.res = min(self.res, cnt)
#                 return
#             for j in range(i + 1, len(accounts)):
#                 if accounts[i] * accounts[j] < 0:
#                     accounts[j] += accounts[i]
#                     dfs(i + 1, cnt + 1)
#                     accounts[j] -= accounts[i]

#         dfs(0, 0)
#         return self.res

# 作者：powcai
# 链接：https://leetcode-cn.com/problems/optimal-account-balancing/solution/bao-li-hui-su-by-powcai/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

S = Solution()
transactions = [[0,1,10], [2,0,5]]
print(S.minTransfers(transactions))
transactions = [[0,1,10], [1,0,1], [1,2,5], [2,0,5]]
print(S.minTransfers(transactions))
transactions = [[0,1,2],[1,2,1],[1,3,1]]
print(S.minTransfers(transactions))
# # 输出：
# # 1
# # 预期结果：
# # 2
transactions = [[10,11,6],[12,13,7],[14,15,2],[14,16,2],[14,17,2],[14,18,2]]
print(S.minTransfers(transactions))
# 输出：
# 7
# 预期结果：
# 6