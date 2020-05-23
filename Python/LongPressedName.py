"""
Your friend is typing his name into a keyboard.  Sometimes, when typing a character c, the key might get long pressed, and the character will be typed 1 or more times.

You examine the typed characters of the keyboard.  Return True if it is possible that it was your friends name, with some characters (possibly none) being long pressed.

 

Example 1:

Input: name = "alex", typed = "aaleex"
Output: true
Explanation: 'a' and 'e' in 'alex' were long pressed.
Example 2:

Input: name = "saeed", typed = "ssaaedd"
Output: false
Explanation: 'e' must have been pressed twice, but it wasn't in the typed output.
Example 3:

Input: name = "leelee", typed = "lleeelee"
Output: true
Example 4:

Input: name = "laiden", typed = "laiden"
Output: true
Explanation: It's not necessary to long press any character.
 

Note:

name.length <= 1000
typed.length <= 1000
The characters of name and typed are lowercase letters.
"""
class Solution:
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        def string_to_list(string):
            pre_letter = ''
            res = []
            for letter in string:
                if letter != pre_letter:
                    res.append([letter, 1])
                    pre_letter = letter
                else:
                    res[-1][1] += 1
            return res


        name_list = string_to_list(name)
        typed_list = string_to_list(typed)

        len_name_list = len(name_list)
        if len_name_list != len(typed_list):
            return False
        for index in range(len_name_list):
            if name_list[index][0] != typed_list[index][0] or name_list[index][1] > typed_list[index][1]:
                return False
        return True

s = Solution()
name = "alex"
typed = "aaleex"
print(s.isLongPressedName(name, typed))

name = "saeed"
typed = "ssaaedd"
print(s.isLongPressedName(name, typed))

name = "leelee"
typed = "lleeelee"
print(s.isLongPressedName(name, typed))

name = "laiden"
typed = "laiden"
print(s.isLongPressedName(name, typed))