"""
You are given a string expression representing a Lisp-like expression to return the integer value of.

The syntax for these expressions is given as follows.

An expression is either an integer, a let-expression, an add-expression, a mult-expression, or an assigned variable. Expressions always evaluate to a single integer.
(An integer could be positive or negative.)
A let-expression takes the form (let v1 e1 v2 e2 ... vn en expr), where let is always the string "let", then there are 1 or more pairs of alternating variables and expressions, meaning that the first variable v1 is assigned the value of the expression e1, the second variable v2 is assigned the value of the expression e2, and so on sequentially; and then the value of this let-expression is the value of the expression expr.
An add-expression takes the form (add e1 e2) where add is always the string "add", there are always two expressions e1, e2, and this expression evaluates to the addition of the evaluation of e1 and the evaluation of e2.
A mult-expression takes the form (mult e1 e2) where mult is always the string "mult", there are always two expressions e1, e2, and this expression evaluates to the multiplication of the evaluation of e1 and the evaluation of e2.
For the purposes of this question, we will use a smaller subset of variable names. A variable starts with a lowercase letter, then zero or more lowercase letters or digits. Additionally for your convenience, the names "add", "let", or "mult" are protected and will never be used as variable names.
Finally, there is the concept of scope. When an expression of a variable name is evaluated, within the context of that evaluation, the innermost scope (in terms of parentheses) is checked first for the value of that variable, and then outer scopes are checked sequentially. It is guaranteed that every expression is legal. Please see the examples for more details on scope.
Evaluation Examples:
Input: (add 1 2)
Output: 3

Input: (mult 3 (add 2 3))
Output: 15

Input: (let x 2 (mult x 5))
Output: 10

Input: (let x 2 (mult x (let x 3 y 4 (add x y))))
Output: 14
Explanation: In the expression (add x y), when checking for the value of the variable x,
we check from the innermost scope to the outermost in the context of the variable we are trying to evaluate.
Since x = 3 is found first, the value of x is 3.

Input: (let x 3 x 2 x)
Output: 2
Explanation: Assignment in let statements is processed sequentially.

Input: (let x 1 y 2 x (add x y) (add x y))
Output: 5
Explanation: The first (add x y) evaluates as 3, and is assigned to x.
The second (add x y) evaluates as 3+2 = 5.

Input: (let x 2 (add (let x 3 (let x 4 x)) x))
Output: 6
Explanation: Even though (let x 4 x) has a deeper scope, it is outside the context
of the final x in the add-expression.  That final x will equal 2.

Input: (let a1 3 b2 (add a1 1) b2) 
Output 4
Explanation: Variable names can contain digits after the first character.

Note:

The given string expression is well formatted: There are no leading or trailing spaces, there is only a single space separating different components of the string, and no space between adjacent parentheses. The expression is guaranteed to be legal and evaluate to an integer.
The length of expression is at most 2000. (It is also non-empty, as that would not be a legal expression.)
The answer and all intermediate calculations of that answer are guaranteed to fit in a 32-bit integer.
"""


# https://leetcode.com/problems/parse-lisp-expression/discuss/109709/python-solution-using-stacks.

class Solution:
    # the conciseness of this solution comes from the great separation of reponsibilities.
    # all layer transitions and string tokenization are handled by the plain expresion iteration "for c in experssion:"
    # all simple calculations are handled by the self-defined evaluate() function
    # these two responsibilities are all you need for this Lisp Parser.
    def evaluate(self, expression: str) -> int:
        # token and stack to separate different layers of expressions
        # dictionary to memorize let
        tokens, st, d = [''], [], {}
        def evaluate(tokens): # process the current layer of expression
            if tokens[0] in ['add', 'mult']:
                n1, n2 = int(d.get(tokens[1], tokens[1])), int(d.get(tokens[2], tokens[2]))
                return str(n1+n2) if tokens[0] == 'add' else str(n1*n2)
            else: # let, update dictionary
                # skip the last one because it's not updating the dictionary
                # d.get() handles both token being var or integer
                for i in range(1, len(tokens)-2, 2): d[tokens[i]] = d.get(tokens[i+1], tokens[i+1])
                # the last token cannot be a nested expression which is intercepted before entering this
                # so it can only be a variable, an integer or ''
                return d.get(tokens[-1], tokens[-1]) 
            
        for c in expression:
            # 4 situations: 
            # transit layers: 1. enter the deeper layer, 2. get back from the deeper layer, 
            # current layer: 3. start a new token, 4. continue reading the current token
            # the magic is, by using stack, recursions for the deeper layers are avoided
            if c == '(':
                # update the dictionary before entering the deeper layer
                if tokens[0] == 'let': evaluate(tokens)
                # tokens is reserved because the "tokens" in the next line is entirely overwritten as a new variable. (for example, tokens[-1] = 'a' won't reserve it)
                # d is reserved because of dict()
                st.append((tokens, dict(d)))
                tokens = ['']
            elif c == ')':
                # get the current layer value
                val = evaluate(tokens)
                tokens, d = st.pop()
                # update the outside layer
                tokens[-1] += val
            elif c == ' ': tokens.append('')
            else: tokens[-1] += c
        # make sure to have the return outside the for loop
        return int(tokens[0])

