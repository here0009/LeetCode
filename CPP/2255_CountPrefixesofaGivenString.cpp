/*
You are given a string array words and a string s, where words[i] and s comprise only of lowercase English letters.

Return the number of strings in words that are a prefix of s.

A prefix of a string is a substring that occurs at the beginning of the string. A substring is a contiguous sequence of characters within a string.

 

Example 1:

Input: words = ["a","b","c","ab","bc","abc"], s = "abc"
Output: 3
Explanation:
The strings in words which are a prefix of s = "abc" are:
"a", "ab", and "abc".
Thus the number of strings in words which are a prefix of s is 3.
Example 2:

Input: words = ["a","a"], s = "aa"
Output: 2
Explanation:
Both of the strings are a prefix of s. 
Note that the same string can occur multiple times in words, and it should be counted each time.
 

Constraints:

1 <= words.length <= 1000
1 <= words[i].length, s.length <= 10
words[i] and s consist of lowercase English letters only.
 */

#include <iostream>
#include <string>
#include <vector>
using namespace std;

class Solution {
 public:
    int countPrefixes(const vector<string>& words, string s) {
      int res = 0;
      for (auto word : words) {
        if (s.substr(0, word.size()) == word) {
          res += 1;
        }
      }
      return res;
    }
};

int main() {
  Solution sol;
  vector<string> words = {"a", "b", "c", "ab", "bc", "abc"};
  string s = "abc";
  cout << sol.countPrefixes(words, s) << endl;   // Output: 3
  vector<string> words2 = {"a", "a"};
  string s2 = "aa";
  cout << sol.countPrefixes(words2, s2) << endl;   // Output: 2
}