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

        String line = "[-1]";
        int[] nums = stringToIntegerArray(line);
        int ret = new Solution().maxSubArray(nums);

        String out = String.valueOf(ret);

        System.out.print(out);

    }
}


class Solution {
    public int maxSubArray(int[] nums) {
        int pre = nums[0];
        int res = nums[0];
        for (int i = 1; i < nums.length; i += 1){
            pre = Math.max(pre + nums[i], nums[i]);
            res = Math.max(res, pre);
        }
        return res;
    }
}