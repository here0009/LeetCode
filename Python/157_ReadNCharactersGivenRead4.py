"""
Given a file and assume that you can only read the file using a given method read4, implement a method to read n characters.

 

Method read4:

The API read4 reads 4 consecutive characters from the file, then writes those characters into the buffer array buf.

The return value is the number of actual characters read.

Note that read4() has its own file pointer, much like FILE *fp in C.

Definition of read4:

    Parameter:  char[] buf4
    Returns:    int

Note: buf4[] is destination not source, the results from read4 will be copied to buf4[]
Below is a high level example of how read4 works:



File file("abcde"); // File is "abcde", initially file pointer (fp) points to 'a'
char[] buf4 = new char[4]; // Create buffer with enough space to store characters
read4(buf4); // read4 returns 4. Now buf = "abcd", fp points to 'e'
read4(buf4); // read4 returns 1. Now buf = "e", fp points to end of file
read4(buf4); // read4 returns 0. Now buf = "", fp points to end of file
 

Method read:

By using the read4 method, implement the method read that reads n characters from the file and store it in the buffer array buf. Consider that you cannot manipulate the file directly.

The return value is the number of actual characters read.

Definition of read:

    Parameters: char[] buf, int n
    Returns:    int

Note: buf[] is destination not source, you will need to write the results to buf[]
 

Example 1:

Input: file = "abc", n = 4
Output: 3
Explanation: After calling your read method, buf should contain "abc". We read a total of 3 characters from the file, so return 3. Note that "abc" is the file's content, not buf. buf is the destination buffer that you will have to write the results to.
Example 2:

Input: file = "abcde", n = 5
Output: 5
Explanation: After calling your read method, buf should contain "abcde". We read a total of 5 characters from the file, so return 5.
Example 3:

Input: file = "abcdABCD1234", n = 12
Output: 12
Explanation: After calling your read method, buf should contain "abcdABCD1234". We read a total of 12 characters from the file, so return 12.
Example 4:

Input: file = "leetcode", n = 5
Output: 5
Explanation: After calling your read method, buf should contain "leetc". We read a total of 5 characters from the file, so return 5.
 

Note:

Consider that you cannot manipulate the file directly, the file is only accesible for read4 but not for read.
The read function will only be called once for each test case.
You may assume the destination buffer array, buf, is guaranteed to have enough space for storing n characters.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/read-n-characters-given-read4
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
"""
The read4 API is already defined for you.

    @param buf, a list of characters
    @return an integer
    def read4(buf):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf = [' '] * 4 # Create buffer with enough space to store characters
read4(buf) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""

class Solution:
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        count, remain = 0, n
        while True:
            tmp = ['']*4
            len_b = read4(tmp)
            for i in range(min(len_b, remain)): 
                buf[count] = tmp[i] # we can not use append or extend to assign values to buffer, probably does not work of this API
                count += 1
            remain -= len_b
            if len_b < 4 or remain <= 0: #read at the end of the input or alreay read n letters
                return count