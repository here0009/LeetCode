"""
Given an array equations of strings that represent relationships between variables, each string equations[i] has length 4 and takes one of two different forms: "a==b" or "a!=b".  Here, a and b are lowercase letters (not necessarily different) that represent one-letter variable names.

Return true if and only if it is possible to assign integers to variable names so as to satisfy all the given equations.

 

Example 1:

Input: ["a==b","b!=a"]
Output: false
Explanation: If we assign say, a = 1 and b = 1, then the first equation is satisfied, but not the second.  There is no way to assign the variables to satisfy both equations.
Example 2:

Input: ["b==a","a==b"]
Output: true
Explanation: We could assign a = 1 and b = 1 to satisfy both equations.
Example 3:

Input: ["a==b","b==c","a==c"]
Output: true
Example 4:

Input: ["a==b","b!=c","c==a"]
Output: false
Example 5:

Input: ["c==c","b==d","x!=z"]
Output: true
 

Note:

1 <= equations.length <= 500
equations[i].length == 4
equations[i][0] and equations[i][3] are lowercase letters
equations[i][1] is either '=' or '!'
equations[i][2] is '='
"""
from collections import defaultdict
class Solution:
    def equationsPossible(self, equations: 'List[str]') -> 'bool':
        letter_group = dict()
        e_dict = defaultdict(set)
        dict_value = 0
        not_equals = list()
        for equation in equations:
            left, right = equation[0], equation[-1]
            if equation[1] == '=':
                equal = True
            else:
                equal = False
                not_equals.append(equation)

            if equal:
                if left not in letter_group and right not in letter_group:
                    dict_value += 1
                    e_dict[dict_value].add(left)
                    e_dict[dict_value].add(right)
                    letter_group[left] = dict_value
                    letter_group[right] = dict_value
                elif left not in letter_group:
                    tmp = letter_group[right]
                    letter_group[left] = tmp
                    e_dict[tmp].add(left)
                elif right not in letter_group:
                    tmp = letter_group[left]
                    letter_group[right] = tmp
                    e_dict[tmp].add(right)
                else:
                    tmp_left = letter_group[left]
                    tmp_right = letter_group[right]
                    if tmp_left != tmp_right:
                        tmp_min = min(tmp_left, tmp_right)
                        tmp_max = max(tmp_left, tmp_right)
                        e_dict[tmp_min] = e_dict[tmp_min].union(e_dict[tmp_max]) #merge the set
                        e_dict.pop(tmp_max, None)
                        #update letter_group
                        for s in e_dict[tmp_min]:
                            letter_group[s] = tmp_min

        for equation in not_equals:
            left, right = equation[0], equation[-1]
            if left == right:
                return False
            if left in letter_group and right in letter_group and letter_group[left] == letter_group[right]:
                return False

        # print(letter_group)
        # print(e_dict)
        return True

s = Solution()
equations = ["a==b","b!=a"]
print(s.equationsPossible(equations))

equations = ["b==a","a==b"]
print(s.equationsPossible(equations))

equations = ["a==b","b==c","a==c"]
print(s.equationsPossible(equations))

equations = ["a==b","b!=c","c==a"]
print(s.equationsPossible(equations))

equations = ["c==c","b==d","x!=z"]
print(s.equationsPossible(equations))

equations = ["c==c","f!=a","f==b","b==c"]
print(s.equationsPossible(equations))

equations = ["e!=c","b!=b","b!=a","e==d"]
print(s.equationsPossible(equations))

equations = ["e==d","e==a","f!=d","b!=c","a==b"]
print(s.equationsPossible(equations))

equations = ["b==d","c==a","h==a","d==d","a==b","h!=k","i==h"]
print(s.equationsPossible(equations))
