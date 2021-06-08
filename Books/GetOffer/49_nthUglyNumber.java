import java.util.HashSet;
import java.util.PriorityQueue;
import java.util.Set;
import java.io.IOException;
public class MainClass {
    public static void main(String[] args) throws IOException {


        int n = 10;

        int ret = new Solution().nthUglyNumber(n);

        String out = String.valueOf(ret);

        System.out.print(out);
    }


}

// class Solution {
//     public int nthUglyNumber(int n) {

//         PriorityQueue<Long> pq = new PriorityQueue<>();
//         Set<Long> visited = new HashSet<>();
//         pq.add(1L);
//         visited.add(1L);
//         // long [] factors= new long [] {2,3,5};
//         long[] factors = { 2, 3, 5 };
//         while (n > 1){
//             long num = pq.poll();
//             for (long k : factors) {
//                 long tmp = k * num;
//                 if (! visited.contains(tmp)){
//                     pq.add(tmp);
//                     visited.add(tmp);
//                 }
//             }
//             n -= 1;
//         }
//         long res = pq.poll();
//         return (int) res;

//     }
// }

class Solution {
    public int nthUglyNumber(int n) {
        int [] dp = new int[n + 1];
        dp[1] = 1;
        int p2 = 1, p3 = 1, p5 = 1;
        for (int i = 2; i <= n; i++){
            int num2 = 2 * dp[p2];
            int num3 = 3 * dp[p3];
            int num5 = 5 * dp[p5];
            dp[i] = Math.min(Math.min(num2, num3), num5);
            if (dp[i] == num2) p2++;
            if (dp[i] == num3) p3++;
            if (dp[i] == num5) p5++;
        }
        return dp[n];

    }
}