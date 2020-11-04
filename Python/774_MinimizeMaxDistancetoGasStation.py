"""
On a horizontal number line, we have gas stations at positions stations[0], stations[1], ..., stations[N-1], where N = stations.length.

Now, we add K more gas stations so that D, the maximum distance between adjacent gas stations, is minimized.

Return the smallest possible value of D.

Example:

Input: stations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], K = 9
Output: 0.500000
Note:

stations.length will be an integer in range [10, 2000].
stations[i] will be an integer in range [0, 10^8].
K will be an integer in range [1, 10^6].
Answers within 10^-6 of the true value will be accepted as correct.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimize-max-distance-to-gas-station
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# 作者：LeetCode
# 链接：https://leetcode-cn.com/problems/minimize-max-distance-to-gas-station/solution/zui-xiao-hua-qu-jia-you-zhan-de-zui-da-ju-chi-by-l/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

class Solution(object):
    """
    TLE
    """
    def minmaxGasDist(self, stations, K):
        pq = [] #(-part_length, original_length, num_parts)
        for i in range(len(stations) - 1):
            x, y = stations[i], stations[i+1]
            pq.append((x-y, y-x, 1))
        heapq.heapify(pq)
        for _ in range(K):
            negnext, orig, parts = heapq.heappop(pq)
            parts += 1
            heapq.heappush(pq, (-(orig / float(parts)), orig, parts))
        return -pq[0][0]



from math import ceil
class Solution:
    def minmaxGasDist(self, stations, K: int) -> float:
        def test(d):
            """
            test if K stations were added, d could be the min distance
            """
            counts = 0
            for gap in gaps:
                counts += ceil(gap/d)-1
                if counts > K:
                    return False
            return True

        length = len(stations)
        gaps = []
        for i in range(1, length):
            if stations[i]-stations[i-1] > 0:
                gaps.append(stations[i]-stations[i-1])
        gaps = sorted(gaps, reverse=True)
        # print(gaps)
        left = gaps[0]/(K+1)
        right = gaps[0]
        # print(left, right)
        while right - left > 1E-7:
            mid = (left + right) / 2
            # print(left, right, mid, test(mid))
            if test(mid):
                right = mid
            else:
                left = mid
        return left

# 作者：LeetCode
# 链接：https://leetcode-cn.com/problems/minimize-max-distance-to-gas-station/solution/zui-xiao-hua-qu-jia-you-zhan-de-zui-da-ju-chi-by-l/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
class Solution(object):
    def minmaxGasDist(self, stations, K):
        def possible(D):
            return sum(int((stations[i+1] - stations[i]) / D)
                       for i in range(len(stations) - 1)) <= K

        lo, hi = 0, 10**8
        while hi - lo > 1e-6:
            mi = (lo + hi) / 2.0
            if possible(mi):
                hi = mi
            else:
                lo = mi
        return lo



S = Solution()
stations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
K = 9
print(S.minmaxGasDist(stations, K))

stations =[23,24,36,39,46,56,57,65,84,98]
K = 1
print(S.minmaxGasDist(stations, K))
# 输出：
# 37.50000
# 预期结果：
# 14.0