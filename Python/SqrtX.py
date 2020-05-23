"""
My submission:
基本思想是将x不断除以2得tmp, 如果tmp**2 > x, 则继续除
如果tmp ** 2 < x, 则tmp不断+1, 直到找到平方根或比平方根小1的数
但数字大的情况下,第二种情况太费时间
参考牛顿的迭代法求平方根,
思想类似, 但tmp的取值是(tmp + x//tmp) //2, 即tmp与x//tmp的中值
class Solution:
    def mySqrt(self, x):

        return self.sqrtRange(x//2, x)

    def sqrtRange(self, lower, dest):
        # print (lower)
        if lower ** 2 == dest:
            return lower
        elif lower ** 2 > dest:
            return self.sqrtRange(lower//2, dest)
        else:
            for i in range(lower,lower*2 + 2):
                # print(i)
                if i ** 2 == dest:
                    return i
                elif i ** 2 > dest:
                    return i-1
            
s = Solution()
# for i in range(100):
#     print(s.mySqrt(i))
print(s.mySqrt(1694275660))
It will exceed time when encounts large numbers
"""
#Newton's method
class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        r = x
        while r**2 > x:
            r = (r + x//r) // 2
        return r


s = Solution()
for i in range(100):
    print(s.mySqrt(i))
print(s.mySqrt(1694275660))