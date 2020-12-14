"""
A gene string can be represented by an 8-character long string, with choices from "A", "C", "G", "T".

Suppose we need to investigate about a mutation (mutation from "start" to "end"), where ONE mutation is defined as ONE single character changed in the gene string.

For example, "AACCGGTT" -> "AACCGGTA" is 1 mutation.

Also, there is a given gene "bank", which records all the valid gene mutations. A gene must be in the bank to make it a valid gene string.

Now, given 3 things - start, end, bank, your task is to determine what is the minimum number of mutations needed to mutate from "start" to "end". If there is no such a mutation, return -1.

Note:

Starting point is assumed to be valid, so it might not be included in the bank.
If multiple mutations are needed, all mutations during in the sequence must be valid.
You may assume start and end string is not the same.
 

Example 1:

start: "AACCGGTT"
end:   "AACCGGTA"
bank: ["AACCGGTA"]

return: 1
 

Example 2:

start: "AACCGGTT"
end:   "AAACGGTA"
bank: ["AACCGGTA", "AACCGCTA", "AAACGGTA"]

return: 2
 

Example 3:

start: "AAAAACCC"
end:   "AACCCCCC"
bank: ["AAAACCCC", "AAACCCCC", "AACCCCCC"]

return: 3
"""


from typing import List
class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        bank_set = set(bank)
        visited = set([start])
        bfs = set([start])
        steps = 0
        length = len(start)
        ATCG = set('ATCG')
        if start == end:
            return steps
        # print(visited, bfs, ATCG, bank_set)
        while bfs:
            for gene in bfs:
                # print(bfs)
                if end in bfs:
                    return steps
                steps += 1
                bfs2 = set()
                for gene in bfs:
                    for i in range(length):
                        for letter in ATCG:
                            if letter != gene[i]:
                                mut_gene = gene[:i] + letter + gene[i+1:]
                                # print(mut_gene, mut_gene in bank_set)
                                if mut_gene not in visited and mut_gene in bank_set:
                                    bfs2.add(mut_gene)
                                    visited.add(mut_gene)
            bfs = bfs2
        return -1


from typing import List
from collections import defaultdict
class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        def mutate(a, b):
            counts = 0
            for i in range(len(a)):
                if a[i] != b[i]:
                    counts += 1
                if counts > 1:
                    return False
            return counts == 1

        if start == end:
            return 0
        bank_set = set(bank)
        if not bank or end not in bank_set:
            return -1
        bank_set.add(start)
        bank = list(bank_set)
        edges = defaultdict(list)
        length = len(bank)

        for i in range(length-1):
            for j in range(i+1, length):
                if mutate(bank[i], bank[j]):
                    edges[i].append(j)
                    edges[j].append(i)
        # start_index, end_index = -1, -1
        for i in range(length):
            if bank[i] == start:
                start_index = i
            elif bank[i] == end:
                end_index = i
        bfs = set([start_index])
        target = end_index
        steps = 0
        visited = set([start_index])
        while bfs:
            bfs2 = set()
            if target in bfs:
                return steps
            for i in bfs:
                for j in edges[i]:
                    if j not in visited:
                        bfs2.add(j)
                        visited.add(j)
            bfs = bfs2
            steps += 1
        return -1


S = Solution()
start = "AACCGGTT"
end = "AACCGGTA"
bank = ["AACCGGTA"]
print(S.minMutation(start, end, bank))
start = "AACCGGTT"
end ="AAACGGTA"
bank = ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
print(S.minMutation(start, end, bank))
start = "AAAAACCC"
end = "AACCCCCC"
bank = ["AAAACCCC", "AAACCCCC", "AACCCCCC"]
print(S.minMutation(start, end, bank))
start = "AAAACCCC"
end = "CCCCCCCC"
bank = ["AAAACCCA","AAACCCCA","AACCCCCA","AACCCCCC","ACCCCCCC","CCCCCCCC","AAACCCCC","AACCCCCC"]
print(S.minMutation(start, end, bank))
"AACCGGTT"
"AACCGGTA"
[]