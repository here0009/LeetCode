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

5 <= word.length <= 2 * 105
word consists only of lowercase English letters.
0 <= k <= word.length - 5
"""

from collections import Counter

class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        
        vowels = set('aeiou')
        length = len(word)
        
        def check(vowel_counter, consonants, m):
            return len(vowel_counter) >= 5 and consonants >=m
        
        def count_substr(m:int) -> int:
            counts = 0
            vowel_counter = dict()
            consonants = 0
            j = 0
            for i in range(length):
                while j < length and (not check(vowel_counter, consonants, m)):
                    if word[j] in vowels:
                        vowel_counter[word[j]] = vowel_counter.get(word[j], 0) + 1
                    else:
                        consonants += 1
                    j += 1
                if check(vowel_counter, consonants, m):
                    counts += length - j + 1 
                if word[i] in vowels:
                    vowel_counter[word[i]] -= 1
                    if vowel_counter[word[i]] == 0:
                        del vowel_counter[word[i]]
                else:
                    consonants -= 1
            return counts

        res = count_substr(k) - count_substr(k + 1)
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