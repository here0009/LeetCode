"""
堆箱子。给你一堆n个箱子，箱子宽 wi、深 di、高 hi。箱子不能翻转，将箱子堆起来时，下面箱子的宽度、高度和深度必须大于上面的箱子。实现一种方法，搭出最高的一堆箱子。箱堆的高度为每个箱子高度的总和。

输入使用数组[wi, di, hi]表示每个箱子。

示例1:

 输入：box = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
 输出：6
示例2:

 输入：box = [[1, 1, 1], [2, 3, 4], [2, 6, 7], [3, 4, 5]]
 输出：10
提示:

箱子的数目不大于3000个。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/pile-box-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


from typing import List
from collections import defaultdict
from functools import lru_cache
class Solution:
    def pileBox(self, box: List[List[int]]) -> int:
        @lru_cache(None)
        def dp(idx):
            return box[idx][2] + max([dp(nxt) for nxt in edges[idx]] + [0])

        box.sort()
        edges = defaultdict(list)
        len_box = len(box)
        for i in range(len_box):
            ai, bi, ci = box[i]
            for j in range(i):
                aj, bj, cj = box[j]
                if aj < ai and bj < bi and cj < ci:
                    edges[i].append(j)
        # print(edges)
        res = 0
        for i in range(len_box):
            res = max(res, dp(i))
        return res


class Solution:
    def pileBox(self, box: List[List[int]]) -> int:
        box.sort()
        len_box = len(box)
        dp = [b[-1] for b in box]
        for i in range(len_box):
            ai, bi, ci = box[i]
            for j in range(i):
                aj, bj, cj = box[j]
                if aj < ai and bj < bi and cj < ci:
                    dp[i] = max(dp[i], dp[j] + ci)
        return max(dp)


# 作者：rockypan
# 链接：https://leetcode-cn.com/problems/pile-box-lcci/solution/chun-hui-su-bei-wang-jia-jian-zhi-6xing-dai-ma-ji-/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
class Solution:
    def pileBox(self, box: List[List[int]]) -> int:
        lru_cache(None)
        def sol(w, d, h) :
            inners = [(iw,id,ih) for iw,id,ih in box if iw<w and id<d and ih<h]
            if not inners: 
                return h
            return max((sol(iw,id,ih) for iw,id,ih in inners)) + h
        return max((sol(w,d,h) for w,d,h in box))

S = Solution()
box = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
print(S.pileBox(box))
box = [[1, 1, 1], [2, 3, 4], [2, 6, 7], [3, 4, 5]]
print(S.pileBox(box))



