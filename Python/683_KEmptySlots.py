"""
You have N bulbs in a row numbered from 1 to N. Initially, all the bulbs are turned off. We turn on exactly one bulb everyday until all bulbs are on after N days.

You are given an array bulbs of length N where bulbs[i] = x means that on the (i+1)th day, we will turn on the bulb at position x where i is 0-indexed and x is 1-indexed.

Given an integer K, find out the minimum day number such that there exists two turned on bulbs that have exactly K bulbs between them that are all turned off.

If there isn't such day, return -1.

 

Example 1:

Input: 
bulbs: [1,3,2]
K: 1
Output: 2
Explanation:
On the first day: bulbs[0] = 1, first bulb is turned on: [1,0,0]
On the second day: bulbs[1] = 3, third bulb is turned on: [1,0,1]
On the third day: bulbs[2] = 2, second bulb is turned on: [1,1,1]
We return 2 because on the second day, there were two on bulbs with one off bulb between them.
Example 2:

Input: 
bulbs: [1,2,3]
K: 1
Output: -1
 

Note:

1 <= N <= 20000
1 <= bulbs[i] <= N
bulbs is a permutation of numbers from 1 to N.
0 <= K <= 20000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/k-empty-slots
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


from typing import List
from bisect import bisect_left
from bisect import insort
class Solution:
    def kEmptySlots(self, bulbs, K: int) -> int:
        light_on = []
        day = 0
        for b in bulbs:
            day += 1  # day-1 is the length of the lignt on bubles
            index = bisect_left(light_on, b)
            # print(b, day, light_on, index)
            if index > 0 and b - light_on[index-1] == K+1:
                return day
            if index < day-1 and light_on[index] - b == K+1:
                return day
            insort(light_on, b)
        return -1


# 作者：loick
# 链接：https://leetcode-cn.com/problems/k-empty-slots/solution/guan-fang-ti-jie-ge-ren-li-jie-by-loick/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
class Solution:
    def kEmptySlots(self, followers: List[int], K: int) -> int:
        days = [0]*len(followers)
        # 花棚在哪一天开花
        for i, f in enumerate(followers, 1):
            days[f-1] = i

        ans = float('inf')
        left, right = 0, K+1
        while right < len(followers):
            for i in range(left+1, right):
                if days[i] < days[left] or days[i] < days[right]:
                    left, right = i, i+K+1
                    break
            # 如果days， left和right中间的数都比左右小
            else:
                ans = min(ans, max(days[left], days[right]))
                left, right = right, right+K+1
        return ans if ans != float('inf') else -1



# 作者：yupeng-6
# 链接：https://leetcode-cn.com/problems/k-empty-slots/solution/python-solution-time-on-space-on-by-yupeng-6/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
class Solution:
    def kEmptySlots(self, bulbs, K):
        """
        :type bulbs: List[int]
        :type K: int
        :rtype: int
        """
        if K > len(bulbs):
            return -1

        days = [0 for i in range(len(bulbs))]

        for i in range(len(bulbs)):
            days[bulbs[i] - 1] = i + 1
        # days[0] = 6 meas we light buble 1 one day 6
        print(days)
        left = 0
        right = K + 1
        cur = 1
        res = float('inf')
        while cur <= right and right < len(bulbs):
            if days[left] < days[cur] and days[right] < days[cur]:
                cur += 1
                continue
            if cur == right:
                res = min(res, max(days[left], days[right]))
            left = cur
            right = cur + K + 1
            cur += 1
        if res == float('inf'):
            return -1
        return res

class Solution:
    """
    使用days按照顺序记录每个灯泡的点亮时间。维持一个大小为K+1的滑动窗口。
    初始值为left = 0, right = K+1； 当left与right中间的值均大于min(days[left], days[right]).
    说明此滑动窗口满足题意，候选最优解为max(days[left], days[right])。
    否则break，继续滑动
    """
    def kEmptySlots(self, bulbs, K):
        length = len(bulbs)
        days = [0]*length
        for i, b in enumerate(bulbs):
            days[b-1] = i+1
        left, right = 0, K+1
        res = float('inf')
        while right < length:
            for i in range(left+1, right):
                if days[i] < days[left] or days[i] < days[right]:
                    left = i
                    right = K+i+1
                    break
            else:
                res = min(res, max(days[left], days[right]))
                left = right
                right = left+K+1
        return res if res != float('inf') else -1


S = Solution()
bulbs = [1,3,2]
K = 1
print(S.kEmptySlots(bulbs, K))

bulbs = [1,2,3]
K = 1
print(S.kEmptySlots(bulbs, K))

bulbs =[6,5,8,9,7,1,10,2,3,4]
K =2
print(S.kEmptySlots(bulbs, K))
