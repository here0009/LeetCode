"""
Given a string s consisting only of characters 'a', 'b', and 'c'. You are asked to apply the following algorithm on the string any number of times:

Pick a non-empty prefix from the string s where all the characters in the prefix are equal.
Pick a non-empty suffix from the string s where all the characters in this suffix are equal.
The prefix and the suffix should not intersect at any index.
The characters from the prefix and suffix must be the same.
Delete both the prefix and the suffix.
Return the minimum length of s after performing the above operation any number of times (possibly zero times).

 

Example 1:

Input: s = "ca"
Output: 2
Explanation: You can't remove any characters, so the string stays as is.
Example 2:

Input: s = "cabaabac"
Output: 0
Explanation: An optimal sequence of operations is:
- Take prefix = "c" and suffix = "c" and remove them, s = "abaaba".
- Take prefix = "a" and suffix = "a" and remove them, s = "baab".
- Take prefix = "b" and suffix = "b" and remove them, s = "aa".
- Take prefix = "a" and suffix = "a" and remove them, s = "".
Example 3:

Input: s = "aabccabba"
Output: 3
Explanation: An optimal sequence of operations is:
- Take prefix = "aa" and suffix = "a" and remove them, s = "bccabb".
- Take prefix = "b" and suffix = "bb" and remove them, s = "cca".
 

Constraints:

1 <= s.length <= 105
s only consists of characters 'a', 'b', and 'c'.
"""


class Solution:
    def minimumLength(self, string: str) -> int:
        left, right = 0, len(string) - 1
        while left < right and string[left] == string[right]:
            key = string[left]
            while left < right and string[left] == key:
                left += 1
            while right >= left and string[right] == key:
                right -= 1
            # print(left, right, key, string[left : right + 1])
        return right - left + 1


S = Solution()
string = "ca"
print(S.minimumLength(string))
string = "cabaabac"
print(S.minimumLength(string))
string = "aabccabba"
print(S.minimumLength(string))