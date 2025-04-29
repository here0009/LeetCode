/*
You are given a 0-indexed two-dimensional integer array nums.

Return the largest prime number that lies on at least one of the diagonals of nums. In case, no prime is present on any of the diagonals, return 0.

Note that:

An integer is prime if it is greater than 1 and has no positive integer divisors other than 1 and itself.
An integer val is on one of the diagonals of nums if there exists an integer i for which nums[i][i] = val or an i for which nums[i][nums.length - i - 1] = val.


In the above diagram, one diagonal is [1,5,9] and another diagonal is [3,5,7].

 

Example 1:

Input: nums = [[1,2,3],[5,6,7],[9,10,11]]
Output: 11
Explanation: The numbers 1, 3, 6, 9, and 11 are the only numbers present on at least one of the diagonals. Since 11 is the largest prime, we return 11.
Example 2:

Input: nums = [[1,2,3],[5,17,7],[9,11,10]]
Output: 17
Explanation: The numbers 1, 3, 9, 10, and 17 are all present on at least one of the diagonals. 17 is the largest prime, so we return 17.
 

Constraints:

1 <= nums.length <= 300
nums.length == numsi.length
1 <= nums[i][j] <= 4*106
 */
#include <iostream>
#include <string>
#include <cmath>
#include <vector>
using namespace std;

class Solution {
 public:
  bool isPrime(int value) {
    if (value <= 1) {
      return false;
    }
    int factor = 2;
    while (factor * factor <= value) {
      if (value % factor == 0) {
        return false;
      }
      factor++;
    }
    return true;
  }

  int diagonalPrime(const vector<vector<int>>& nums) {
    int length = nums.size(), res = 0;
    for (int i = 0; i < length; i++) {
      if (nums[i][i] > res && isPrime(nums[i][i])) {
        res = nums[i][i];
      }
      if (nums[i][length - 1 - i] > res && isPrime(nums[i][length - 1 - i])) {
        res = nums[i][length - 1 - i];
      }
    }
    return res;
  }
};

int main() {
  Solution sol;
  vector<vector<int>> nums1 = {{1, 2, 3}, {5, 6, 7}, {9, 10, 11}};
  cout << "Largest prime in diagonals: " << sol.diagonalPrime(nums1) << endl;  // Output: 11

  vector<vector<int>> nums2 = {{1, 2, 3}, {5, 17, 7}, {9, 11, 10}};
  cout << "Largest prime in diagonals: " << sol.diagonalPrime(nums2) << endl;  // Output: 17

  vector<vector<int>> nums3 = {{4, 6, 8}, {10, 12, 14}, {16, 18, 20}};
  cout << "Largest prime in diagonals: " << sol.diagonalPrime(nums3) << endl;  // Output: 0 (no primes)
}
