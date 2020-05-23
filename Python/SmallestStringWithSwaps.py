"""
You are given a string s, and an array of pairs of indices in the string pairs where pairs[i] = [a, b] indicates 2 indices(0-indexed) of the string.

You can swap the characters at any pair of indices in the given pairs any number of times.

Return the lexicographically smallest string that s can be changed to after using the swaps.

 

Example 1:

Input: s = "dcab", pairs = [[0,3],[1,2]]
Output: "bacd"
Explaination: 
Swap s[0] and s[3], s = "bcad"
Swap s[1] and s[2], s = "bacd"
Example 2:

Input: s = "dcab", pairs = [[0,3],[1,2],[0,2]]
Output: "abcd"
Explaination: 
Swap s[0] and s[3], s = "bcad"
Swap s[0] and s[2], s = "acbd"
Swap s[1] and s[2], s = "abcd"
Example 3:

Input: s = "cba", pairs = [[0,1],[1,2]]
Output: "abc"
Explaination: 
Swap s[0] and s[1], s = "bca"
Swap s[1] and s[2], s = "bac"
Swap s[0] and s[1], s = "abc"

 

Constraints:

1 <= s.length <= 10^5
0 <= pairs.length <= 10^5
0 <= pairs[i][0], pairs[i][1] < s.length
s only contains lower case English letters.
"""
# from collections import defaultdict
# class Solution:
#     def smallestStringWithSwaps(self, s, pairs):
#         """
#         thoughts: merge all the connected pairs, then sort them
#          TLE       
#         """
#         def findRoot(n):
#             while root[n] != n:
#                 tmp = n
#                 n = root[tmp]
#                 if n is None:
#                     return None
#                 root[tmp] = n
#             return n

#         def setRoot(n,r):
#             if r in visited_node:
#                 r = findRoot(r)
#             if n not in visited_node:
#                 root[n] = r
#                 visited_node.add(n)
#             else:
#                 root[findRoot(n)] = r
#             visited_node.add(r)

#         visited_node = set()
#         len_s = len(s)
#         root = [None]*len_s
#         for i,j in pairs:
#             setRoot(i,i)
#             setRoot(j,i)

#         # print(root)
#         node_dict = defaultdict(list)
#         for node in range(len_s):
#             if node not in visited_node:
#                 node_dict[-1].append(node)
#             else:
#                 node_dict[findRoot(node)].append(node)
#         node_list = sorted(node_dict.keys(), key = lambda x:min(node_dict[x]))
#         res = [None]*len_s
#         # print(node_dict)
#         # print(node_list)
#         for key in node_list:
#             pos = sorted(node_dict[key])
#             letters = sorted([s[i] for i in node_dict[key]])
#             if key == -1:
#                 for j in pos:
#                     res[j] = s[j]
#             else:
#                 for i in range(len(pos)):
#                     res[pos[i]] = letters[i]
#         return ''.join(res)



from collections import defaultdict
class Solution:
    def smallestStringWithSwaps(self, s, pairs):
        """
        thoughts: merge all the connected pairs, then sort them
        still TLe
        """
        def findRoot(n):
            """
            This will TLE
            while n != root[n]:
                tmp = n
                n = root[tmp]
                root[tmp] = n
                # root[n] = findRoot(root[n])
            return n
            """
            if n != root[n]:
                root[n] = findRoot(root[n])
            return root[n]
            
        def union(i,j):
            root[findRoot(i)] = findRoot(j)
            


        len_s = len(s)
        root = list(range(len_s))

        for i,j in pairs:
            union(i,j)


        
        node_dict = defaultdict(list)
        for node in range(len_s):
            node_dict[findRoot(node)].append(s[node])


        res = list(s)
        # print(root)
        # print(node_dict)
        for key in node_dict.keys():
            node_dict[key].sort(reverse = True)

        for node in range(len_s):
            res[node] = node_dict[findRoot(node)].pop()

        return ''.join(res)

S = Solution()
s = "dcab"
pairs = [[0,3],[1,2]]
print(S.smallestStringWithSwaps(s,pairs))

s = "dcab"
pairs = [[0,3],[1,2],[0,2]]
print(S.smallestStringWithSwaps(s,pairs))

s = "cba"
pairs = [[0,1],[1,2]]
print(S.smallestStringWithSwaps(s,pairs))

s = "dcab"
pairs = []
print(S.smallestStringWithSwaps(s,pairs))

s = "udyyek"
pairs = [[3,3],[3,0],[5,1],[3,1],[3,4],[3,5]]
print(S.smallestStringWithSwaps(s,pairs))


s = "qdwyt"
pairs = [[2,3],[3,2],[0,1],[4,0],[3,2]]
print(S.smallestStringWithSwaps(s,pairs))