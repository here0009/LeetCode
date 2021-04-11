"""
有个马戏团正在设计叠罗汉的表演节目，一个人要站在另一人的肩膀上。出于实际和美观的考虑，在上面的人要比下面的人矮一点且轻一点。已知马戏团每个人的身高和体重，请编写代码计算叠罗汉最多能叠几个人。

示例：

输入：height = [65,70,56,75,60,68] weight = [100,150,90,190,95,110]
输出：6
解释：从上往下数，叠罗汉最多能叠 6 层：(56,90), (60,95), (65,100), (68,110), (70,150), (75,190)
提示：

height.length == weight.length <= 10000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/circus-tower-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


from typing import List
from functools import lru_cache
class Solution:
    def bestSeqAtIndex(self, height: List[int], weight: List[int]) -> int:
        """
        TLE
        """
        @lru_cache(None)
        def calc(idx, h, w):
            if idx == length:
                return 0
            res = calc(idx + 1, h, w)
            for j in range(idx, length):
                h2, w2 = sorted_h_w[j]
                if h2 > h and w2 > w:
                    res = max(res, 1 + calc(j, h2, w2))
            return res

        length = len(height)
        sorted_h_w = sorted(zip(height, weight))
        # print(sorted_h_w)
        return calc(0, 0, 0)

from typing import List
from bisect import bisect_left, bisect_right
class Solution:
    def bestSeqAtIndex(self, height: List[int], weight: List[int]) -> int:

        length = len(height)
        sorted_h_w = sorted(zip(height, weight), key=lambda x: (x[0], -x[1]))
        stack = []
        # print(sorted_h_w)
        for i in range(length):
            _, w = sorted_h_w[i]
            idx = bisect_left(stack, w)  # bisect_left will replace the idx, bisect_right will append num to the end
            if idx == len(stack):
                if not stack or w > stack[-1]:
                    stack.append(w)
            else:
                stack[idx] = w
            # print(stack)
        return len(stack)

S = Solution()
height = [65,70,56,75,60,68]
weight = [100,150,90,190,95,110]
print(S.bestSeqAtIndex(height, weight))

height =[1,2,3,4]
weight =[4,3,2,1]
print(S.bestSeqAtIndex(height, weight))

nums = [1,3,3,3,4,5,7,10]
for k in range(10):
    print(k, bisect_left(nums, k), bisect_right(nums, k))
