"""
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Write a function to count the total strobogrammatic numbers that exist in the range of low <= num <= high.

Example:

Input: low = "50", high = "100"
Output: 3 
Explanation: 69, 88, and 96 are three strobogrammatic numbers.
Note:
Because the range might be a large number, the low and high numbers are represented as string.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/strobogrammatic-number-iii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""




from functools import lru_cache
class Solution:
    def strobogrammaticInRange(self, low: str, high: str) -> int:
        """
        self strobogrammatic 0,1,8
        strobogrammatic pairs 6-9
        """
        @lru_cache(None)
        def candidateNums(length):
            if length == 0:
                return []
            if length == 1:
                return len_1_list
            if length == 2:
                return len_2_list
            res = []
            candi = ['0'*(length-2)] + candidateNums(length-2)
            for s in len_2_list:
                pre, suf = list(s)
                for c in candi:
                    res.append(pre+c+suf)
            return res

        length_min = len(low)
        length_high = len(high)
        len_1_list = ['1', '8']
        len_2_list = ['11','69','88','96']
        res = 0
        res_list = []
        flag = False
        for length in range(length_min, length_high+1):
            candi = candidateNums(length)
            if length == 1:
                candi = ['0'] + candi
            # print(candi)
            for c in candi:
                if length == length_high and c > high:
                    flag = True
                    break
                if c >= low:
                    res += 1
                    res_list.append(c)
            print(res_list)
            if flag:
                break
        return res

from functools import lru_cache
class Solution:
    def strobogrammaticInRange(self, low: str, high: str) -> int:
        """
        self strobogrammatic 0,1,8
        strobogrammatic pairs 6-9
        """
        def compare(s, t):
            """
            1 for s > t, -1 for s < t, 0 for s == t
            """
            if len(s) > len(t):
                return 1
            elif len(s) < len(t):
                return -1
            else:
                if s == t:
                    return 0
                elif s > t:
                    return 1
                else:
                    return -1

        @lru_cache(None)
        def candidateNums(length):
            if length == 0:
                return []
            if length == 1:
                return len_1_list
            if length == 2:
                return len_2_list
            res = []
            candi = candidateNums(length-2)
            for s in len_2_list:
                pre, suf = list(s)
                for c in candi:
                    res.append(pre+c+suf)
            return res

        length_min = len(low)
        length_high = len(high)
        len_1_list = ['0','1', '8']
        len_2_list = ['00', '11','69','88','96']
        # for i in range(7):
        #     print(i, candidateNums(i))
        res = 0
        res_list = []
        flag = False
        for length in range(length_min, length_high+1):
            candi = candidateNums(length)
            # print(length, candi)
            for c in candi:
                if compare(c, high) == 1:
                    flag = True
                    break
                if compare(c, low) >= 0 and (c[0] != '0' or c == '0'):
                    res += 1
                    res_list.append(c)
            if flag:
                break
        # print(res_list)
        return res


from functools import lru_cache
class Solution:
    def strobogrammaticInRange(self, low: str, high: str) -> int:
        """
        self strobogrammatic 0,1,8
        strobogrammatic pairs 6-9
        """
        def compare(s, t):
            """
            return True is s >= t, else False
            """
            if len(s) > len(t):
                return True
            elif len(s) < len(t):
                return False
            else:
                return s >= t

        @lru_cache(None)
        def candidateNums(length):
            """
            return the candidates string of len == length, because we may use strings start with 0 in  the next round, (such as 010, next round will generate 10101), we also generate strings start with 0
            """
            if length == 0:
                return []
            if length == 1:
                return len_1_list
            if length == 2:
                return len_2_list
            res = []
            candi = candidateNums(length-2)
            for s in len_2_list: 
                pre, suf = list(s)
                for c in candi:
                    res.append(pre+c+suf) # add prefix and suffix to strings in candi, so the strings generated is also strobogrammatic, the strings were generated based on their values, so if the generated value larger than high we can break the loop
            return res

        length_min = len(low)
        length_high = len(high)
        len_1_list = ['0','1', '8']
        len_2_list = ['00', '11','69','88','96']
        res = 0
        for length in range(length_min, length_high+1):
            candi = candidateNums(length)
            for c in candi:
                if not compare(high, c):  # high < c
                    break
                if compare(c, low) and (c[0] != '0' or c == '0'):  #c >= low
                    res += 1
        return res
S = Solution()
low = "50"
high = "100"
print(S.strobogrammaticInRange(low, high))

low = "0"
high = "1680"
print(S.strobogrammaticInRange(low, high))
# 输出：
# 20
# 预期结果：
# 21
low = "1001"
high = "11111"
print(S.strobogrammaticInRange(low, high))
# 输出：
# 22
# 预期结果：
# 25