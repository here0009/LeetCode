/*
Given a string s and a character letter, return the percentage of characters in s that equal letter rounded down to the nearest whole percent.

 

Example 1:

Input: s = "foobar", letter = "o"
Output: 33
Explanation:
The percentage of characters in s that equal the letter 'o' is 2 / 6 * 100% = 33% when rounded down, so we return 33.
Example 2:

Input: s = "jjjj", letter = "k"
Output: 0
Explanation:
The percentage of characters in s that equal the letter 'k' is 0%, so we return 0.
 

Constraints:

1 <= s.length <= 100
s consists of lowercase English letters.
letter is a lowercase English letter.
 */
#include <ranges>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <unordered_map>
#include <unordered_set>
using namespace std;


class Solution_1 {
 public:
  int percentageLetter(string s, char letter) {
    int counts = 0;
    for (auto c : s) {
      if (c == letter) {
        counts += 1;
      }
    }
    int res = counts * 100 / s.size();
    return res;
  }
};

class Solution {
 public:
  int percentageLetter(string s, char letter) {
    return ranges::count(s, letter) * 100 / s.size();
  }
};

int main() {
  Solution sol;
  cout << sol.percentageLetter("foobar", 'o') << endl;
  cout << sol.percentageLetter("jjjj", 'k') << endl;
}