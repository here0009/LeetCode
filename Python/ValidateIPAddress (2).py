"""
Write a function to check whether an input string is a valid IPv4 address or IPv6 address or neither.

IPv4 addresses are canonically represented in dot-decimal notation, which consists of four decimal numbers, each ranging from 0 to 255, separated by dots ("."), e.g.,172.16.254.1;

Besides, leading zeros in the IPv4 is invalid. For example, the address 172.16.254.01 is invalid.

IPv6 addresses are represented as eight groups of four hexadecimal digits, each group representing 16 bits. The groups are separated by colons (":"). For example, the address 2001:0db8:85a3:0000:0000:8a2e:0370:7334 is a valid one. Also, we could omit some leading zeros among four hexadecimal digits and some low-case characters in the address to upper-case ones, so 2001:db8:85a3:0:0:8A2E:0370:7334 is also a valid IPv6 address(Omit leading zeros and using upper cases).

However, we don't replace a consecutive group of zero value with a single empty group using two consecutive colons (::) to pursue simplicity. For example, 2001:0db8:85a3::8A2E:0370:7334 is an invalid IPv6 address.

Besides, extra leading zeros in the IPv6 is also invalid. For example, the address 02001:0db8:85a3:0000:0000:8a2e:0370:7334 is invalid.

Note: You may assume there is no extra space or special characters in the input string.

Example 1:
Input: "172.16.254.1"

Output: "IPv4"

Explanation: This is a valid IPv4 address, return "IPv4".
Example 2:
Input: "2001:0db8:85a3:0:0:8A2E:0370:7334"

Output: "IPv6"

Explanation: This is a valid IPv6 address, return "IPv6".
Example 3:
Input: "256.256.256.256"

Output: "Neither"

Explanation: This is neither a IPv4 address nor a IPv6 address.
"""
class Solution:
    def validIPAddress(self, IP: str) -> str:
        def checkIPv4(IP):
            ip_list = IP.split('.')
            if len(ip_list) != 4:
                return False
            for num in ip_list:
                l_num = len(num)
                try:
                    int_num = int(num)
                except:
                    return False
                if int_num > 255 or int_num < 0:
                    return False
                if (l_num > 1 and int_num < 10) or (l_num > 2 and int_num < 100):
                    return False
            return True

        def checkIPv6(IP):
            ip_list = IP.split(':')
            # print(ip_list)
            if len(ip_list) != 8:
                return False
            for num in ip_list:
                # print(num)
                l_num = len(num)
                if l_num > 4 or l_num == 0:
                    return False
                if not all([k in letters for k in num]):
                    return False
            return True

        letters = set([str(i) for i in range(10)])
        letters |= set(list('ABCDEF'))
        letters |= set(list('abcdef'))

        if '.' in IP and checkIPv4(IP):
            return 'IPv4'
        elif ':' in IP and checkIPv6(IP):
            return 'IPv6'
        return 'Neither'


S = Solution()
# IP = "172.16.254.1"
# print(S.validIPAddress(IP))
# IP = "2001:0db8:85a3:0:0:8A2E:0370:7334"
# print(S.validIPAddress(IP))
# IP = "256.256.256.256"
# print(S.validIPAddress(IP))

IP = "20EE:Fb8:85a3:0:0:8A2E:0370:7334"
print(S.validIPAddress(IP))

IP = "018.16.254.1"
print(S.validIPAddress(IP))