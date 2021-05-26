import java.lang.Math;
import java.io.IOException;
public class MainClass {
    public static void main(String[] args) throws IOException {

        int n = 7;
        
        int ret = new Solution().numWays(n);
        
        String out = String.valueOf(ret);
        
        System.out.print(out);

    }
}

class Solution {
    public int numWays(int n) {
        if (n < 2) return n;
        long M = 1000000007;
        long [] dp = new long[n + 1];
        dp[0] = 1;
        dp[1] = 1;
        for (int i = 2; i < dp.length; i++) {
            long tmp = dp[i - 1] + dp[i - 2];
            dp[i] = tmp % M;
        }
        return (int) dp[n];
    }
}

class Solution {
    public int numWays(int n) {
        int a = 1, b = 1, sum;
        for(int i = 0; i < n; i++){
            sum = (a + b) % 1000000007;
            a = b;
            b = sum;
        }
        return a;
    }
}

// 作者：jyd 链接：https:// leetcode-cn.com/problems/qing-wa-tiao-tai-jie-wen-ti-lcof/solution/mian-shi-ti-10-ii-qing-wa-tiao-tai-jie-wen-ti-dong/
// 来源：力扣（LeetCode）著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
