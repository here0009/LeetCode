"""
给定一个整数，打印该整数的英文描述。

示例 1:

输入: 123
输出: "One Hundred Twenty Three"
示例 2:

输入: 12345
输出: "Twelve Thousand Three Hundred Forty Five"
示例 3:

输入: 1234567
输出: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
示例 4:

输入: 1234567891
输出: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"
注意：本题与 273 题相同：https://leetcode-cn.com/problems/integer-to-english-words/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/english-int-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

提示：

0 <= num <= 2**31 - 1
at most 10**10
"""


class Solution:
    def numberToWords(self, num: int) -> str:
        def toWords(str_num):
            num = int(str_num)
            if num == 0:
                return ''
            elif num < 20:
                res = one_to_19[num - 1]
            elif num >= 100:
                q, rmd = divmod(num, 100)
                res = one_to_19[q - 1] + ' ' + 'Hundred'
                if rmd:
                    res += ' ' + toWords(str(rmd))
            else:
                q, rmd = divmod(num, 10)
                res = twenty_to_100[q - 2]
                if rmd:
                    res += ' ' + one_to_19[rmd - 1]
            return res

        if num == 0:
            return 'Zero'
        str_num = str(num)
        words = []
        one_to_19 = 'One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen'.split()
        twenty_to_100 = 'Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split()
        lst = ['', ' Thousand', ' Million', ' Billion']
        idx = 0
        while str_num:
            w = toWords(str_num[-3:])
            if w:
                words.append(w + lst[idx])
            str_num = str_num[:-3]
            idx += 1
        return ' '.join(words[::-1])

S = Solution()
# num = 123
# print(S.numberToWords(num))
# num = 12345
# print(S.numberToWords(num))
# num = 1234567
# print(S.numberToWords(num))
# num = 1234567891
# print(S.numberToWords(num))
num = 1000
print(S.numberToWords(num))