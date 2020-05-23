#include<math.h>
class Solution {
public:
    int sumSubseqWidths(vector<int>& A) {
        int large_num, ans
        large_num = power(10,9)+7
        ans = 0
        if A.size() == 1:
            return ans
        sorted(A.begin(), A.end(), less)
        // # print(A)
        for (int i = 0; i < A.size()-1; i++):
            for (int j = i+1; j < A.size(); j++):
                ans += power(2, j-i-1)*(A[j]-A[i])
        return ans % large_num
    }
};