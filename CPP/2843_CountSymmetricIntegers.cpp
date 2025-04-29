/*
You are given two positive integers low and high.

An integer x consisting of 2 * n digits is symmetric if the sum of the first n digits of x is equal to the sum of the last n digits of x. Numbers with an odd number of digits are never symmetric.

Return the number of symmetric integers in the range [low, high].

 

Example 1:

Input: low = 1, high = 100
Output: 9
Explanation: There are 9 symmetric integers between 1 and 100: 11, 22, 33, 44, 55, 66, 77, 88, and 99.
Example 2:

Input: low = 1200, high = 1230
Output: 4
Explanation: There are 4 symmetric integers between 1200 and 1230: 1203, 1212, 1221, and 1230.
 

Constraints:

1 <= low <= high <= 104
 */
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <unordered_map>
#include <unordered_set>
using namespace std;

class Solution {
 public:
  bool checkSymmetirc(int num) {
    string s = to_string(num);
    if (s.size() % 2 == 1) {
      return false;
    }
    int low = 0, high = 0;
    int half_size = s.size() / 2;
    for (int i = 0; i < s.size(); i++) {
      if (i < half_size) {
        low += s[i] - '0';
      } else {
        high += s[i] - '0';
      }
    }
    return low == high;
  }
  int countSymmetricIntegers(int low, int high) {
    int res = 0;
    for (int num = low; num < high + 1; num++) {
      if (checkSymmetirc(num)) {
        res += 1;
      }
    }
    return res;
  }
};


int main() {
  Solution sol;
  cout << sol.countSymmetricIntegers(1, 100) << endl;
  cout << sol.countSymmetricIntegers(1200, 1230) << endl;
}