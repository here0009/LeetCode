import java.io.IOException;
import java.util.Arrays;

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

    public static String booleanToString(boolean input) {
        return input ? "True" : "False";
    }

    public static void main(String[] args) throws IOException {

        String line = "[4, 8, 6, 12, 16, 14, 10]";

        int[] postorder = stringToIntegerArray(line);

        boolean ret = new Solution().verifyPostorder(postorder);

        String out = booleanToString(ret);

        System.out.print(out);

    }
}

class Solution {
    public boolean verifyPostorder(int[] postorder) {
        return recur(postorder, 0, postorder.length);

    }
    private boolean  recur(int [] postorder, int left, int right){
        if (left >= right) return true;
        int val = postorder[right - 1];
        int mid = left;
        while (mid < right && postorder[mid] < val) mid++;
        int j = mid;
        while (j < right && postorder[j] > val) j++;
        return j == right - 1 && recur(postorder, left, mid) && recur(postorder, mid, right - 1);
    }
}

class Solution {
    public boolean verifyPostorder(int[] postorder) {
        int length = postorder.length;
        if (length <= 1)
            return true;
        int root_val = postorder[length - 1];
        int left = 0;
        while (left < length && postorder[left] < root_val)
            left += 1;
        int right = left;
        while (right < length && postorder[right] > root_val)
            right += 1;
        return right == length - 1 && verifyPostorder(Arrays.copyOfRange(postorder, 0, left))
                && verifyPostorder(Arrays.copyOfRange(postorder, left, length - 1));
    }
}


