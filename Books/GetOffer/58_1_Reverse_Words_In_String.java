import java.io.IOException;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class MainClass {

    public static void main(String[] args) throws IOException {

        String line = "  hello world!  ";

        String ret = new Solution().reverseWords(line);

        String out = (ret);

        System.out.print(out);
    }
}

class Solution {
    public String reverseWords(String s) {

        List<String> lst = Arrays.asList(s.trim().split("\\s+"));
        Collections.reverse(lst);
        return String.join(" ", lst);
    }
}