import java.io.IOException;
import java.lang.Math;

public class MainClass {
    public static int[] stringToIntegerArray(String input) {
        input = input.trim();
        input = input.substring(1, input.length() - 1);
        if (input.length() == 0) {
            return new int[0];
        }

        String[] parts = input.split(",");
        int[] output = new int[parts.length];
        for (int index = 0; index < parts.length; index++) {
            String part = parts[index].trim();
            output[index] = Integer.parseInt(part);
        }
        return output;
    }

    public static void main(String[] args) throws IOException {


            String line = "[7,1,5,3,6,4]";

            int[] prices = stringToIntegerArray(line);

            int ret = new Solution().maxProfit(prices);

            String out = String.valueOf(ret);

            System.out.print(out);

    }
}

class Solution {
    public int maxProfit(int[] prices) {

        if (prices.length == 0) return 0;
        int res = 0;
        int min_price = prices[0];
        for (int i = 1; i < prices.length; i++){
            int price = prices[i];
            if (price <= min_price) min_price = price;
            else res  = Math.max(res, price - min_price);
        }
        return res;
    }
}