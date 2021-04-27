"""
请实现整数数字的乘法、减法和除法运算，运算结果均为整数数字，程序中只允许使用加法运算符和逻辑运算符，允许程序中出现正负常数，不允许使用位运算。

你的实现应该支持如下操作：

Operations() 构造函数
minus(a, b) 减法，返回a - b
multiply(a, b) 乘法，返回a * b
divide(a, b) 除法，返回a / b
示例：

Operations operations = new Operations();
operations.minus(1, 2); //返回-1
operations.multiply(3, 4); //返回12
operations.divide(5, -2); //返回-2
提示：

你可以假设函数输入一定是有效的，例如不会出现除法分母为0的情况
单个用例的函数调用次数不会超过1000次

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/operations-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Operations:
    """
    [面试题 16.09. 运算](https://leetcode-cn.com/problems/operations-lcci)
    """
    def __init__(self):
        self.pos = [1]
        self.neg = [-1]
        for i in range(30):
            self.pos += [self.pos[-1] + self.pos[-1]]
            self.neg += [self.neg[-1] + self.neg[-1]]

    def ng(self, x: int):
        if x == 0: return 0
        if x > 0:
            p, n, op = self.pos, self.neg, lambda x, y: x >= y
        else:
            p, n, op = self.neg, self.pos, lambda x, y: x <= y
        res = 0
        i = 30
        while x:
            if op(x, p[i]):
                x += n[i]
                res += n[i]
            i += self.neg[0]
        return res

    def minus(self, a: int, b: int) -> int:
        return a + self.ng(b)

    def multiply(self, a: int, b: int) -> int:
        # 写一种b大于0时的情况，然后配合取反函数适应所有情况，快速乘得用右移，只能递归了
        if a == 0 or b == 0: return 0
        if a == 1: return b
        if b == 1: return a
        if b < 0: return self.ng(self.multiply(a, self.ng(b)))
        mask = res = i = 0
        base = a
        while mask < b and i < 30:
            mask += self.pos[i]
            res += base
            base += base
            i += 1
        res = self.minus(res, self.multiply(a, self.minus(mask, b)))
        return res

    def divide(self, a: int, b: int) -> int:
        if b == 1: return a
        if a < 0: return self.ng(self.divide(self.ng(a), b))
        if b < 0: return self.ng(self.divide(a, self.ng(b)))
        if a < b: return 0
        mask = cur = i = 0
        base = b
        while cur + base <= a and i < 30:
            mask += self.pos[i]
            cur += base
            base += base
            i += 1
        res = mask + self.divide(self.minus(a, cur), b)
        return res


# 作者：jet-lag
# 链接：https://leetcode-cn.com/problems/operations-lcci/solution/wo-jiu-suan-cong-zhe-tiao-xia-qu-e-si-ye-bu-hui-za/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


class Operations:

    def __init__(self):
        pass

    def flip(self, num):
        if num == 0:
            return num
        elif num < 0:
            add = 1
            res = 0
            while 1:
                count = add
                if num + count <= 0:
                    num += count
                    res += count
                else:
                    break
                while 1:
                    count = self.multiply2(count)
                    if num + count <= 0:
                        num += count
                        res += count
                    else:
                        break
            return res
        else:
            add = -1
            res = 0
            while 1:
                count = add
                if num + count >= 0:
                    num += count
                    res += count
                else:
                    break
                while 1:
                    count = self.multiply2(count)
                    if num + count >= 0:
                        num += count
                        res += count
                    else:
                        break
            return res

    def minus(self, a: int, b: int) -> int:
        return a + self.flip(b)

    def abs(self, num):
        if num >= 0:
            return num
        else:
            return self.flip(num)

    def divide2(self, num):
        res = 0
        cur = 0
        while 1:
            t = 2
            count = 1
            if cur + t <= num:
                cur += t
                res += count
            else:
                break
            while 1:
                t = self.multiply2(t)
                count = self.multiply2(count)
                if cur + t <= num:
                    res += count
                    cur += t
                else:
                    break
        if cur < num:
            remainder = 1
        else:
            remainder = 0
        return res, remainder

    def multiply2(self, num):
        return num + num

    def multiply(self, a: int, b: int) -> int:
        neg = (a < 0 and b > 0) or (b < 0 and a > 0)
        a, b = self.abs(a), self.abs(b)
        if a > b:
            a, b = b, a
        if a == 0:
            return 0
        elif a == 1:
            res = b
        elif a == 2:
            res = b + b
        else:
            r, r2 = self.divide2(b)
            half = self.multiply(r, a)
            res = half + half + self.multiply(r2, a)
        if neg:
            res = self.flip(res)
        return res

    def divide(self, a: int, b: int) -> int:
        neg = (a < 0 and b > 0) or (b < 0 and a > 0)
        a, b = self.abs(a), self.abs(b)
        res = 0
        cur = 0
        while 1:
            t = b
            count = 1
            cur += t
            if cur <= a:
                res += count
            else:
                break
            while 1:
                t = self.multiply2(t)
                count = self.multiply2(count)
                if cur + t <= a:
                    res += count
                    cur += t
                else:
                    break
        if neg:
            res = self.flip(res)
        return res
    

# Your Operations object will be instantiated and called as such:
# obj = Operations()
# param_1 = obj.minus(a,b)
# param_2 = obj.multiply(a,b)
# param_3 = obj.divide(a,b)

# 作者：_fsp
# 链接：https://leetcode-cn.com/problems/operations-lcci/solution/man-zu-suo-you-ti-mu-yao-qiu-de-jie-fa-by-_fsp/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。



# Your Operations object will be instantiated and called as such:
# obj = Operations()
# param_1 = obj.minus(a,b)
# param_2 = obj.multiply(a,b)
# param_3 = obj.divide(a,b)

class Operations:
    def __init__(self):
        pass

    def calSign(self, a, b):
        pos = True
        if a < 0:
            pos = not pos
            a = self.minus(0, a)
        if b < 0:
            pos = not pos
            b = self.minus(0, b)
        return (a, b, pos)

    def minus(self, a: int, b: int) -> int:
        # 不用位运算 - 借助str
        if b < 0:
            b = int(str(b)[1:])
        else:
            b = int('-' + str(b))
        return a + b

    def multiply(self, a: int, b: int) -> int:
        # 不用位运算, 十进制乘法, 需要借助str
        a, b, pos = self.calSign(a, b)
        res = 0
        sb = str(b)
        zerobits = 0
        for c in sb[::-1]:
            n = int(c)
            cur = 0
            for i in range(n):
                cur += a
            cur = int(str(cur) + '0' * zerobits)
            zerobits += 1
            res += cur
        return res if pos else self.minus(0, res)

    def divide(self, a: int, b: int) -> int:
        # 十进制除法, 借助str
        a, b, pos = self.calSign(a, b)
        res = 0
        cur = 0
        for c in str(a):
            cur = self.multiply(10, cur) + int(c)
            cnt = 0
            while cur >= b:
                cur = self.minus(cur, b)
                cnt += 1
            res = self.multiply(10, res) + cnt
        return res if pos else self.minus(0, res)

# 作者：suibianfahui
# 链接：https://leetcode-cn.com/problems/operations-lcci/solution/liang-chong-fang-fa-bu-shi-yong-wei-yun-suan-he-sh/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


class Operations:

    def __init__(self):
        pass

    def neg(self, num):
        if num > 0:
            return int('-' + str(num))
        elif num < 0:
            return int(str(num)[1:])
        return 0

    def get_sign(self, a, b):
        sign = 1
        if a < 0:
            a = self.neg(a)
            sign *= -1
        if b < 0:
            b = self.neg(b)
            sign *= -1
        return a, b, sign

    def minus(self, a: int, b: int) -> int:
        return a + self.neg(b)

    def multiply(self, a: int, b: int) -> int:
        a, b, sign = self.get_sign(a, b)
        res = 0
        zeros = ''
        for c in str(a)[::-1]:
            curr = 0
            for i in range(int(c)):
                curr += b
            res += int(str(curr) + zeros)
            zeros += '0'
        return res if sign > 0 else self.neg(res)

    def divide(self, a: int, b: int) -> int:
        a, b, sign = self.get_sign(a, b)
        res = 0
        curr = 0
        for c in str(a):
            curr = self.multiply(curr, 10) + int(c)
            cnt = 0
            while curr >= b:
                curr -= b
                cnt += 1
            res = self.multiply(res, 10) + cnt
        return res if sign > 0 else self.neg(res)


operations = Operations()
print(operations.minus(1, 2))
print(operations.multiply(3, 4))
print(operations.divide(5, -2))