class Solution:
    def evaluate(self, expression):
        st, d, tokens = [], {}, ['']

        def getval(x):
            return d.get(x, x)

        def evaluate(tokens):
            if tokens[0] in ('add', 'mult'):
                tmp = list(map(int, map(getval, tokens[1:])))
                return str(tmp[0] + tmp[1] if tokens[0] == 'add' else tmp[0] * tmp[1])
            else:  # let
                for i in range(1, len(tokens) - 1, 2):
                    if tokens[i+1]:
                        d[tokens[i]] = getval(tokens[i + 1])
                return getval(tokens[-1])

        # print(expression)
        for c in expression:
            if c == '(':
                if tokens[0] == 'let':
                    evaluate(tokens)
                st.append((tokens, dict(d)))
                tokens = ['']
            elif c == ' ':
                tokens.append('')
            elif c == ')':
                val = evaluate(tokens)
                tokens, d = st.pop()
                tokens[-1] += val
            else:
                tokens[-1] += c
        return int(tokens[0])

class Solution:
    def evaluate(self, expression):
        """
        Thoughts: 
        use a dict to store the variable information.
        use a stack to record the token and dict information of current layer
        if we met 'let', update the dict
        if we met 'add' or 'mul', calculate the val
        if we met ')', eval the tokens and dict
        """
        # print(expression)
        def solve(tokens):
            if tokens[0] == 'let':
                for i in range(1, len(tokens) - 1, 2):
                    if tokens[i + 1]:
                        memo[tokens[i]] = memo.get(tokens[i + 1], tokens[i + 1])
                return memo.get(tokens[-1], tokens[-1])
            else:  # add or mul
                a, b = int(memo.get(tokens[1], tokens[1])), int(memo.get(tokens[2], tokens[2]))
                if tokens[0] == 'add':
                    return str(a + b)
                elif tokens[0] == 'mult':
                    return str(a * b)


        stack, memo, tokens = [], dict(), ['']
        for ch in expression:
            if ch == '(':
                if tokens[0] == 'let':
                    solve(tokens)
                stack.append((tokens, dict(memo)))  # use dict to copy memo, other wise memo will influenced by future steps
                tokens = ['']
            elif ch == ')':
                val = solve(tokens)
                tokens, memo = stack.pop()
                tokens[-1] += val  # there is an extra space before each (, val will be added to it
            elif ch == ' ':
                tokens.append('')
            else:
                tokens[-1] += ch
        return int(tokens[0])


S = Solution()
expression = '(let x 1 y 2 x (add x y) (add x y))'
print(S.evaluate(expression))
expression = '(let x 2 (mult x (let x 3 y 4 (add x y))))'
print(S.evaluate(expression))
expression = '(add 1 2)'
print(S.evaluate(expression))
expression = '(mult 3 (add 2 3))'
print(S.evaluate(expression))
expression = '(let x 2 (mult x 5))'
print(S.evaluate(expression))
expression = '(let x 2 (mult x (let x 3 y 4 (add x y))))'
print(S.evaluate(expression))
expression = '(let x 3 x 2 x)'
print(S.evaluate(expression))
expression = '(let x 1 y 2 x (add x y) (add x y))'
print(S.evaluate(expression))
expression = '(let x 2 (add (let x 3 (let x 4 x)) x))'
print(S.evaluate(expression))
expression = '(let a1 3 b2 (add a1 1) b2)'
print(S.evaluate(expression))
                # print(ch, '==================')
                # print(stack)
                # print(memo)
                # print(tokens)