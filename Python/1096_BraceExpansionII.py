"""
Under a grammar given below, strings can represent a set of lowercase words.  Let's use R(expr) to denote the set of words the expression represents.

Grammar can best be understood through simple examples:

Single letters represent a singleton set containing that word.
R("a") = {"a"}
R("w") = {"w"}
When we take a comma delimited list of 2 or more expressions, we take the union of possibilities.
R("{a,b,c}") = {"a","b","c"}
R("{{a,b},{b,c}}") = {"a","b","c"} (notice the final set only contains each word at most once)
When we concatenate two expressions, we take the set of possible concatenations between two words where the first word comes from the first expression and the second word comes from the second expression.
R("{a,b}{c,d}") = {"ac","ad","bc","bd"}
R("a{b,c}{d,e}f{g,h}") = {"abdfg", "abdfh", "abefg", "abefh", "acdfg", "acdfh", "acefg", "acefh"}
Formally, the 3 rules for our grammar:

For every lowercase letter x, we have R(x) = {x}
For expressions e_1, e_2, ... , e_k with k >= 2, we have R({e_1,e_2,...}) = R(e_1) ∪ R(e_2) ∪ ...
For expressions e_1 and e_2, we have R(e_1 + e_2) = {a + b for (a, b) in R(e_1) × R(e_2)}, where + denotes concatenation, and × denotes the cartesian product.
Given an expression representing a set of words under the given grammar, return the sorted list of words that the expression represents.

 

Example 1:

Input: "{a,b}{c,{d,e}}"
Output: ["ac","ad","ae","bc","bd","be"]
Example 2:

Input: "{{a,z},a{b,c},{ab,z}}"
Output: ["a","ab","ac","z"]
Explanation: Each distinct word is written only once in the final answer.
 

Constraints:

1 <= expression.length <= 60
expression[i] consists of '{', '}', ','or lowercase English letters.
The given expression represents a set of words based on the grammar given in the description.
"""

# https://leetcode.com/problems/brace-expansion-ii/discuss/368829/Python3-Stack-Solution
# https://leetcode.com/problems/brace-expansion-ii/discuss/322002/Python-concise-stack-solution
class Solution:
    def braceExpansionII(self, expression: str):
        stack, union, product = [], [], ['']
        print(expression)
        for i in range(len(expression)):
            c = expression[i]
            if c.isalpha():
                product = [r + c for r in product]
            elif c == '{':
                stack.append(union)
                stack.append(product)
                union, product = [], ['']
            elif c == '}':
                pre_product, pre_union = stack.pop(), stack.pop()
                product = [p + r for r in product + union for p in pre_product]
                union = pre_union
            else:
                union += product
                product = ['']
            # print(c, stack, union, product)
        return sorted(s for s in set(union + product))


S = Solution()
expression = "{a,b}{c,{d,e}}"
print(S.braceExpansionII(expression))
expression = "{{a,z},a{b,c},{ab,z}}"
print(S.braceExpansionII(expression))
