"""
Convert a non-negative integer num to its English words representation.

 

Example 1:

Input: num = 123
Output: "One Hundred Twenty Three"
Example 2:

Input: num = 12345
Output: "Twelve Thousand Three Hundred Forty Five"
Example 3:

Input: num = 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
Example 4:

Input: num = 1234567891
Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"
 

Constraints:

0 <= num <= 231 - 1
"""

# nums won't bigger than 1E10. so Billion is enough.
class Solution:
    def numberToWords(self, num: int) -> str:
        def wordify(num):
            if num == 0:
                return []
            if num < 20:
                return [one_to_19[num-1]]
            if num < 100:
                d, rmd = divmod(num, 10)
                return [twenty_to_100[d-2]] + wordify(rmd)
            if num < 1000:
                d, rmd = divmod(num, 100)
                return [one_to_19[d-1]] + ['Hundred'] + wordify(rmd)

            res = wordify(num%1000)
            num //= 1000
            for i in range(3):
                if num % 1000 != 0:
                    res = wordify(num%1000) + [tmb[i]] + res
                num //= 1000
            return res


        one_to_19 = 'One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen'.split()
        twenty_to_100 = 'Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split()
        tmb = 'Thousand Million Billion'.split()
        if num == 0:
            return 'Zero'
        return ' '.join(wordify(num))


class Solution:
    def __init__(self):
        self.lessThan20 = ["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
        self.tens = ["","Ten","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"]
        self.thousands = ["","Thousand","Million","Billion"]

    def numberToWords(self, num):
        if num == 0:
            return "Zero"
        res = ""
        for i in range(len(self.thousands)):
            if num % 1000 != 0:
                res = self.helper(num%1000) + self.thousands[i] + " " + res
            num /= 1000
        return res.strip()

    def helper(self, num):
        if num == 0:
            return ""
        elif num < 20:
            return self.lessThan20[num] + " "
        elif num < 100:
            return self.tens[num/10] + " " + self.helper(num%10)
        else:
            return self.lessThan20[num/100] + " Hundred " + self.helper(num%100)

S = Solution()
num = 123
print(S.numberToWords(num))
num = 12345
print(S.numberToWords(num))
num = 1234567
print(S.numberToWords(num))
num = 1234567891
print(S.numberToWords(num))
print(S.numberToWords(20))
print(S.numberToWords(100))