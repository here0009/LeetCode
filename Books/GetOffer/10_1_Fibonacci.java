
class Solution {

    public static void main(String[] args) {
        for (int i = 1; i < 10 ; i ++) {
            // System.out.println("%,d", fib(i));
            System.out.println(fib(i));

        }
            
    }
    public static int fib(int n) {
        int a = 0, b = 1, sum;
        for(int i = 0; i < n; i++){
            sum = (a + b) % 1000000007;
            a = b;
            b = sum;
        }
        return a;
    }
}
