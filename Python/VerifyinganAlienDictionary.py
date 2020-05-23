"""
In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographicaly in this alien language.

 

Example 1:

Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.

Example 2:

Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.

Example 3:

Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).
 

Note:

1 <= words.length <= 100
1 <= words[i].length <= 20
order.length == 26
All characters in words[i] and order are english lowercase letters.
"""
class Solution_1:
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        order_dict = {s:index for index, s in enumerate(order)}
        for i in range(len(words)-1):
            fst, scd = words[i], words[i+1]
            j = 0
            breakFlag = False
            while j < min(len(fst), len(scd)):
                fst_l, scd_l = fst[j], scd[j]
                if order_dict[fst_l] > order_dict[scd_l]:
                    return False
                elif fst_l == scd_l:
                    j+=1
                else:
                    breakFlag = True
                    break
            if not breakFlag and len(fst) > len(scd):
                return False
        return True

class Solution:
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        """
        The code from LeetCode solution, the fastest python, it is more concise
        """
        for i in range(len(words)-1):
            for j in range(len(words[i])):
                if j == len(words[i+1]):
                    #words[i+1][-1] == words[i][j-1], words[i+1] is at the end
                    return False
                elif order.index(words[i][j]) < order.index(words[i+1][j]):
                    break
                elif order.index(words[i][j]) > order.index(words[i+1][j]):
                    return False
        return True

s = Solution()
words = ["hello","leetcode"]
order = "hlabcdefgijkmnopqrstuvwxyz"
print(s.isAlienSorted(words,order))


words = ["word","world","row"]
order = "worldabcefghijkmnpqstuvxyz"
print(s.isAlienSorted(words,order))


words = ["apple","app"]
order = "abcdefghijklmnopqrstuvwxyz"
print(s.isAlienSorted(words,order))

words = ["a","z"]
order = "abcdefghijklmnopqrstuvwxyz"
print(s.isAlienSorted(words,order))

words = ["a","a"]
order = "abcdefghijklmnopqrstuvwxyz"
print(s.isAlienSorted(words,order))


words = ["kuvp","q"]
order = "ngxlkthsjuoqcpavbfdermiywz"
print(s.isAlienSorted(words,order))