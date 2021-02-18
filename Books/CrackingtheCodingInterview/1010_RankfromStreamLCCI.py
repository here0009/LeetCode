"""
假设你正在读取一串整数。每隔一段时间，你希望能找出数字 x 的秩(小于或等于 x 的值的个数)。请实现数据结构和算法来支持这些操作，也就是说：

实现 track(int x) 方法，每读入一个数字都会调用该方法；

实现 getRankOfNumber(int x) 方法，返回小于或等于 x 的值的个数。

注意：本题相对原题稍作改动

示例:

输入:
["StreamRank", "getRankOfNumber", "track", "getRankOfNumber"]
[[], [1], [0], [0]]
输出:
[null,0,null,1]
提示：

x <= 50000
track 和 getRankOfNumber 方法的调用次数均不超过 2000 次

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/rank-from-stream-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class StreamRank:
    """
    Thoughts: bit tree, wrong answer, x could be negative
    """

    def __init__(self):
        self.max_limit = 50000
        self.bit = [0] * (self.max_limit + 1)


    def track(self, x: int) -> None:
        while x <= self.max_limit:
            self.bit[x] += 1
            x += x ^ - x
            print(x)

    def getRankOfNumber(self, x: int) -> int:
        return self.bit[x]


from bisect import bisect_right, insort
class StreamRank:
    """
    Thoughts: bit tree, wrong answer, x could be negative
    """

    def __init__(self):
        self.vals = []


    def track(self, x: int) -> None:
        insort(self.vals, x)

    def getRankOfNumber(self, x: int) -> int:
        return bisect_right(self.vals, x)


# Your StreamRank print object will be instantiated and called as such:
obj = StreamRank()
print(obj.getRankOfNumber(1))
print(obj.track(0))
print(obj.getRankOfNumber(0))