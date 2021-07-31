import java.io.IOException;

public class MainClass {
    public static void main(String[] args) throws IOException {
    int n = 10;

    int ret = new Solution().cuttingRope(n);

    String out = String.valueOf(ret);

    System.out.print(out);
    }

}

class Solution {
    public int cuttingRope(int n) {
        if (n < 4) return n - 1;
        int d = n / 3;
        int rmd = n % 3;
        if (rmd == 1){
            rmd += 3;
            d -= 1;
        }
        int res = (int) Math.pow(3, d);
        if (rmd > 0) res = res * rmd;
        return res;
    }
}

class Solution {
    public int cuttingRope(int n) {
        if(n <= 3) return n - 1;
        int a = n / 3, b = n % 3;
        if(b == 0) return (int)Math.pow(3, a);
        if(b == 1) return (int)Math.pow(3, a - 1) * 4;
        return (int)Math.pow(3, a) * 2;
    }
}
