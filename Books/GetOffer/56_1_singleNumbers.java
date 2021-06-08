import java.io.IOException;

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

    public static String integerArrayToString(int[] nums, int length) {
        if (length == 0) {
            return "[]";
        }

        String result = "";
        for (int index = 0; index < length; index++) {
            int number = nums[index];
            result += Integer.toString(number) + ", ";
        }
        return "[" + result.substring(0, result.length() - 2) + "]";
    }

    public static String integerArrayToString(int[] nums) {
        return integerArrayToString(nums, nums.length);
    }

    public static void main(String[] args) throws IOException {

        String line = "[1,2,10,4,1,4,3,3]";

        int[] nums = stringToIntegerArray(line);

        int[] ret = new Solution().singleNumbers(nums);

        String out = integerArrayToString(ret);

        System.out.print(out);

    }
}


class Solution {
    public int[] singleNumbers(int[] nums) {
        int x = 0;
        for (int i = 0; i < nums.length; i++) x ^= nums[i];
        int div = 1;
        while ((div & x) == 0) div <<= 1;
        int a = 0;
        int b = 0;
        for (int i = 0; i < nums.length; i++){
            if ((nums[i] & div) == 0) a = a ^ nums[i];
            else b = b ^ nums[i];

        }
        return new int [] {a, b};
    }
}