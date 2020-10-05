"""
An abbreviation of a word follows the form <first letter><number><last letter>. Below are some examples of word abbreviations:

a) it                      --> it    (no abbreviation)

     1
     ↓
b) d|o|g                   --> d1g

              1    1  1
     1---5----0----5--8
     ↓   ↓    ↓    ↓  ↓    
c) i|nternationalizatio|n  --> i18n

              1
     1---5----0
     ↓   ↓    ↓
d) l|ocalizatio|n          --> l10n

Additionally for any string s of size less than or equal to 2 their abbreviation is the same string s.
Find whether its abbreviation is unique in the dictionary. A word's abbreviation is called unique if any of the following conditions is met:

There is no word in dictionary such that their abbreviation is equal to the abbreviation of word.
Else, for all words in dictionary such that their abbreviation is equal to the abbreviation of word those words are equal to word.
 

Example 1:

Input
["ValidWordAbbr", "isUnique", "isUnique", "isUnique", "isUnique"]
[[["deer", "door", "cake", "card"]], ["dear"], ["cart"], ["cane"], ["make"]]
Output
[null, false, true, false, true]

Explanation
ValidWordAbbr validWordAbbr = new ValidWordAbbr(["deer", "door", "cake", "card"]);
validWordAbbr.isUnique("dear"); // return False
validWordAbbr.isUnique("cart"); // return True
validWordAbbr.isUnique("cane"); // return False
validWordAbbr.isUnique("make"); // return True
 

Constraints:

Each word will only consist of lowercase English characters.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/unique-word-abbreviation
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class ValidWordAbbr:

    def __init__(self, dictionary):
        self.dict = dict()
        dictionary = set(dictionary)
        for word in dictionary:
            tmp = self.abbr(word)
            if tmp in self.dict:
                self.dict[tmp] = None
            else:
                self.dict[tmp] = word

    def abbr(self, word):
        if len(word) < 2:
            return word
        return word[0] + str(len(word)-2) + word[-1]

    def isUnique(self, word: str) -> bool:
        tmp = self.abbr(word)
        if tmp in self.dict:
            return self.dict[tmp] == word
        return True


["ValidWordAbbr","isUnique","isUnique","isUnique","isUnique"]
[[["deer","door","cake","card"]],["dear"],["door"],["cart"],["cake"]]

# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)