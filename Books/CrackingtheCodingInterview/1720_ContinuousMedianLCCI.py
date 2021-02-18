"""
随机产生数字并传递给一个方法。你能否完成这个方法，在每次产生新值时，寻找当前所有值的中间值（中位数）并保存。

中位数是有序列表中间的数。如果列表长度是偶数，中位数则是中间两个数的平均值。

例如，

[2,3,4] 的中位数是 3

[2,3] 的中位数是 (2 + 3) / 2 = 2.5

设计一个支持以下两种操作的数据结构：

void addNum(int num) - 从数据流中添加一个整数到数据结构中。
double findMedian() - 返回目前所有元素的中位数。
示例：

addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3) 
findMedian() -> 2

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/continuous-median-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


import heapq
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.larger = []
        self.smaller = []


    def addNum(self, num: int) -> None:
        heapq.heappush(self.larger, num)
        heapq.heappush(self.smaller, -1 * heapq.heappop(self.larger))
        if len(self.smaller) > len(self.larger):
            heapq.heappush(self.larger, -1 * heapq.heappop(self.smaller))


    def findMedian(self) -> float:
        if len(self.larger) > len(self.smaller):
            return self.larger[0]
        else:
            return (self.larger[0] + -1 * self.smaller[0]) / 2



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()