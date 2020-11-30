"""
A character in UTF8 can be from 1 to 4 bytes long, subjected to the following rules:

For 1-byte character, the first bit is a 0, followed by its unicode code.
For n-bytes character, the first n-bits are all one's, the n+1 bit is 0, followed by n-1 bytes with most significant 2 bits being 10.
This is how the UTF-8 encoding would work:

   Char. number range  |        UTF-8 octet sequence
      (hexadecimal)    |              (binary)
   --------------------+---------------------------------------------
   0000 0000-0000 007F | 0xxxxxxx
   0000 0080-0000 07FF | 110xxxxx 10xxxxxx
   0000 0800-0000 FFFF | 1110xxxx 10xxxxxx 10xxxxxx
   0001 0000-0010 FFFF | 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx
Given an array of integers representing the data, return whether it is a valid utf-8 encoding.

Note:
The input is an array of integers. Only the least significant 8 bits of each integer is used to store the data. This means each integer represents only 1 byte of data.

Example 1:

data = [197, 130, 1], which represents the octet sequence: 11000101 10000010 00000001.

Return true.
It is a valid utf-8 encoding for a 2-bytes character followed by a 1-byte character.
Example 2:

data = [235, 140, 4], which represented the octet sequence: 11101011 10001100 00000100.

Return false.
The first 3 bits are all one's and the 4th bit is 0 means it is a 3-bytes character.
The next byte is a continuation byte which starts with 10 and that's correct.
But the second continuation byte does not start with 10, so it is invalid.
"""


from typing import List
class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        n = 0
        for val in data:
            bin_val = bin(val)[2:]
            if len(bin_val) < 8:
                bin_val = (8 - len(bin_val))*'0' + bin_val
            elif len(bin_val) > 8:
                bin_val = bin_val[-8:]
            if n == 0:
                while n < 8 and bin_val[n] == '1':
                    n += 1
                if n > 4 or n == 1:  # A character in UTF8 can be from 1 to 4 bytes long, there can be multiple character in data
                    return False
                if n > 0:
                    n -= 1
            elif n > 0:
                if bin_val[:2] != '10':
                    return False
                n -= 1
        return n == 0


class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        cnt = 0 
        for x in data:
            x = bin(x)[2:][-8:].zfill(8)
            if cnt: # in the middle of multi-byte 
                if x.startswith("10"): 
                  cnt -= 1
                else: 
                  return False 
            else: # beginning 
                cnt = x.find("0")
                if cnt == -1 or cnt == 1 or cnt > 4: 
                  return False 
                if cnt: 
                  cnt -= 1
        return cnt == 0


class Solution:
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        n_bytes = 0
        mask1 = 1 << 7
        mask2 = 1 << 6
        for num in data:
            mask = 1 << 7
            if n_bytes == 0:
                while mask & num:
                    n_bytes += 1
                    mask = mask >> 1
                if n_bytes == 0:
                    continue
                if n_bytes == 1 or n_bytes > 4:
                    return False
            else:
                if not (num & mask1 and not (num & mask2)):
                    return False
            n_bytes -= 1
        return n_bytes == 0


S = Solution()
data = [197, 130, 1]
print(S.validUtf8(data))
data = [235, 140, 4]
print(S.validUtf8(data))
data = [237]
print(S.validUtf8(data))
data = [145]
print(S.validUtf8(data))
data = [250,145,145,145,145]
print(S.validUtf8(data))
data = [240,162,138,147,17]
print(S.validUtf8(data))