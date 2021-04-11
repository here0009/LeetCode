"""
有些数的素因子只有 3，5，7，请设计一个算法找出第 k 个数。注意，不是必须有这些素因子，而是必须不包含其他的素因子。例如，前几个数按顺序应该是 1，3，5，7，9，15，21。

示例 1:

输入: k = 5

输出: 9

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/get-kth-magic-number-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


import heapq
class Solution:
    def getKthMagicNumber(self, k: int) -> int:

        def getNum(p, q, r):
            return 3**p * 5 ** q * 7 ** r

        pq = [(1, 0, 0, 0)]
        incr = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
        visited = set()
        while k > 0:
            num, p, q, r = heapq.heappop(pq)
            for i in range(3):
                p2, q2, r2 = p + incr[i][0], q + incr[i][1], r + incr[i][2]
                num2 = getNum(p2, q2, r2)
                if num2 not in visited:
                    visited.add(num2)
                    heapq.heappush(pq, (num2, p2, q2, r2))
            # print(pq)
            k -= 1
        return num

S = Solution()
for i in range(1, 10):
    print(i, S.getKthMagicNumber(i))