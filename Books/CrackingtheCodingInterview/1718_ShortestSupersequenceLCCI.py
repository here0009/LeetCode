"""
假设你有两个数组，一个长一个短，短的元素均不相同。找到长数组中包含短数组所有的元素的最短子数组，其出现顺序无关紧要。

返回最短子数组的左端点和右端点，如有多个满足条件的子数组，返回左端点最小的一个。若不存在，返回空数组。

示例 1:

输入:
big = [7,5,9,0,2,1,3,5,7,9,1,1,5,8,8,9,7]
small = [1,5,9]
输出: [7,10]
示例 2:

输入:
big = [1,2,3]
small = [4]
输出: []
提示：

big.length <= 100000
1 <= small.length <= 100000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shortest-supersequence-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


from typing import List
from collections import Counter
class Solution:
    def shortestSeq(self, big: List[int], small: List[int]) -> List[int]:
        target = set(small)
        length = len(big)
        left, right = 0, 0
        tmp_set = set()
        tmp_counter = Counter()
        res = [-float('inf'), float('inf')]
        # print(len(big))
        while left < length:

            while right < length and tmp_set != target:
                if big[right] in target:
                    tmp_counter[big[right]] += 1
                    tmp_set.add(big[right])
                right += 1
            while left < right:
                if big[left] in target and tmp_counter[big[left]] == 1:
                    break
                if tmp_counter[big[left]] > 1:
                    tmp_counter[big[left]] -= 1
                left += 1

            if tmp_set == target and right - 1 - left < res[1] - res[0]:
                res = [left, right - 1]
            # print(left, right, tmp_set, tmp_counter, res)
            if left < length and big[left] in tmp_counter:
                tmp_counter[big[left]] -= 1
                if tmp_counter[big[left]] == 0:
                    tmp_set.remove(big[left])
            left += 1
        return res if res != [-float('inf'), float('inf')] else []

S = Solution()
big = [7,5,9,0,2,1,3,5,7,9,1,1,5,8,8,9,7]
small = [1,5,9]
print(S.shortestSeq(big, small))
big = [1,2,3]
small = [4]
print(S.shortestSeq(big, small))