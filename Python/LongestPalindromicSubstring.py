class Solution(object):
    """
    Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

    Example:

    Input: "babad"

    Output: "bab"

    Note: "aba" is also a valid answer.
    Example:

    Input: "cbbd"

    Output: "bb"
    """
    def lenExpanded(self, left, right,k):

        while (left >= 0 and right < len(k) and k[left] == k[right]):
            left-=1
            right+=1

        #when left the while loop, the condition is not met, either out of range or k[left] != k[right], so the return value should be k[left+1 : right]
        return k[left+1 : right]

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 1:
            return s
        if len(s) == 2:
            if s[0] != s[1]:
                return s[0]
            else:
                return s


        longest_palindrome = ""
        #one letter in the middle
        for i in range(len(s)):
            palindrom = self.lenExpanded(i, i,s) 
            if len(palindrom) > len(longest_palindrome):
                longest_palindrome = palindrom

        #two letters in the middle
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                palindrom = self.lenExpanded(i, i+1,s)
                if len(palindrom) > len(longest_palindrome):
                    longest_palindrome = palindrom
        
        
        return longest_palindrome






s = Solution()
print(s.longestPalindrome("babad"))
print(s.longestPalindrome("cbbd"))
print(s.longestPalindrome("abb"))
print(s.longestPalindrome("a"))
print(s.longestPalindrome("an"))
print(s.longestPalindrome("bb"))
print(s.longestPalindrome("ccc"))
print(s.longestPalindrome("ccd"))
print(s.longestPalindrome("abcdasdfghjkldcba"))

print("**************")
# for i in reversed(range(-3,2)):
#     print(i)