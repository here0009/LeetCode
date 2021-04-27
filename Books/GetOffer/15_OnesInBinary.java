public class Solution {
    // you need to treat n as an unsigned value
    public static void main(String[] args) {
        System.out.println(hammingWeight(3)); 
        System.out.println(hammingWeight(1));
        System.out.println(hammingWeight(31));
    }

    public static int hammingWeight(int n) {
        int res = 0;
        // we should use n != 0 rather than n > 0 since n can be negatives
        while (n != 0) {  
            res += n & 1;
            n >>>= 1;  // >>> is unsinged bitwise operations
        }
        return res;
    }
}