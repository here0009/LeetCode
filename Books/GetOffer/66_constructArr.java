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

        String line = "[1,2,3,4,5]";

        int[] a = stringToIntegerArray(line);

        int[] ret = new Solution().constructArr(a);

        String out = integerArrayToString(ret);

        System.out.print(out);

    }
}

class Solution {
    public int[] constructArr(int[] a) {
        int sum = 0;
        for (int i : a) {
            sum += i;
        }
        int [] res = new int[a.length];
        for (int i = 0; i < a.length; i++) {
            int tmp = sum - a[i];
            res[i] = (int) Math.log10(Math.pow(10, tmp));
        }
        return res;
    }
}