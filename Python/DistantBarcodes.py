"""
In a warehouse, there is a row of barcodes, where the i-th barcode is barcodes[i].

Rearrange the barcodes so that no two adjacent barcodes are equal.  You may return any answer, and it is guaranteed an answer exists.

 

Example 1:

Input: [1,1,1,2,2,2]
Output: [2,1,2,1,2,1]
Example 2:

Input: [1,1,1,1,2,2,3,3]
Output: [1,3,1,3,2,1,2,1]
 

Note:

1 <= barcodes.length <= 10000
1 <= barcodes[i] <= 10000
"""
from collections import Counter
class Solution:
    def rearrangeBarcodes(self, barcodes):
        b_counter = Counter(barcodes)
        # print(b_counter)
        res = len(barcodes)*[0]
        b_counter_list = sorted(b_counter.keys(), key = lambda x : b_counter[x], reverse = True)
        # print(b_counter_list)
        index = 0
        for i in range(0,len(res),2):
            if b_counter[b_counter_list[index]] == 0:
                index += 1
            res[i] = b_counter_list[index]
            b_counter[b_counter_list[index]] -= 1

        for i in range(1,len(res),2):
            if b_counter[b_counter_list[index]] == 0:
                index += 1
            res[i] = b_counter_list[index]
            b_counter[b_counter_list[index]] -= 1
        return res


from collections import Counter
class Solution:
    def rearrangeBarcodes(self, barcodes):
        len_b = len(barcodes)
        b_counter = Counter(barcodes).most_common()
        # print(b_counter)
        res = [0]*len_b
        index = 0
        for key, value in b_counter:
            for _ in range(value):
                res[index] = key
                index += 2
                if index >= len_b:
                    index = 1
        return res

s = Solution()
barcodes = [1,1,1,2,2,2]
print(s.rearrangeBarcodes(barcodes))

barcodes = [1,1,1,1,2,2,3,3]
print(s.rearrangeBarcodes(barcodes))

barcodes = [1]
print(s.rearrangeBarcodes(barcodes))

