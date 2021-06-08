import java.io.IOException;

public class MainClass {
    public static void main(String[] args) throws IOException {

            int n = 6;

            int ret = new Solution().sumNums(n);

            String out = String.valueOf(ret);

            System.out.print(out);

    }
}

class Solution {
    public int sumNums(int n) {
        boolean x = n > 1 && (n += sumNums(n - 1)) > 0;
        return n;
    }
}