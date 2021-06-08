import java.io.IOException;
import java.util.HashMap;
import java.util.Map;
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

        String line = "[9,1,7,9,7,9,7]";

        int[] nums = stringToIntegerArray(line);

        int ret = new Solution().singleNumber(nums);

        String out = String.valueOf(ret);

        System.out.print(out);

    }
}

class Solution {
    public int singleNumber(int[] nums) {
        Map <Integer, Integer> dict = new HashMap <Integer, Integer>();
        for (int i : nums) {
            int tmp = dict.containsKey(i) ? dict.get(i) : 0;
            dict.put(i, tmp + 1);
        }
        for (int i : dict.keySet()) {
            if (dict.get(i) == 1) return i;
        }
        return -1;
    }
}