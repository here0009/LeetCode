"""
Given a string S and a character C, return an array of integers representing the shortest distance from the character C in the string.

Example 1:

Input: S = "loveleetcode", C = 'e'
Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
 

Note:

S string length is in [1, 10000].
C is a single character, and guaranteed to be in string S.
All letters in S and C are lowercase.
"""
class Solution:
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        res = []
        c_positions = self.find_all(S,C)
        len_c_positions = len(c_positions)
        if len_c_positions == 1:
            for index in range(len(S)):
                res.append(abs(c_positions[0]-index))
            return res


        for index in range(c_positions[0]+1):
            res.append(c_positions[0]-index)
            print("a")
            print(c_positions[0]-index)
        pos_left = 0
        pos_right = 1
        for index in range(c_positions[0]+1, c_positions[-1]):
            if index <= c_positions[pos_right]:
                
                if index-c_positions[pos_left] <= c_positions[pos_right]-index:
                    res.append(index-c_positions[pos_left])
                    print("b")
                    print(index-c_positions[pos_left])
                else:
                    res.append(c_positions[pos_right]-index)
                    print("c")
                    print(c_positions[pos_right]-index)
            
            else:
                pos_left += 1
                pos_right += 1
                # if pos_right >= len_c_positions:
                #     break

        for index in range(c_positions[-1], len(S)):
            res.append(index-c_positions[-1])
            print("d")
            print((index-c_positions[-1]))

        return res

    def find_all(self, string, letter):
        """
        return all the positon of letter in str
        """
        res = []
        for index, s in enumerate(string):
            if s == letter:
                res.append(index)
        return res

"""
1. find all c in S, record the positions in a list, distance_list, set the value in distance_list to 0
2. set the element in next to distance_list to 1
3. iterate the process until all the position values are seted.
"""
class Solution_1:
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        distance_list = [-1]*len(S)
        curr_p = []
        processed_p = set()
        next_p = set()
        for c in C:
            p = 0
            while True:
                p = S.find(c, p)
                if p != -1:
                    # distance_list[p] = 0
                    curr_p.append(p)
                    p += 1
                else:
                    break

        # print(curr_p)
        value = 0
        while len(curr_p) > 0:

            for p in curr_p:
                
                distance_list[p] = value
                processed_p.add(p)
                # curr_p.remove(p)
            for p in curr_p:
                if p-1 >=0 and p-1 not in processed_p:
                    next_p.add(p-1)
                if p+1 < len(S) and p+1 not in processed_p:
                    next_p.add(p+1)
            curr_p = list(next_p)
            next_p = set()
            # print(curr_p)
            value += 1

        return distance_list

class Solution_official:
    """
    Thoughts,
    the nearest value is either from left or from right. calulate both of them, then compare to find the answer.
    """
    def shortestToChar(self, S, C):
        prev = float('-inf')
        ans = []
        for i, x in enumerate(S):
            if x == C: prev = i
            ans.append(i - prev)

        prev = float('inf')
        for i in xrange(len(S) - 1, -1, -1):
            if S[i] == C: prev = i
            ans[i] = min(ans[i], prev - i)

        return ans

s = Solution_1()
S = "loveleetcode"
C = 'el'
print(s.shortestToChar(S, C))