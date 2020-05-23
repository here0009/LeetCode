"""
Given an array of strings products and a string searchWord. We want to design a system that suggests at most three product names from products after each character of searchWord is typed. Suggested products should have common prefix with the searchWord. If there are more than three products with a common prefix return the three lexicographically minimums products.

Return list of lists of the suggested products after each character of searchWord is typed. 

 

Example 1:

Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
Output: [
["mobile","moneypot","monitor"],
["mobile","moneypot","monitor"],
["mouse","mousepad"],
["mouse","mousepad"],
["mouse","mousepad"]
]
Explanation: products sorted lexicographically = ["mobile","moneypot","monitor","mouse","mousepad"]
After typing m and mo all products match and we show user ["mobile","moneypot","monitor"]
After typing mou, mous and mouse the system suggests ["mouse","mousepad"]
Example 2:

Input: products = ["havana"], searchWord = "havana"
Output: [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]
Example 3:

Input: products = ["bags","baggage","banner","box","cloths"], searchWord = "bags"
Output: [["baggage","bags","banner"],["baggage","bags","banner"],["baggage","bags"],["bags"]]
Example 4:

Input: products = ["havana"], searchWord = "tatiana"
Output: [[],[],[],[],[],[],[]]
 

Constraints:

1 <= products.length <= 1000
There are no repeated elements in products.
1 <= Σ products[i].length <= 2 * 10^4
All characters of products[i] are lower-case English letters.
1 <= searchWord.length <= 1000
All characters of searchWord are lower-case English letters.
"""
class TrieNode:
    def __init__(self):
        self.children = {}

class Trietree:
    def __init__(self):
        self.root = TrieNode()

    def dfs(self, root):
        if len(self.res) >= 3:
            return
        for w in root.children:
            if w == '$':
                self.res.append(root.children[w])
                if len(self.res) >= 3:
                    break
            else:
                self.dfs(root.children[w])


    def insert(self, word):
        root = self.root
        for letter in word:
            if letter not in root.children:
                root.children[letter] = TrieNode()
            root = root.children[letter]
        root.children['$'] = word

    def search(self, prefix):
        root = self.root
        for letter in prefix:
            if letter not in root.children:
                return []
            root = root.children[letter]
        self.res = []
        self.dfs(root)
        return self.res

class Solution:
    def suggestedProducts(self, products, searchWord: str):
        t = Trietree()
        products = sorted(products)
        # print(products)
        for p in products:
            t.insert(p)

        res = []
        for i in range(1,len(searchWord)+1): #
            res.append(t.search(searchWord[:i]))
        return res
    
s = Solution()
products = ["mobile","mouse","moneypot","monitor","mousepad"]
searchWord = "mouse"
print(s.suggestedProducts(products, searchWord))

products = ["havana"]
searchWord = "havana"
print(s.suggestedProducts(products, searchWord))


products = ["bags","baggage","banner","box","cloths"]
searchWord = "bags"
print(s.suggestedProducts(products, searchWord))


products = ["havana"]
searchWord = "tatiana"
print(s.suggestedProducts(products, searchWord))
