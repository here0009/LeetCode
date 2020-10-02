"""
Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

Machine 1 (sender) has the function:

string encode(vector<string> strs) {
  // ... your code
  return encoded_string;
}
Machine 2 (receiver) has the function:
vector<string> decode(string s) {
  //... your code
  return strs;
}
So Machine 1 does:

string encoded_string = encode(strs);
and Machine 2 does:

vector<string> strs2 = decode(encoded_string);
strs2 in Machine 2 should be the same as strs in Machine 1.

Implement the encode and decode methods.

 

Note:

The string may contain any possible characters out of 256 valid ascii characters. Your algorithm should be generalized enough to work on any possible characters.
Do not use class member/global/static variables to store states. Your encode and decode algorithms should be stateless.
Do not rely on any library method such as eval or serialize methods. You should implement your own encode/decode algorithm.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/encode-and-decode-strings
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


from random import randint
class Codec:


    def encode(self, string):
        """Encodes a list of strings to a single string.
        """
        
        

    def decode(self, string):
        """Decodes a single string to a list of strings.
        """
        return 
        

class Codec:
    def __init__(self):
        self.M = 256 # the length of ascii characters
        self.rand = randint(1, 255)

    def encode(self, strs: [str]) -> str:
        """Encodes a list of strings to a single string.
        """
        if len(strs) == 0:
            return chr(258)
        res = []
        for string in strs:
            res.append(''.join((chr((ord(k) - self.rand)%self.M)) for k in string))
        return chr(257).join(res)

    def decode(self, s: str) -> [str]:
        """Decodes a single string to a list of strings.
        """
        if s == chr(258):
            return []
        lst = s.split(chr(257))
        res = []
        for string in lst:
            res.append(''.join((chr((ord(k) + self.rand)%self.M)) for k in string))
        return res
     
# 作者：LeetCode
# 链接：https://leetcode-cn.com/problems/encode-and-decode-strings/solution/zi-fu-chuan-de-bian-ma-yu-jie-ma-by-leetcode/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

class Codec:
    def len_to_str(self, x):
        """
        Encodes length of string to bytes string
        """
        x = len(x)
        bytes = [chr(x >> (i * 8) & 0xff) for i in range(4)]
        bytes.reverse()
        bytes_str = ''.join(bytes)
        return bytes_str
    
    def encode(self, strs):
        """Encodes a list of strings to a single string.
        :type strs: List[str]
        :rtype: str
        """
        # encode here is a workaround to fix BE CodecDriver error
        return ''.join(self.len_to_str(x) + x for x in strs)
        
    def str_to_int(self, bytes_str):
        """
        Decodes bytes string to integer.
        """
        result = 0
        for ch in bytes_str:
            result = result * 256 + ord(ch)
        return result
    
    def decode(self, s):
        """Decodes a single string to a list of strings.
        :type s: str
        :rtype: List[str]
        """
        i, n = 0, len(s)
        output = []
        while i < n:
            length = self.str_to_int(s[i: i + 4])
            i += 4
            output.append(s[i: i + length])
            i += length
        return output



# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
# Your Codec object will be instantiated and called as such:
codec = Codec()
strs = ['abc', 'sdfefd', '213124hk']
print(strs)
ecd = codec.encode(strs)
print(ecd)
print(codec.decode(ecd))