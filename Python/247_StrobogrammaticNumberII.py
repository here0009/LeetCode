"""
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Find all strobogrammatic numbers that are of length = n.

Example:

Input:  n = 2
Output: ["11","69","88","96"]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/strobogrammatic-number-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def findStrobogrammatic(self, n: int):
        def genSgb(length):
            """
            generate strobogrammatic numbers that got a defined length
            """
            res = []
            l2sbg = ["00" ,"11","69","88","96"] # the strobogrammatic numbers of length 2
            if length == 0:
                return res
            if length == 1:
                return ['0', '1', '8']
            candi = genSgb(length-2)
            if length == 2:
                return l2sbg
            for string in l2sbg:
                pre, suff = string
                for c in candi:
                    res.append(pre + c + suff)
            return res

        return [s for s in genSgb(n) if (s[0] != '0' or s == '0')]


class Solution:
    def findStrobogrammatic(self, n: int):
        def helper(left, right, tmp = [None] * n, res = tuple()):
            if left > right: return ("".join(tmp),)
            for k, v in (('0', '0'), ('1', '1'), ('6', '9'), ('8', '8'), ('9', '6')):
                if not left and right and k == '0' or left == right and k != v: continue
                tmp[left], tmp[right] = k, v
                res += helper(left + 1, right - 1)
            return res
        return helper(0, n - 1)

作者：mimosys
链接：https://leetcode-cn.com/problems/strobogrammatic-number-ii/solution/c-python-247-zhong-xin-dui-cheng-shu-iishuang-zhi-/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
S = Solution()
for i in range(6):
    print(i, S.findStrobogrammatic(i))
