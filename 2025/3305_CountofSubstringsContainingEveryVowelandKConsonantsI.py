
"""
You are given a string word and a non-negative integer k.

Return the total number of substrings of word that contain every vowel ('a', 'e', 'i', 'o', and 'u') at least once and exactly k consonants.

 

Example 1:

Input: word = "aeioqq", k = 1

Output: 0

Explanation:

There is no substring with every vowel.

Example 2:

Input: word = "aeiou", k = 0

Output: 1

Explanation:

The only substring with every vowel and zero consonants is word[0..4], which is "aeiou".

Example 3:

Input: word = "ieaouqqieaouqq", k = 1

Output: 3

Explanation:

The substrings with every vowel and one consonant are:

word[0..5], which is "ieaouq".
word[6..11], which is "qieaou".
word[7..12], which is "ieaouq".
 

Constraints:

5 <= word.length <= 250
word consists only of lowercase English letters.
0 <= k <= word.length - 5
"""

from collections import Counter

class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        
        def check(start:int, end:int) -> int:
            consonant = sum([1 for c in word[start:end] if c not in self.vowels])
            # print(consonant)
            if consonant != k or len(self.vowels - set(word[start:end])) > 0:
                return False
            return True
        
        self.vowels = set("aeiou")
        length = len(word)
        res = 0
        for start in range(length - 5 - k + 1):
            for end in range(start + 5 + k, length + 1):
                if check(start, end):
                    res += 1
        return res

# Example usage
def main():
    s = Solution()
    word = "aeioqq"
    k = 1
    print(s.countOfSubstrings(word, k))
    word = "aeiou"
    k = 0
    print(s.countOfSubstrings(word, k))
    word = "ieaouqqieaouqq"
    k = 1
    print(s.countOfSubstrings(word, k))
    word = "iqeaouqi"
    k = 2
    print(s.countOfSubstrings(word, k))
# Example usage
    
if __name__ == "__main__":
    main()