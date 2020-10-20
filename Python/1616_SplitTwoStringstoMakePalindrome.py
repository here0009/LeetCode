"""
You are given two strings a and b of the same length. Choose an index and split both strings at the same index, splitting a into two strings: aprefix and asuffix where a = aprefix + asuffix, and splitting b into two strings: bprefix and bsuffix where b = bprefix + bsuffix. Check if aprefix + bsuffix or bprefix + asuffix forms a palindrome.

When you split a string s into sprefix and ssuffix, either ssuffix or sprefix is allowed to be empty. For example, if s = "abc", then "" + "abc", "a" + "bc", "ab" + "c" , and "abc" + "" are valid splits.

Return true if it is possible to form a palindrome string, otherwise return false.

Notice that x + y denotes the concatenation of strings x and y.

 

Example 1:

Input: a = "x", b = "y"
Output: true
Explaination: If either a or b are palindromes the answer is true since you can split in the following way:
aprefix = "", asuffix = "x"
bprefix = "", bsuffix = "y"
Then, aprefix + bsuffix = "" + "y" = "y", which is a palindrome.
Example 2:

Input: a = "abdef", b = "fecab"
Output: true
Example 3:

Input: a = "ulacfd", b = "jizalu"
Output: true
Explaination: Split them at index 3:
aprefix = "ula", asuffix = "cfd"
bprefix = "jiz", bsuffix = "alu"
Then, aprefix + bsuffix = "ula" + "alu" = "ulaalu", which is a palindrome.
Example 4:

Input: a = "xbdef", b = "xecab"
Output: false
 

Constraints:

1 <= a.length, b.length <= 105
a.length == b.length
a and b consist of lowercase English letters
"""


class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        """
        TLE
        """
        def isPalindrom(string):
            left, right = 0, len(string)-1
            while left < right:
                if string[left] != string[right]:
                    return False
                left += 1
                right -= 1
            return True

        length = len(a)
        for i in range(length+1):
            s1 = a[:i] + b[i:]
            s2 = b[:i] + a[i:]
            # print(s1,s2)
            if isPalindrom(s1) or isPalindrom(s2):
                return True
        return False


class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        def isPalindrom(string):
            left, right = 0, len(string)-1
            while left < right:
                if string[left] != string[right]:
                    return False
                left += 1
                right -= 1
            return True

        def smiliarity(s1, s2):
            res = 0
            for i in range(half_len):
                if s1[i] == s2[i]:
                    res += 1
                else:
                    break
            return res

        length = len(a)
        half_len = length//2
        rev_a, rev_b = a[::-1], b[::-1]
        n1 = smiliarity(a, rev_b)
        n2 = smiliarity(b, rev_a)
        s1 = a[:n1] + b[n1:]
        s2 = b[:n2] + a[n2:]
        s3 = a[:-n1] + b[-n1:]
        s4 = b[:-n2] + a[-n2:]
        # print(a, b, '+++++++++++++')
        # print(n1, n2, s1, s2, s3, s4)
        if isPalindrom(s1) or isPalindrom(s2) or isPalindrom(s3) or isPalindrom(s4):
            return True
        return False

class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        """
        if a[i] == b[-i], strip a[i] return True if any of the stripped string is palindrome
        """
        length = len(a)
        i, j = 0, length-1

        while i < j and a[i] == b[j]:
            i += 1
            j -= 1
        s1, s2 = a[i:j+1], b[i:j+1]

        i, j = 0, length-1
        while i < j and b[i] == a[j]:
            i += 1
            j -= 1
        s3, s4 = a[i:j+1], b[i:j+1]

        return any(s == s[::-1] for s in [s1, s2, s3, s4])


S = Solution()
a = "x"
b = "y"
print(S.checkPalindromeFormation(a, b))
a = "abdef"
b = "fecab"
print(S.checkPalindromeFormation(a, b))
a = "ulacfd"
b = "jizalu"
print(S.checkPalindromeFormation(a, b))
a = "xbdef"
b = "xecab"
print(S.checkPalindromeFormation(a, b))
a = "pvhmupgqeltozftlmfjjde"
b = "yjgpzbezspnnpszebzmhvp"
print(S.checkPalindromeFormation(a, b))
# 输出：
# false
# 预期：
# true
a = "aejbaalflrmkswrydwdkdwdyrwskmrlfqizjezd"
b = "uvebspqckawkhbrtlqwblfwzfptanhiglaabjea"
print(S.checkPalindromeFormation(a, b))
# 输出：
# false
# 预期：
# true