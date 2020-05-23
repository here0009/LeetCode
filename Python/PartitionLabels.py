"""
A string S of lowercase letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.

Example 1:
Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
Note:

S will have length in range [1, 500].
S will consist of lowercase letters ('a' to 'z') only.
"""
class Solution_1:
    def partitionLabels(self, S: str):
        set_S = set(S)
        res = []
        index_list = []
        for letter in set_S:
            index_list.append((S.find(letter), S.rfind(letter)))
        index_list = sorted(index_list, key = lambda x: x[0])
        # print(index_list)
        start, end = index_list[0][0], index_list[0][1]
        res.append(end - start + 1)
        index = 0
        for _s, _e in index_list[1:]:
            if _s > end:
                start, end = _s, _e
                res.append(end - start +1)
                index += 1
            else:
                end = max(end, _e)
                start = min(start, _s)
                res[index] = end - start + 1

        return res

class Solution:
    def partitionLabels(self, S: str):
        last_index_dict = {}
        res = []
        for i,c in enumerate(S):
            last_index_dict[c] = i
        start_index = 0
        last_index = last_index_dict[S[0]]
        for i,c in enumerate(S):
            last_index = max(last_index, last_index_dict[c])
            if last_index == i:
                res.append(last_index - start_index + 1)
                start_index = i+1
        return res


s = Solution()
S = "ababcbacadefegdehijhklij"
print(s.partitionLabels(S))

S = "a"
print(s.partitionLabels(S))