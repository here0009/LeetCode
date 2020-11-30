"""
Validate if a given string can be interpreted as a decimal number.

Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
" -90e3   " => true
" 1e" => false
"e3" => false
" 6e-1" => true
" 99e2.5 " => false
"53.5e93" => true
" --6 " => false
"-+3" => false
"95a54e53" => false

Note: It is intended for the problem statement to be ambiguous. It would be best if you gathered all requirements up front before implementing one. However, here is a list of characters that can be in a valid decimal number:

Numbers 0-9
Exponent - "e"
Positive/negative sign - "+"/"-"
Decimal point - "."
Of course, the context of these characters also matters in the input.

 

Example 1:

Input: s = "0"
Output: true
Example 2:

Input: s = "3"
Output: true
 

Constraints:

1 <= s.length <= 20
s consists of only English letters, digits, space ' ', plus '+', minus '-', or dot '.'.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


import string
from collections import Counter
class Solution:
    def isNumber(self, s: str) -> bool:
        """
        wrong answer
        """
        s = s.strip().lower()
        if not s or s == '.':
            return False
        unique_letters = set('e.+-')
        valid_letters = set(string.digits + 'e.+-')
        # print(s)
        s_set = set(s)
        counts = Counter(s)
        if s_set - valid_letters:
            return False
        for letter in unique_letters:
            if counts[letter] > 1:
                return False
        if s[0] == 'e' or s[-1] == 'e':
            return False
        if '+' in s_set or '-' in s_set:
            if (counts['+'] + counts['-'] == 1) and (s[0] not in '+-') and (('e' not in s_set) or ('e' in s_set and s[s.find('e')+1] not in '+-')):
                return False
            if counts['+'] + counts['-'] > 3:
                return False
            if counts['+'] + counts['-'] > 2 and s[0] not in '+-' and not ('e+' in string or 'e-' in string):
                return False

        if 'e' in s_set and '.' in s_set and s.find('.') > s.find('e'):
            return False
        if len(s) > 1 and (s[:2] in {'-.', '+.', '++', '--', '.e'} or s[-2:] in {'e+','e-'}):
            return False
        return True


import string
from collections import Counter
class Solution:
    def isNumber(self, s: str) -> bool:


        s = s.strip().lower()
        if len(s) == 0 or s == '.':
            return False
        length = len(s)
        s_set = set(s)
        counts = Counter(s)
        # print(s_set)
        valid_letters = set(string.digits + 'e.+-')
        if s_set - valid_letters:
            return False
        if len(set(string.digits) & s_set) == 0:
            return False
        if counts['.'] > 1:
            return False
        if 'e' in s_set:
            if counts['e'] > 1:
                return False
            if '.' in s_set and s.find('.') > s.find('e'):
                return False
            left, right = s.split('e')
            return self.isNumber(left) and self.isNumber(right)

        if '+' in s_set or '-' in s_set:
            if length == 1:
                return False
            if counts['+'] + counts['-'] > 1:
                return False
            if s[0] not in '+-':
                return False
            if s[-1] in '+-':
                return False
        return True


import string
from collections import Counter
class Solution:
    def isNumber(self, s: str) -> bool:
        def isValid(s):
            s_set = set(s)
            if len(set(string.digits) & s_set) == 0:
                return False
            counts = Counter(s)
            if '+' in s_set or '-' in s_set:
                if length == 1:
                    return False
                if counts['+'] + counts['-'] > 1:
                    return False
                if s[0] not in '+-':
                    return False
                if s[-1] in '+-':
                    return False
            return True

        s = s.strip().lower()
        if len(s) == 0 or s == '.':
            return False
        length = len(s)
        s_set = set(s)
        counts = Counter(s)
        # print(s_set)
        valid_letters = set(string.digits + 'e.+-')
        if s_set - valid_letters:
            return False
        if len(set(string.digits) & s_set) == 0:
            return False
        if counts['.'] > 1:
            return False
        if 'e' in s_set:
            if counts['e'] > 1:
                return False
            if '.' in s_set and s.find('.') > s.find('e'):
                return False
            left, right = s.split('e')
            return isValid(left) and isValid(right)
        return isValid(s)

import string
from collections import Counter
class Solution:
    def isNumber(self, s: str) -> bool:
        def isValid(s):
            s_set = set(s)
            if len(set(string.digits) & s_set) == 0:
                return False
            counts = Counter(s)
            if '+' in s_set or '-' in s_set:
                if counts['+'] + counts['-'] > 1:
                    return False
                if s[0] not in '+-':
                    return False
            return True

        s = s.strip().lower()
        if len(s) == 0 or s == '.':
            return False
        s_set = set(s)
        counts = Counter(s)
        valid_letters = set(string.digits + 'e.+-')
        if s_set - valid_letters:
            return False
        if len(set(string.digits) & s_set) == 0:
            return False
        if counts['.'] > 1:
            return False
        if 'e' in s_set:
            if counts['e'] > 1:
                return False
            if '.' in s_set and s.find('.') > s.find('e'):
                return False
            left, right = s.split('e')
            return isValid(left) and isValid(right)
        return isValid(s)


# 作者：jutraman
# 链接：https://leetcode-cn.com/problems/valid-number/solution/pythonyou-xiao-shu-zi-by-jutraman/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
import re
class Solution:
    def isNumber(self, s: str) -> bool:
        return bool(re.match(r'\s*[+-]?([\d]+(\.[\d]*)?|\.[\d]+)(e[+-]?[\d]+)? *$', s))

class Solution:
    def isNumber(self, s: str) -> bool:
        try:
            float(s)
        except:
            return False
        return True

# https://leetcode.com/problems/valid-number/discuss/348874/Python-3-Regex-with-example
class Solution:
    def isNumber(self, s: str) -> bool:
        import re 
        #Example:               +-     (1 or 1). or (1.2 or .2)   e +- 1     
        engine = re.compile(r"^[+-]?((\d+\.?\d*)|(\d*\.?\d+))(e[+-]?\d+)?$")
        return engine.match(s.strip(" ")) # i prefer this over putting more things (\S*) in regex

class Solution:
    def isNumber(self, s: str) -> bool:
        engine = re.compile(r"^[+-]?((\d+\.?\d*)|(\d*\.?\d+))(e[+-]?\d+)?$")
        if engine.fullmatch(s.strip(' ')):
            print(engine.fullmatch(s.strip(' ')).group(0))
            return True
        else:
            return False


# https://leetcode.com/problems/valid-number/discuss/23728/A-simple-solution-in-Python-based-on-DFA
class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #define DFA state transition tables
        states = [{},
                 # State (1) - initial state (scan ahead thru blanks)
                 {'blank': 1, 'sign': 2, 'digit':3, '.':4},
                 # State (2) - found sign (expect digit/dot)
                 {'digit':3, '.':4},
                 # State (3) - digit consumer (loop until non-digit)
                 {'digit':3, '.':5, 'e':6, 'blank':9},
                 # State (4) - found dot (only a digit is valid)
                 {'digit':5},
                 # State (5) - after dot (expect digits, e, or end of valid input)
                 {'digit':5, 'e':6, 'blank':9},
                 # State (6) - found 'e' (only a sign or digit valid)
                 {'sign':7, 'digit':8},
                 # State (7) - sign after 'e' (only digit)
                 {'digit':8},
                 # State (8) - digit after 'e' (expect digits or end of valid input) 
                 {'digit':8, 'blank':9},
                 # State (9) - Terminal state (fail if non-blank found)
                 {'blank':9}]
        currentState = 1
        for c in s:
            # If char c is of a known class set it to the class name
            if c in '0123456789':
                c = 'digit'
            elif c in ' \t\n':
                c = 'blank'
            elif c in '+-':
                c = 'sign'
            # If char/class is not in our state transition table it is invalid input
            if c not in states[currentState]:
                return False
            # State transition
            currentState = states[currentState][c]
        # The only valid terminal states are end on digit, after dot, digit after e, or white space after valid input
        if currentState not in [3,5,8,9]:
            return False
        return True

# https://leetcode.com/problems/valid-number/discuss/360781/Python-with-state-machine-36ms        
class Solution:
    def isNumber(self, s: str) -> bool:
        # states
        start       = 0
        int_sign    = 1
        integer     = 2
        point       = 3
        frac        = 4
        exp         = 5
        exp_sign    = 6
        exp_int     = 7

        # inputs
        digit       = 1
        sign        = 2
        dot         = 3
        e           = 4

        def classify(c):
            if c in '0123456789': return digit
            if c == '.'         : return dot
            if c in '+-'        : return sign
            if c == 'e'         : return e
            raise ValueError

        machine = {
            start   : {sign:int_sign, digit:integer, dot:point},
            int_sign: {digit:integer, dot:point},
            integer : {digit:integer, dot:frac, e:exp},
            point   : {digit:frac},
            frac    : {digit:frac, e:exp},
            exp     : {digit:exp_int, sign:exp_sign},
            exp_sign: {digit:exp_int},
            exp_int : {digit:exp_int},
        }

        state = start
        for c in s.strip():
            try:
                state = machine[state][classify(c)]
            except: return False
        return state in [integer, frac, exp_int]


class Solution:
    def isNumber(self, s: str) -> bool:
        #state
        state = {}

S = Solution()
s = 'e9'
print(s, S.isNumber(s))
s = "0"
print(s, S.isNumber(s))
# => true
s = " 0.1 "
print(s, S.isNumber(s))
# => true
s = "abc"
print(s, S.isNumber(s))
# => false
s = "1 a"
print(s, S.isNumber(s))
# => false
s = "2e10"
print(s, S.isNumber(s))
# => true
s = " -90e3   "
print(s, S.isNumber(s))
# => true
s = " 1e"
print(s, S.isNumber(s))
# => false
s = "e3"
print(s, S.isNumber(s))
# => false
s = " 6e-1"
print(s, S.isNumber(s))
# => true
s = " 99e2.5 "
print(s, S.isNumber(s))
# => false
s = "53.5e93"
print(s, S.isNumber(s))
# => true
s = " --6 "
print(s, S.isNumber(s))
# => false
s = "-+3"
print(s, S.isNumber(s))
# => false
s = "95a54e53"
print(s, S.isNumber(s))
# => false
s = "95AB54e53"
print(s, S.isNumber(s))
s = "2e0"
print(s, S.isNumber(s))