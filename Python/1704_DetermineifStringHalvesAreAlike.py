"""
You are given a string s of even length. Split this string into two halves of equal lengths, and let a be the first half and b be the second half.

Two strings are alike if they have the same number of vowels ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'). Notice that s contains uppercase and lowercase letters.

Return true if a and b are alike. Otherwise, return false.

 

Example 1:

Input: s = "book"
Output: true
Explanation: a = "bo" and b = "ok". a has 1 vowel and b has 1 vowel. Therefore, they are alike.
Example 2:

Input: s = "textbook"
Output: false
Explanation: a = "text" and b = "book". a has 1 vowel whereas b has 2. Therefore, they are not alike.
Notice that the vowel o is counted twice.
Example 3:

Input: s = "MerryChristmas"
Output: false
Example 4:

Input: s = "AbCdEfGh"
Output: true
 

Constraints:

2 <= s.length <= 1000
s.length is even.
s consists of uppercase and lowercase letters.
"""

from collections import Counter
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        def calc(string):
            counts = Counter(string)
            return sum(counts[v] for v in vowels)

        s = s.lower()
        vowels = 'aeiou'
        mid = len(s) // 2
        left, right = s[:mid], s[mid:]
        return calc(left) == calc(right)

S = Solution()
s = "book"
print(S.halvesAreAlike(s))
s = "textbook"
print(S.halvesAreAlike(s))
s = "MerryChristmas"
print(S.halvesAreAlike(s))
s = "AbCdEfGh"
print(S.halvesAreAlike(s))