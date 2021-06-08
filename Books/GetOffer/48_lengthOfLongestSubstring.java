import java.io.IOException;
import java.util.HashMap;


public class MainClass {
    public static String stringToString(String input) {
        if (input == null) {
            return "null";
        }
        return Json.value(input).toString();
    }

    public static void main(String[] args) throws IOException {

        String line;

        String s = stringToString(line);

        int ret = new Solution().lengthOfLongestSubstring(s);

        String out = String.valueOf(ret);

        System.out.print(out);

    }
}

class Solution {
    public int lengthOfLongestSubstring(String s) {
        HashMap<Character, Integer> map = new HashMap<>();
        int left = -1, res = 0;
        for (int i = 0; i < s.length(); i++){
            char tmp = s.charAt(i);
            if (map.containsKey(tmp)) left = Math.max(left, map.get(tmp));
            map.put(tmp, i);
            res = Math.max(res, i - left);
        }
        return res;

    }
}