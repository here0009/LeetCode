"""
You have a list of words and a pattern, and you want to know which words in words matches the pattern.

A word matches the pattern if there exists a permutation of letters p so that after replacing every letter x in the pattern with p(x), we get the desired word.

(Recall that a permutation of letters is a bijection from letters to letters: every letter maps to another letter, and no two letters map to the same letter.)

Return a list of the words in words that match the given pattern. 

You may return the answer in any order.

 

Example 1:

Input: words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
Output: ["mee","aqq"]
Explanation: "mee" matches the pattern because there is a permutation {a -> m, b -> e, ...}. 
"ccc" does not match the pattern because {a -> c, b -> c, ...} is not a permutation,
since a and b map to the same letter.
 

Note:

1 <= words.length <= 50
1 <= pattern.length = words[i].length <= 20
"""

class Solution:
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        ans = []
        for word in words:
            if len(word) != len(pattern):
                # print(word)
                continue
            wtp_dict = dict()
            ptw_dict = dict()
            flag = True
            for index in range(len(pattern)):
                pattern_letter = pattern[index]
                word_letter = word[index]
                if word_letter not in wtp_dict:
                    wtp_dict[word_letter] = pattern_letter
                else:
                    if wtp_dict[word_letter] != pattern_letter:
                        flag = False
                        break

                if pattern_letter not in ptw_dict:
                    ptw_dict[pattern_letter] = word_letter
                else:
                    if ptw_dict[pattern_letter] != word_letter:
                        flag = False
                        break

            # print(letter_dict)
            if flag:
                ans.append(word)
        return ans

s = Solution()


words = ["abc","deq","mee","aqq","dkd","ccc", "ab"]
pattern = "abb"

# words = ["abc"]
# pattern = "abb"
print(s.findAndReplacePattern(words, pattern))