"""
Given a binary string s, return the minimum number of character swaps to make it alternating, or -1 if it is impossible.

The string is called alternating if no two adjacent characters are equal. For example, the strings "010" and "1010" are alternating, while the string "0100" is not.

Any two characters may be swapped, even if they are not adjacent.

 

Example 1:

Input: s = "111000"
Output: 1
Explanation: Swap positions 1 and 4: "111000" -> "101010"
The string is now alternating.
Example 2:

Input: s = "010"
Output: 0
Explanation: The string is already alternating, no swaps are needed.
Example 3:

Input: s = "1110"
Output: -1
 

Constraints:

1 <= s.length <= 1000
s[i] is either '0' or '1'.
"""


from collections import Counter
class Solution:
    def minSwaps(self, string: str) -> int:

        counts = Counter(string)
        zeros = counts['0']
        ones = counts['1']
        if abs(zeros - ones) > 1:
            return -1
        if zeros == ones:
            targets = ['10' * zeros, '01' * zeros]
        elif zeros - ones == 1:
            targets = ['0' + '10' * ones]
        else:  # ones - zeros == 1
            targets = ['1' + '01' * zeros]
        length = len(string)
        res = length
        for target in targets:
            tmp = sum([1 for i in range(length) if string[i] != target[i]])
            res = min(res, tmp // 2)
        return res


S = Solution()
string = "111000"
print(S.minSwaps(string))
string = "010"
print(S.minSwaps(string))
string = "1110"
print(S.minSwaps(string))