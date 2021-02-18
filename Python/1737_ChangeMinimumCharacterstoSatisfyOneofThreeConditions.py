"""
You are given two strings a and b that consist of lowercase letters. In one operation, you can change any character in a or b to any lowercase letter.

Your goal is to satisfy one of the following three conditions:

Every letter in a is strictly less than every letter in b in the alphabet.
Every letter in b is strictly less than every letter in a in the alphabet.
Both a and b consist of only one distinct letter.
Return the minimum number of operations needed to achieve your goal.

 

Example 1:

Input: a = "aba", b = "caa"
Output: 2
Explanation: Consider the best way to make each condition true:
1) Change b to "ccc" in 2 operations, then every letter in a is less than every letter in b.
2) Change a to "bbb" and b to "aaa" in 3 operations, then every letter in b is less than every letter in a.
3) Change a to "aaa" and b to "aaa" in 2 operations, then a and b consist of one distinct letter.
The best way was done in 2 operations (either condition 1 or condition 3).
Example 2:

Input: a = "dabadd", b = "cda"
Output: 3
Explanation: The best way is to make condition 1 true by changing b to "eee".
 

Constraints:

1 <= a.length, b.length <= 105
a and b consist only of lowercase letters.
"""



class Solution:
    def minCharacters(self, a: str, b: str) -> int:
        def counts(string):
            res = [0] * 26
            for s in string:
                res[ord(s) - ord('a')] += 1
            return res

        def convert(x_counts, y_counts):
            """
            min steps to convert x_counts, so every letter in x < y
            """
            total_x = x_counts[-1]
            res = x_counts[-1] - x_counts[-2] + y_counts[-2]  # change z in x to y and change not z in y to z
            for i in range(25):
                res = min(res, total_x - x_counts[i] + y_counts[i])
            return res

        a_counts = counts(a)
        b_counts = counts(b)
        ab_counts = counts(a + b)
        pre_a, pre_b = [a_counts[0]], [b_counts[0]]
        for _num in a_counts[1:]:
            pre_a.append(pre_a[-1] + _num)
        for _num in b_counts[1:]:
            pre_b.append(pre_b[-1] + _num)

        len_a, len_b = len(a), len(b)
        op3 = len_a + len_b - max(ab_counts)
        res = min(op3, convert(pre_a, pre_b), convert(pre_b, pre_a))
        return res

S = Solution()
a = "aba"
b = "caa"
print(S.minCharacters(a, b))
a = "dabadd"
b = "cda"
print(S.minCharacters(a, b))