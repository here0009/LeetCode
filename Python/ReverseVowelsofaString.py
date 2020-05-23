"""
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:

Input: "hello"
Output: "holle"
Example 2:

Input: "leetcode"
Output: "leotcede"
Note:
The vowels does not include the letter "y".
"""
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = 'aeiouAEIOU'
        v_str = [letter for letter in s if letter in vowels][::-1]
        v_str_index = 0
        res = ''
        for letter in s:
            if letter not in vowels:
                res += letter
            else:
                res += v_str[v_str_index]
                v_str_index+=1
        return res

s = Solution()
input_str = "hello"
print(s.reverseVowels(input_str))
input_str = "leetcode"
print(s.reverseVowels(input_str))
input_str = "aA"
print(s.reverseVowels(input_str))