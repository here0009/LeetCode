import java.util.ArrayList;
import java.util.Deque;
import java.util.LinkedList;
import java.util.List;

public class MainClass {
    public static int[] stringToIntegerArray(String input) {
        input = input.trim();
        input = input.substring(1, input.length() - 1);
        if (input.length() == 0) {
          return new int[0];
        }
    
        String[] parts = input.split(",");
        int[] output = new int[parts.length];
        for(int index = 0; index < parts.length; index++) {
            String part = parts[index].trim();
            output[index] = Integer.parseInt(part);
        }
        return output;
    }
    
    public static String booleanToString(boolean input) {
        return input ? "True" : "False";
    }
    
    public static void main(String[] args) throws IOException {

        String line = "[1,2,3,4,5]";

        int[] pushed = stringToIntegerArray(line);

        line = "[4,5,3,2,1]";

        int[] popped = stringToIntegerArray(line);
        
        boolean ret = new Solution().validateStackSequences(pushed, popped);
        
        String out = booleanToString(ret);
        
        System.out.print(out);

    }
}


class Solution {
    public boolean validateStackSequences(int[] pushed, int[] popped) {
        Deque<Integer> st = new LinkedList<>();
        int idx_pushed = 0;
        int idx_poped = 0;
        int length = pushed.length;
        while (! st.isEmpty() && st.getLast() == popped[idx_poped]){
            idx_poped++;
            st.removeLast();
        }
        while (idx_pushed < length && pushed[idx_pushed] != popped[idx_poped]){
            st.addLast(pushed[idx_pushed++]);
        }
        if (idx_poped == length) return true;
        return false;
    }
}