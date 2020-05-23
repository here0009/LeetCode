"""
We had some 2-dimensional coordinates, like "(1, 3)" or "(2, 0.5)".  Then, we removed all commas, decimal points, and spaces, and ended up with the string S.  Return a list of strings representing all possibilities for what our original coordinates could have been.

Our original representation never had extraneous zeroes, so we never started with numbers like "00", "0.0", "0.00", "1.0", "001", "00.01", or any other number that can be represented with less digits.  Also, a decimal point within a number never occurs without at least one digit occuring before it, so we never started with numbers like ".1".

The final answer list can be returned in any order.  Also note that all coordinates in the final answer have exactly one space between them (occurring after the comma.)

Example 1:
Input: "(123)"
Output: ["(1, 23)", "(12, 3)", "(1.2, 3)", "(1, 2.3)"]
Example 2:
Input: "(00011)"
Output:  ["(0.001, 1)", "(0, 0.011)"]
Explanation: 
0.0, 00, 0001 or 00.01 are not allowed.
Example 3:
Input: "(0123)"
Output: ["(0, 123)", "(0, 12.3)", "(0, 1.23)", "(0.1, 23)", "(0.1, 2.3)", "(0.12, 3)"]
Example 4:
Input: "(100)"
Output: [(10, 0)]
Explanation: 
1.0 is not allowed.
 

Note:

4 <= S.length <= 12.
S[0] = "(", S[S.length - 1] = ")", and the other elements in S are digits.

"""
class Solution:
    def ambiguousCoordinates(self, string: str):
        def addPoint(string):
            if len(string) == 1:
                return [string]
            if string[0] == '0':
                return [string[0]+'.'+string[1:]]
            res = [string]
            if string[-1] == '0':
                return res
            for i in range(1,len(string)):
                res.append(string[:i]+'.'+string[i:])
            return res

        def checkZeros(string):
            return len(string) > 1 and string[0] == '0' and string[-1] == '0'

        string = string[1:len(string)-1]
        # print(string)
        res = []
        for split in range(1,len(string)):
            p, q = string[:split], string[split:]
            if checkZeros(p) or checkZeros(q):
                continue
            p_list = addPoint(p)
            q_list = addPoint(q)
            res.extend(['({}, {})'.format(i,j) for i in p_list for j in q_list])
        return res

S = Solution()
string = "(123)"
print(S.ambiguousCoordinates(string))

string = "(00011)"
print(S.ambiguousCoordinates(string))

string = "(0123)"
print(S.ambiguousCoordinates(string))

string = "(100)"
print(S.ambiguousCoordinates(string))

string = "(0010)"
print(S.ambiguousCoordinates(string))

string = "(0000001)"
print(S.ambiguousCoordinates(string))
