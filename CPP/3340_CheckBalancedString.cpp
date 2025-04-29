/*
You are given a string num consisting of only digits. A string of digits is called balanced if the sum of the digits at even indices is equal to the sum of digits at odd indices.

Return true if num is balanced, otherwise return false.

 

Example 1:

Input: num = "1234"

Output: false

Explanation:

The sum of digits at even indices is 1 + 3 == 4, and the sum of digits at odd indices is 2 + 4 == 6.
Since 4 is not equal to 6, num is not balanced.
Example 2:

Input: num = "24123"

Output: true

Explanation:

The sum of digits at even indices is 2 + 1 + 3 == 6, and the sum of digits at odd indices is 4 + 2 == 6.
Since both are equal the num is balanced.
 

Constraints:

2 <= num.length <= 100
num consists of digits only
 */
#include <iostream>
#include <string>
// using namespace std;

class Solution {
 public:
  bool isBalanced(std::string num) {
    int odd_sum = 0;
    int even_sum = 0;
    for (int i = 0; i < num.length(); ++i) {
      if (i % 2 == 0) {
        even_sum += num[i] - '0';
      } else {
        odd_sum += num[i] - '0';
      }
    }
    return even_sum == odd_sum;
  }
};

int main() {
  Solution sol;
  std::cout << sol.isBalanced("1234") << std::endl;   // Output: 0 (false)
  std::cout << sol.isBalanced("24123") << std::endl;  // Output: 1 (true)
  return 0;
}

