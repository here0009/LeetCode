"""
We can rotate digits by 180 degrees to form new digits. When 0, 1, 6, 8, 9 are rotated 180 degrees, they become 0, 1, 9, 8, 6 respectively. When 2, 3, 4, 5 and 7 are rotated 180 degrees, they become invalid.

A confusing number is a number that when rotated 180 degrees becomes a different number with each digit valid.(Note that the rotated number can be greater than the original number.)

Given a positive integer N, return the number of confusing numbers between 1 and N inclusive.

 

Example 1:

Input: 20
Output: 6
Explanation: 
The confusing numbers are [6,9,10,16,18,19].
6 converts to 9.
9 converts to 6.
10 converts to 01 which is just 1.
16 converts to 91.
18 converts to 81.
19 converts to 61.
Example 2:

Input: 100
Output: 19
Explanation: 
The confusing numbers are [6,9,10,16,18,19,60,61,66,68,80,81,86,89,90,91,98,99,100].
 

Note:

1 <= N <= 10^9

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/confusing-number-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def confusingNumberII(self, N: int) -> int:
        def isValid(num):
            rev_str = [rev_dict[i] for i in list(str(num))][::-1]
            rev_num = int(''.join(rev_str))
            # print(num, rev_num)
            return num != rev_num


        def dfs(index, num):
            if index == length:
                self.res += int(num <= N and isValid(num))
                return
            for d in digits:
                dfs(index+1, num*10+d)

        rev_dict = dict(zip('01689', '01986'))
        length = len(str(N))
        digits = [0,1,6,8,9]
        self.res = 0
        dfs(0, 0)
        return self.res


class Solution:
    def confusingNumberII(self, N: int) -> int:
        def isValid(num):
            str_num = str(num)
            rev_str = ''.join([rev_dict[i] for i in list(str_num)][::-1])
            return str_num != rev_str

        # @lru_cache(None)
        def dfs(index, num):
            if index == length:
                return int(num <= N and isValid(num))
            res = 0
            for d in digits:
                res += dfs(index+1, num*10+d)
            return res

        rev_dict = dict(zip('01689', '01986'))
        length = len(str(N))
        digits = [0,1,6,8,9]
        return dfs(0, 0)



# 作者：yuzhifeng1992
# 链接：https://leetcode-cn.com/problems/confusing-number-ii/solution/python-shi-jian-100-fei-hui-su-by-yuzhifeng1992/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

class Solution(object):
    def confusingNumberII(self, N):
        """
        :type N: int
        :rtype: int
        """
        # 计算各位数字
        # 数字位数为digitn
        digitArr = []
        i = N
        while (i > 0):
            digitArr.append(i % 10)
            i = i / 10
        # 获得所有位数均可反转的数量
        validNum = 0
        digitn = len(digitArr)
        # 1至digitn-1位数中的数量
        for i in xrange(digitn - 1):
            validNum += (4 * (5 ** i))
        # 小于N的digitn位数中的数量
        for i in xrange(digitn - 1, -1, -1):
            digit = digitArr[i]
            validDigit = 0
            start = 0
            end = digit
            if (i == 0):
                end = digit + 1
            if (i == digitn - 1):
                start = 1
            for j in xrange(start, end):
                if (self.isConfuseDigit(j)):
                    validDigit += 1
            validNum += (validDigit * (5 ** i))
            if (not self.isConfuseDigit(digit)):
                break

        #获得反转后等于自身数字的数量
        invalidNum = 0
        if (digitn == 1):
            for i in xrange(1,digit + 1):
                if (self.isSelfConfuseDigit(i)):
                    invalidNum += 1
            return validNum - invalidNum

        #统计（1 至（digitn-2）/ 2）数字中可翻转数字数量
        #这些数字可以'0','1','8',''四个轴做翻转得到一颗翻转后等于自身的数字
        #如此可统计出 1 至（digitn-2（digitn为奇数），digitn-1（digitn为偶数））位的翻转后等于自身的数字数量
        invalidPairNum = 1
        a = max(0, (digitn - 2) / 2)
        for i in xrange(a):
            invalidPairNum += 4 * (5 ** i)
        invalidNum += ((invalidPairNum * 4) - 2)
        #统计奇数位数字中digitn-1位的反转后等于自身数字的数量
        #这些数字只能以''为轴翻转
        if (digitn % 2 == 1 and digitn >= 3):
            invalidNum += (4 * 5 ** ((digitn - 3) / 2))
        fullInvalidPairNum = 0
        axisNum = 1
        allConfuseDigit = True
        #最后统计digitn位的反转后等于自身数字的数量，基本原理同上
        for i in xrange(digitn - 1, (digitn + 1)/ 2 - 1, -1):
            digit = digitArr[i]
            validDigit = 0
            start = 0
            end = digit
            if (i == digitn - 1):
                start = 1
            for j in xrange(start, end):
                if (self.isConfuseDigit(j)):
                    validDigit += 1
            fullInvalidPairNum += validDigit * (5 ** (i - ((digitn + 1)/ 2)))
            if (not self.isConfuseDigit(digit)):
                allConfuseDigit = False
                break
        if (digitn % 2 == 1):
            axisNum = 3
        invalidNum += (fullInvalidPairNum * axisNum)
        # 以下部分判断N的整个前半部分反转是否符合要求（即N的前半位数反转后小于其后半位数）
        if (allConfuseDigit and digitn % 2 == 1):
            for j in xrange(digitArr[digitn / 2]):
                if (self.isSelfConfuseDigit(j)):
                    invalidNum += 1
            allConfuseDigit = self.isSelfConfuseDigit(digitArr[digitn / 2]) 
        allConfusedDigitArr = [0] * digitn
        if (allConfuseDigit):
            for i in xrange((digitn + 1)/ 2, digitn):
                digit = digitArr[i]
                confusedDigit = self.getConfusedDigit(digit)
                if (confusedDigit > digitArr[digitn - 1 - i]):
                    allConfuseDigit = False
                    break
                elif (confusedDigit < digitArr[digitn - 1 - i]):
                    break
        if (allConfuseDigit):
            invalidNum += 1
        return validNum - invalidNum
    def isConfuseDigit(self, i):
        return i == 0 or i == 1 or i == 6 or i == 8 or i == 9
    def isSelfConfuseDigit(self, i):
        return i == 0 or i == 1 or i == 8
    def getConfusedDigit(self, i):
        if i == 6:
            return 9
        if i == 9:
            return 6
        return i



# 作者：eastdog
# 链接：https://leetcode-cn.com/problems/confusing-number-ii/solution/xian-ji-suan-mou-wei-shu-de-quan-bu-suan-shu-jie-z/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
from math import log10

class Solution(object):
    def confusingNumberII(self, N):
        """
        :type N: int
        :rtype: int
        """
        rotation = {
            '0': '0',
            '1': '1',
            '6': '9',
            '8': '8',
            '9': '6'
        }

        def is_confusing(number):
            length = len(number)
            rotated = [rotation.get(number[i]) for i in range(length-1, -1, -1)]
            if ''.join(number) == ''.join(rotated):
                return False
            return True


        def sum_bit_n(number_digit):

            if number_digit == 0:
                return 0
            if number_digit == 1:
                return 2
            if number_digit % 2 == 0:
                return 5**(number_digit-1)*4 - 5**((number_digit-2)/2)*4
            return 5**(number_digit-1)*4 - 5**((number_digit-3)/2)*12
        
        def population(size):

            pool = [list('01689')] * (size-1)
            pool.append(list('1689'))
            count = 0
            total = 4 * 5 **(size-1)
            while count < total:
                yield tuple(pool[i][count/(5**i)%5] for i in reversed(range(size)))
                count += 1
            

        bit_N = len(str(N))
        bit_N = int(bit_N)
        count = sum([sum_bit_n(i) for i in range(1, bit_N)])
        for comb in population(bit_N):
            # print(comb, count)
            if comb[0] == '0':
                continue
            if int(''.join(comb)) > N:
                return count
            if is_confusing(comb):
                count += 1
        return count
        


class Solution(object):
    def confusingNumberII(self, N):
        """
        :type N: int
        :rtype: int
        """
        digitArr = []
        i = N
        while (i > 0):
            digitArr.append(i % 10)
            i = i / 10
        validNum = 0
        digitn = len(digitArr)
        for i in xrange(digitn - 1):
            validNum += (4 * (5 ** i))
        for i in xrange(digitn - 1, -1, -1):
            digit = digitArr[i]
            validDigit = 0
            start = 0
            end = digit
            if (i == 0):
                end = digit + 1
            if (i == digitn - 1):
                start = 1
            for j in xrange(start, end):
                if (self.isConfuseDigit(j)):
                    validDigit += 1
            validNum += (validDigit * (5 ** i))
            if (not self.isConfuseDigit(digit)):
                break

        invalidNum = 0
        if (digitn == 1):
            for i in xrange(1,digit + 1):
                if (self.isSelfConfuseDigit(i)):
                    invalidNum += 1
            return validNum - invalidNum


        invalidPairNum = 1
        a = max(0, (digitn - 2) / 2)
        for i in xrange(a):
            invalidPairNum += 4 * (5 ** i)
        invalidNum += ((invalidPairNum * 4) - 2)
        if (digitn % 2 == 1 and digitn >= 3):
            invalidNum += (4 * 5 ** ((digitn - 3) / 2))
        fullInvalidPairNum = 0
        axisNum = 1
        allConfuseDigit = True
        for i in xrange(digitn - 1, (digitn + 1)/ 2 - 1, -1):
            digit = digitArr[i]
            validDigit = 0
            start = 0
            end = digit
            if (i == digitn - 1):
                start = 1
            for j in xrange(start, end):
                if (self.isConfuseDigit(j)):
                    validDigit += 1
            fullInvalidPairNum += validDigit * (5 ** (i - ((digitn + 1)/ 2)))
            if (not self.isConfuseDigit(digit)):
                allConfuseDigit = False
                break
        if (digitn % 2 == 1):
            axisNum = 3
        invalidNum += (fullInvalidPairNum * axisNum)
        if (allConfuseDigit and digitn % 2 == 1):
            for j in xrange(digitArr[digitn / 2]):
                if (self.isSelfConfuseDigit(j)):
                    invalidNum += 1
            allConfuseDigit = self.isSelfConfuseDigit(digitArr[digitn / 2]) 
        allConfusedDigitArr = [0] * digitn
        if (allConfuseDigit):
            for i in xrange((digitn + 1)/ 2, digitn):
                digit = digitArr[i]
                confusedDigit = self.getConfusedDigit(digit)
                if (confusedDigit > digitArr[digitn - 1 - i]):
                    allConfuseDigit = False
                    break
                elif (confusedDigit < digitArr[digitn - 1 - i]):
                    break
        if (allConfuseDigit):
            invalidNum += 1
        return validNum - invalidNum
    def isConfuseDigit(self, i):
        return i == 0 or i == 1 or i == 6 or i == 8 or i == 9
    def isSelfConfuseDigit(self, i):
        return i == 0 or i == 1 or i == 8
    def getConfusedDigit(self, i):
        if i == 6:
            return 9
        if i == 9:
            return 6
        return i

# class Solution:
#     def confusingNumberII(self, N: int) -> int:
#         """
#         可以尝试枚举d位数中有'01689'构成的非confusing number, 再用5**d - 非confusing number及大于N的数
#         """
#         d = len(str(N))
#         res = 5**d

S = Solution()
print(S.confusingNumberII(20))
print(S.confusingNumberII(100))