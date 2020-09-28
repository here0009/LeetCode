"""
Given an input string , reverse the string word by word. 

Example:

Input:  ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
Output: ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]
Note: 

A word is defined as a sequence of non-space characters.
The input string does not contain leading or trailing spaces.
The words are always separated by a single space.
Follow up: Could you do it in-place without allocating extra space?

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-words-in-a-string-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def reverseWords(self, s) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s_list = ''.join(s).split()
        r_s_list = ' '.join(s_list[::-1])
        # print(r_s_list)
        for i in range(len(s)):
            s[i] = r_s_list[i]
        # print(s)

class Solution:
    def reverseWords(self, s) -> None:
        """
        1. reverse s totally
        2. reverse word in s seperately
        """
        def rev(i,j):
            while i < j:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1

        length = len(s)
        left = 0
        rev(0, length-1)
        # print(s)
        for right in range(length):
            if s[right] == ' ':
                rev(left, right-1)
                left = right+1
        rev(left, length-1) # reverse the last word
        # print(s)



S = Solution()
s = ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
print(S.reverseWords(s))
