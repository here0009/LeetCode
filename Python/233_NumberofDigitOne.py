"""
Given an integer n, count the total number of digit 1 appearing in all non-negative integers less than or equal to n.

Example:

Input: 13
Output: 6 
Explanation: Digit 1 occurred in the following numbers: 1, 10, 11, 12, 13.
"""


class Solution:
    def countDigitOne(self, n: int) -> int:
        def f(string):
            if len(string) == 1:
                return int(string) >= 1
            start = int(string[0])
            res = (int(string[0]) + 1) * f(string[1:])
            if start < 2:
                res += start * int(string[1:]+1)
            else: 
                res += 10**(len(string)-1)
            return res

        n += 1 # return total number smaller than n
        return f(str(n))

# https://leetcode.com/problems/number-of-digit-one/discuss/277541/1
"""
对于任意一个数，比如 abcde，
我们只需要找出万位、千万、百位、十位、个位上分别出现了多少个1就行了。
对于每一位，寻找出现多少个1的方法是一样的。比如，我们现在寻找百位出现了多少个1。
分成两个部分：

在小于 ab000 的数里，百位出现1的情况有 (为了醒目我把整个数字写成了这个格式" (百位左边 ) 百位 [百位右边]"
(00) 1 [00、01、02……99]
(01) 1 [00、01、02……99],
(02) 1 [00、01、02……99]
……
(ab-1) 1 [00、01、02……99]
因此一共有 ab*100 次
在大于 ab000 的数里，如果百位这个数也就是 c 大于1的话，那其实就是在1的情况里再加上
(ab) 1 [00、01、02……99] 这100次
如果e=1，那么会有 (ab) 1 [00、01……de] , 1 *(de+1) 次
如果 e=0, 那么会有 0 * (de+1）次
简单的说对于每一位，出现的次数都等于 ：左边的数字当前基数（百位就是100，千位就是1000……）+自己右边的数字 || 当前基数
"""
class Solution:
    def countDigitOne(self, n: int) -> int:
        """
        split each digit, count res for each digit
        """
        if n <= 0:
            return 0
        str_n = str(n)
        res = 0
        length = len(str_n)
        # print(str_n)
        for i in range(length):
            d = int(str_n[i])
            res += (int(str_n[:i]) if str_n[:i] else 0) * 10**(length-i-1)
            if d > 1:
                res += 10**(length-i-1)
            else:
                res += d*(int(str_n[i+1:] if str_n[i+1:] else 0)+1)
            # print(i, d, res)
        return res


class Solution:
    def countDigitOne(self, n: int) -> int:
        if n <= 0:
            return 0
        d = len(str(n)) - 1
        
        if d == 0:
            return 1
        
        p = pow(10, d - 1)
        res = d * p
        q, r = divmod(n, 10 * p)
        res += self.countDigitOne(r)
        if q == 1:
            res += r + 1
        else:
            res += (10 + d * (q - 1)) * p
        return res

class Solution:
    def countDigitOne(self, n):
        ones = 0
        m = r = 1
        while n > 0:
            print(n, ones, m, r)
            ones += (n + 8) // 10 * m + (n % 10 == 1) * r
            r += n % 10 * m
            m *= 10
            n = n //10
        # print(n, ones, m, r)
        return ones
S = Solution()
# n = 13
# print(S.countDigitOne(n))
# n = 32
# print(S.countDigitOne(n))
# n = 1
# print(S.countDigitOne(n))
# n = 100
# print(S.countDigitOne(n))
n = 3312
print(S.countDigitOne(n))
n = 3342
print(S.countDigitOne(n))