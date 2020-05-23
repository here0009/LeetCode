"""
Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.
Example 1:
Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]
Note:
You may use one character in the keyboard more than once.
You may assume the input string will only contain letters of alphabet.
"""
class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        row_1 = set("qwertyuiop")
        row_2 = set("asdfghjkl")
        row_3 = set("zxcvbnm")
        rows = [row_1, row_2, row_3]
        res = []
        for word in words:
            letters = set(word.lower())
            # print (letters)
            for row in rows:
                # print(letters - row)
                if len(letters - row) == 0:
                    res.append(word)
                    break
        return res

s = Solution()
test = ["Hello", "Alaska", "Dad", "Peace"]
print(s.findWords(test))
