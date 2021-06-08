import java.util.Deque;
import java.util.LinkedList;
import java.util.Queue;

public class MainClass {
    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        String line;
        while ((line = in.readLine()) != null) {
            int m = Integer.parseInt(line);
            line = in.readLine();
            int n = Integer.parseInt(line);
            line = in.readLine();
            int k = Integer.parseInt(line);

            int ret = new Solution().movingCount(m, n, k);

            String out = String.valueOf(ret);

            System.out.print(out);
        }
    }
}


class Solution {
    public int movingCount(int m, int n, int k) {
        int res = 0;
        boolean [][] visited = new boolean [m][n];
        Queue<int []> queue =new LinkedList<int []>();
        queue.add(new int[] {0, 0});
        while (queue.size() > 0){
            int [] idx = queue.poll();
            int i = idx[0], j = idx[1];
            if ( i >= m || j >= n || visited[i][j] || (calc(i) + calc(j) > k)) continue;
            visited[i][j] = true;
            res++;
            queue.add(new int[] {i + 1, j});
            queue.add(new int[] { i, j + 1 });
        }

        return res;
    }
    private int calc(int num){
        int res = 0;
        while (num > 0){
            res += num % 10;
            num = num / 10;
        }
        return res;
    }
}