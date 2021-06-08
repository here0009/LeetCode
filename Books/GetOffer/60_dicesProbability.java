import java.io.IOException;
import java.util.Arrays;
public class MainClass {
    public static String doubleArrayToString(double[] input) {
        JsonArray jsonArray = JsonArray.readFrom(input);
        double[] arr = new double[jsonArray.size()];
        for (int i = 0; i < arr.length; i++) {
            arr[i] = jsonArray.get(i).asDouble();
        }
        return arr;
    }

    public static void main(String[] args) throws IOException {

        int n = 2;
        double[] ret = new Solution().dicesProbability(n);
        String out = doubleArrayToString(ret);
        System.out.print(out);

    }
}

class Solution {
    public double[] dicesProbability(int n) {
        double [][] dp = new double [n + 1][6 * n + 1];
        for (int j = 1; j <= 6; j++){
            dp[1][j] = (double) 1/6;
        }
        for (int i = 2; i <= n; i++){
            for (int j = i; j <= i * 6; j++){
                for (int k = 1; k < j; k++){
                    dp[i][j] += dp[1][k] * dp[i - 1][j - k];
                }
            }
        }
        return Arrays.copyOfRange(dp[n], n, 6*n + 1);
    }
}

class Solution {
    public double[] dicesProbability(int n) {
        double[][] dp = new double[n + 1][6 * n + 1];
        for (int i = 1; i <= 6; i++) {
            dp[1][i] = (double) 1 / 6;
        }
        for (int i = 2; i <= n; i++) {
            for (int j = i; j <= 6 * i; j++) {
                for (int k = 1; k <= 6; k++) {
                    if (j - k < 1) {
                        continue;
                    }
                    dp[i][j] += dp[1][k] * dp[i - 1][j - k];
                }
            }
        }
        return Arrays.copyOfRange(dp[n], n, 6 * n + 1);
    }
}


class Solution {
    public double[] dicesProbability(int n) {
        double[][] dp = new double[n + 1][6 * n + 1];
        for (int i = 1; i <= 6; i++) {
            dp[1][i] = (double) 1 / 6;
        }
        for (int i = 2; i <= n; i++) {
            for (int j = i; j <= 6 * i; j++) {
                for (int k = 1; k <= 6; k++) {
                    if (j <= k) {
                        break;
                    }
                    dp[i][j] += dp[1][k] * dp[i - 1][j - k];
                }
            }
        }
        double[] res = new double[5 * n + 1];
        int id = n;
        for (int i = 0; i < res.length; i++) {
            res[i] = dp[n][id++];
        }
        return res;
    }
}

// 作者：da-shi-shuo
// 链接：https://leetcode-cn.com/problems/nge-tou-zi-de-dian-shu-lcof/solution/dong-tai-gui-hua-gai-lu-java-by-da-shi-s-mqgv/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

class Solution {
    public double[] dicesProbability(int n) {
        double[][] dp = new double[n + 1][6 * n + 1];
        for (int i = 1; i <= 6; i++) {
            dp[1][i] = (double) 1 / 6;
        }
        for (int i = 2; i <= n; i++) {
            for (int j = i; j <= 6 * i; j++) {
                for (int k = 1; k < 6; k++) {
                    if (j <= k) {
                        break;
                    }
                    dp[i][j] += dp[1][k] * dp[i - 1][j - k];
                }
            }
        }
        return Arrays.copyOfRange(dp[n], n, 6 * n + 1);
    }
}