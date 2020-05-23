class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        lefts = "([{"
        rights = ")]}"
        symbol_dict = dict(zip(lefts, rights))
        stack = list()
        for symbol in s:
            if symbol in lefts:
                stack.append(symbol)
            elif symbol in rights:
                if len(stack) > 0:
                    tmp = stack.pop()
                    if symbol != symbol_dict[tmp]:
                        return False
                else:
                    return False

        return len(stack) == 0

s = Solution()
string_list = ["()", "()[]{}","(]","([)]", "{[]}"]
for string in string_list:
    print(s.isValid(string))