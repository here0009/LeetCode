"""
You are given a binary string binary consisting of only 0's or 1's. You can apply each of the following operations any number of times:

Operation 1: If the number contains the substring "00", you can replace it with "10".
For example, "00010" -> "10010"
Operation 2: If the number contains the substring "10", you can replace it with "01".
For example, "00010" -> "00001"
Return the maximum binary string you can obtain after any number of operations. Binary string x is greater than binary string y if x's decimal representation is greater than y's decimal representation.

 

Example 1:

Input: binary = "000110"
Output: "111011"
Explanation: A valid transformation sequence can be:
"000110" -> "000101" 
"000101" -> "100101" 
"100101" -> "110101" 
"110101" -> "110011" 
"110011" -> "111011"
Example 2:

Input: binary = "01"
Output: "01"
Explanation: "01" cannot be transformed any further.
 

Constraints:

1 <= binary.length <= 105
binary consist of '0' and '1'.
"""


class Solution:
    def maximumBinaryString(self, binary: str) -> str:
        """
        Thoughts: the value of s[i] will only influenced by the value of s[i + 1]
        we can keep the max 0 + s[i + 2] and max 1 + s[i + 2]
        """
        def dp(index):
            print(index, binary[:index])
            if index == len_b - 2:
                if binary[index:] == '00':
                    return '00', '10'
                elif binary[index:] == '10':
                    return '01', '10'
                # return '', ''
            zero, one = dp(index + 1)
            if binary[index] == '0':
                return '0' + one, '10' + zero[1:]
            elif binary[index] == '1':
                return '01' + zero[1:], '1' + one

        len_b = len(binary)
        right = binary.rfind('0')
        rmd = binary[right + 1:]
        binary = binary[:right + 1]
        print(binary)
        print(dp(0))

class Solution:
    def maximumBinaryString(self, binary: str) -> str:
        nums = list(binary)
        length = len(nums)
        for i in range(length - 1, 1, -1):
            if nums[i - 1] == '1' and nums[i] == '0':
                nums[i - 1], nums[i] = nums[i], nums[i - 1]
        print(''.join(nums))
        for i in range(length - 1):
            if nums[i] == '0' and nums[i + 1] == '0':
                nums[i] = '1'
        return ''.join(nums)


class Solution:
    def maximumBinaryString(self, binary: str) -> str:
        """
        because 10 -> 01, we can always move 0s to the left
        because 00 -> 10, we can always change 1st 0 to 1, so we move as many zero to the left as we can after the leading '11111's
        unless there is only one zero, then we return the binary itself
        """
        pre_ones = 0
        while pre_ones < len(binary) and binary[pre_ones] == '1':
            pre_ones += 1

        zeros, ones = 0, 0
        for b in binary[pre_ones:]:
            if b == '0':
                zeros += 1
            else:
                ones += 1
        if zeros > 1:
            return (pre_ones + zeros - 1) * '1' + '0' + ones * '1'
        else:
            return binary


S = Solution()
binary = "000110"
print(S.maximumBinaryString(binary))
binary = "01"
print(S.maximumBinaryString(binary))
binary = "01111001100000110010"
print(S.maximumBinaryString(binary))
# Output:
# "10111110111111011101"
# Expected:
# "11111111110111111111"
print(S.maximumBinaryString('11'))
binary ="101010111011001101000110010001100001111"
# Output:
# "111111111111111111011111111111111111111"
# Expected:
# "111111111111111111101111111111111111111"
print(S.maximumBinaryString(binary))
111111111111111111101111111111111111111