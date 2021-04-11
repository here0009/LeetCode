"""
Given a (0-indexed) integer array nums and two integers low and high, return the number of nice pairs.

A nice pair is a pair (i, j) where 0 <= i < j < nums.length and low <= (nums[i] XOR nums[j]) <= high.

 

Example 1:

Input: nums = [1,4,2,7], low = 2, high = 6
Output: 6
Explanation: All nice pairs (i, j) are as follows:
    - (0, 1): nums[0] XOR nums[1] = 5 
    - (0, 2): nums[0] XOR nums[2] = 3
    - (0, 3): nums[0] XOR nums[3] = 6
    - (1, 2): nums[1] XOR nums[2] = 6
    - (1, 3): nums[1] XOR nums[3] = 3
    - (2, 3): nums[2] XOR nums[3] = 5
Example 2:

Input: nums = [9,8,4,2,1], low = 5, high = 14
Output: 8
Explanation: All nice pairs (i, j) are as follows:
​​​​​    - (0, 2): nums[0] XOR nums[2] = 13
    - (0, 3): nums[0] XOR nums[3] = 11
    - (0, 4): nums[0] XOR nums[4] = 8
    - (1, 2): nums[1] XOR nums[2] = 12
    - (1, 3): nums[1] XOR nums[3] = 10
    - (1, 4): nums[1] XOR nums[4] = 9
    - (2, 3): nums[2] XOR nums[3] = 6
    - (2, 4): nums[2] XOR nums[4] = 5
 

Constraints:

1 <= nums.length <= 2 * 104
1 <= nums[i] <= 2 * 104
1 <= low <= high <= 2 * 104
"""


from typing import List
from collections import defaultdict
class Solution:
    def countPairs(self, nums: List[int], low: int, high: int) -> int:
        """
        TLE
        """
        res = 0
        length = len(nums)
        for i in range(length):
            for j in range(i + 1, length):
                val = nums[i] ^ nums[j]
                if low <= val <= high:
                    res += 1
        return res


from collections import Counter
from typing import List
class Solution:
    def countPairs(self, nums: List[int], low: int, high: int) -> int:
        """
        Thoughts: 
        for num in nums calculate the 
        """

        res = 0
        length = len(nums)
        counts = Counter()
        for num in nums:
            counts[len(bin(num)) - 2] += 1

        for num in nums:
            group = len(bin(num)) - 2


from collections import Counter
from typing import List
class Solution:
    def countPairs(self, nums: List[int], low: int, high: int) -> int:
        def countsmaller(limit):
            res = 0
            for i in range(16):
                signature = limit>>i       # get prefix signature
                if signature & 1:          # the digit of interest is 1 otherwise no pair can be smaller than 0 for this position
                    target = signature - 1 # target is the same as signature, just the last bit is 0
                    prefix_counter = collections.Counter([n>>i for n in nums])
                    #                      # if a^b = target, then they are a "smaller pair" for this signature
                    #                      # so b = a^target or target^a, for each a, we look up for b.
                    res += sum( prefix_counter[a]*prefix_counter[target^a]  for a in prefix_counter)
                    #                      # sum up all the counts for pairs that XOR to this signature.
            return res//2                  # each pair is counted twice
        
        return countsmaller(high+1) - countsmaller(low) # diff gives the range


# https://leetcode.com/problems/count-pairs-with-xor-in-a-range/discuss/1124536/Python3-Trie-with-diagram-and-explanations
class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.count = 0
        
class Trie:
    def __init__(self, maxbits=None):
        self.root = TrieNode()
        self.maxbits = maxbits

    def add(self, v):
        n = self.root
        # build the trie from the left-most bit
        for i in reversed(range(self.maxbits)):
            node_value = (v >> i) & 1
            n.children[node_value].count += 1
            n = n.children[node_value]

    def count(self, v, high):
        cnt = 0
        n = self.root
        for i in reversed(range(self.maxbits)):
            if not n: break

            high_at_bit_i = (high >> i) & 1
            v_at_bit_i = (v >> i) & 1
            if high_at_bit_i:  # x could be v_at_bit_i, and possibly 1-v_at_bit_i
                if v_at_bit_i in n.children:
                    cnt += n.children[v_at_bit_i].count
                n = n.children.get(1 - v_at_bit_i, None)  # diff with v_at_bit_i, so xor will be 1
            else:  # x must be v_at_bit_i
                n = n.children.get(v_at_bit_i, None)

        return cnt


class Solution:
    def countPairs(self, nums: List[int], low: int, high: int) -> int:
        max_bits = len(bin(max(nums))) - 2
        ans = 0
        trie = Trie(max_bits)
        for num in nums:
            ans += trie.count(num, high+1) - trie.count(num, low)  # due to `low <= (nums[i] XOR nums[j]) <= high`
            trie.add(num)
        return ans

# https://leetcode.com/problems/count-pairs-with-xor-in-a-range/discuss/1119703/Python3-trie
class Trie: 
    def __init__(self): 
        self.root = {}
        
    def insert(self, val): 
        node = self.root 
        for i in reversed(range(15)):
            bit = (val >> i) & 1
            if bit not in node: 
                node[bit] = {"cnt": 1}
            else: 
                node[bit]["cnt"] += 1
            node = node[bit]
        
    def count(self, val, high): 
        ans = 0 
        node = self.root
        for i in reversed(range(15)):
            if not node: 
                break 
            bit = (val >> i) & 1 
            cmp = (high >> i) & 1
            if cmp: 
                if node.get(bit, {}): 
                    ans += node[bit]["cnt"]
                node = node.get(1^bit, {})
            else: 
                node = node.get(bit, {})
        return ans 
            
        
class Solution:
    def countPairs(self, nums: List[int], low: int, high: int) -> int:
        trie = Trie()
        
        ans = 0
        for x in nums: 
            ans += trie.count(x, high+1) - trie.count(x, low)
            trie.insert(x)
        return ans 



class Trie:

    def __init__(self):
        self.root = {}

    def insert(self, val):
        node = self.root
        for i in range(16, -1, -1):
            val_i = (val >> i) & 1
            if val_i not in node:
                node[val_i] = {"cnt": 1}
            else:
                node[val_i]['cnt'] += 1
            node = node[val_i]


    def query(self, val, limit):
        node = self.root
        res = 0
        for i in range(16, -1, -1):
            if not node:
                break
            limit_i = (limit >> i) & 1
            val_i = (val >> i) & 1
            if limit_i:
                if val_i in node:  # val_i ^ node[val_i] == 0, so less than limit
                    res += node[val_i]['cnt']
                node = node.get(1 ^ val_i, None)  # val_i ^ node[val_i] == 1, same than limit
            else:
                node = node.get(val_i, None)  # val_i ^ node[val_i] == 0, same than limit
        return res


class Solution:
    def countPairs(self, nums: List[int], low: int, high: int) -> int:

        trie = Trie()
        res = 0
        for num in nums:
            res += trie.query(num, high + 1) - trie.query(num, low)
            trie.insert(num)
        # print(trie)
        return res


S = Solution()
nums = [1,4,2,7]
low = 2
high = 6
print(S.countPairs(nums, low, high))
nums = [9,8,4,2,1]
low = 5
high = 14
print(S.countPairs(nums, low, high))
