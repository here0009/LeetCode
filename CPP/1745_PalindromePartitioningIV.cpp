/*
Given a string s, return true if it is possible to split the string s into three non-empty palindromic substrings. Otherwise, return false.​​​​​

A string is said to be palindrome if it the same string when reversed.

 

Example 1:

Input: s = "abcbdd"
Output: true
Explanation: "abcbdd" = "a" + "bcb" + "dd", and all three substrings are palindromes.
Example 2:

Input: s = "bcbddxy"
Output: false
Explanation: s cannot be split into 3 palindromes.
 

Constraints:

3 <= s.length <= 2000
s​​​​​​ consists only of lowercase English letters.
*/
#include <iostream>
#include <vector>
using namespace std;


class Solution {
public:
    bool checkPartitioning(string s) {
        int n = s.size();
        vector<vector<bool>> isPalindrome(n, vector<bool>(n));
        for (int length = 1; length < n; length++){
            for (int start = 0; start <= n - length; start++){
                int end = start + length - 1;
                if (length == 1){
                    isPalindrome[start][end] = true;
                }
                else if (length == 2){
                    isPalindrome[start][end] = s[start] == s[end];
                }
                else{
                    isPalindrome[start][end] = s[start] == s[end] && isPalindrome[start + 1][end - 1];
                }
            }
        }
        for (int start = 1; start < n - 1; start++){
            if (!isPalindrome[0][start-1]){
                continue;
            }
            for (int end = start; end < n-1; end++){
                if (isPalindrome[start][end] and isPalindrome[end+1][n-1]){
                    return true;
                }
            }
        }
        return false;
    }
};

int main(){
    Solution s;
    cout << s.checkPartitioning("abcbdd") << endl;
    cout << s.checkPartitioning("bcbddxy") << endl;
};