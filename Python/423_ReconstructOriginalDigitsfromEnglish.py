"""
Given a non-empty string containing an out-of-order English representation of digits 0-9, output the digits in ascending order.

Note:
Input contains only lowercase English letters.
Input is guaranteed to be valid and can be transformed to its original digits. That means invalid inputs such as "abc" or "zerone" are not permitted.
Input length is less than 50,000.
Example 1:
Input: "owoztneoer"

Output: "012"
Example 2:
Input: "fviefuro"

Output: "45"
"""

from collections import Counter
class Solution:
    def originalDigits(self, string: str) -> str:
        l_digits = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
        # total = Counter(''.join(l_digits))
        # print(total)
        digits_dict = dict()
        for i, v in enumerate(l_digits):
            digits_dict[str(i)] = Counter(v)
            # print(i, v, Counter(v))
        string_counter = Counter(string)
        res = ''
        #0-z,2-w,4-r,6-x 8-g
        #h-[3,8], f-[4,5], v-[5,7]
        #o-[0,1,2,4]
        for letter, digit in zip('zwuxgfhvio','0246853791'):
            v = string_counter[letter]
            res += v*digit
            for k in digits_dict[digit]:
                string_counter[k] -= v*digits_dict[digit][k]
        return ''.join(sorted(res))


S = Solution()
string = "owoztneoer"
print(S.originalDigits(string))
string = "fviefuro"
print(S.originalDigits(string))
string = "ereht"
print(S.originalDigits(string))
string = "nnei"
print(S.originalDigits(string))