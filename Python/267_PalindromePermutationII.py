"""
Given a string s, return all the palindromic permutations (without duplicates) of it. Return an empty list if no palindromic permutation could be form.

Example 1:

Input: "aabb"
Output: ["abba", "baab"]
Example 2:

Input: "abc"
Output: []

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/palindrome-permutation-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from collections import Counter
class Solution:
    def generatePalindromes(self, s: str):
        def genString(rmd):
            """
            generate palindrom that length == rmd
            """
            if rmd == 0:
                return [center]
            res = []
            for key in keys:
                if counter[key] >= 2:
                    counter[key] -= 2
                    res.extend([key + string + key for string in genString(rmd-2)])
                    counter[key] += 2
            # print(rmd, res)
            return res

        counter = Counter(s)
        center = ''
        res = []
        for k, v in counter.items():
            if v % 2 == 1:
                center += k
        # print(s, counter, center)
        if len(center) > 1:
            return res
        keys = list(counter.keys())
        vals = sum(counter.values()) - len(center)
        # print(keys, vals)
        return genString(vals)

S = Solution()
s = "aabb"
print(S.generatePalindromes(s))
s = "abc"
print(S.generatePalindromes(s))
s = "abcbababaxx"
print(S.generatePalindromes(s))
