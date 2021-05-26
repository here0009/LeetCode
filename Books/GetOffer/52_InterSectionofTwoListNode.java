/* -----------------------------------
 *  WARNING:
 * -----------------------------------
 *  Your code may fail to compile
 *  because it contains public class
 *  declarations.
 *  To fix this, please remove the
 *  "public" keyword from your class
 *  declarations.
 */

/**
 * Definition for singly-linked list. 
 */

import java.io.IOException;
import java.util.Set;
import java.util.HashSet;

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

    public static ListNode stringToListNode(String input) {
        // Generate array from the input
        int[] nodeValues = stringToIntegerArray(input);

        // Now convert that list into linked list
        ListNode dummyRoot = new ListNode(0);
        ListNode ptr = dummyRoot;
        for (int item : nodeValues) {
            ptr.next = new ListNode(item);
            ptr = ptr.next;
        }
        return dummyRoot.next;
    }

    public static String listNodeToString(ListNode node) {
        if (node == null) {
            return "[]";
        }

        String result = "";
        while (node != null) {
            result += Integer.toString(node.val) + ", ";
            node = node.next;
        }
        return "[" + result.substring(0, result.length() - 2) + "]";
    }

    public static void main(String[] args) throws IOException {

        String line;
        int intersectVal = 8;
        line = "[4,1,8,4,5]";
        ListNode listA = stringToListNode(line);
        line = "[5,0,1,8,4,5]";
        ListNode listB = stringToListNode(line);
        int skipA = 2;
        int skipB = 3;
        ListNode ret = new Solution().getIntersectionNode(intersectVal, listA, listB, skipA, skipB);
        String out = listNodeToString(ret);
        System.out.print(out);

    }
}


public class ListNode {
    int val;
    ListNode next;
    ListNode(int x) {
        val = x;
        next = null;
    }
}

public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        Set<ListNode> visited = new HashSet<>();;
        ListNode dummy = headA;
        while (dummy != null){
            visited.add(dummy);
            dummy = dummy.next;
        }
        dummy = headB;
        while (dummy != null){
            if (visited.contains(dummy)){
                return dummy;
            }
            dummy = dummy.next;
        }
        return null;
    }
}

public class Solution{
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        ListNode nodeA = headA;
        ListNode nodeB = headB;
        while (nodeA != nodeB){
            nodeA = nodeA != null ? nodeA.next : headB;
            nodeB = nodeB != null ? nodeB.next : headA;
        }
        return nodeA;

    }
}

// 作者：sdwwld
// 链接：https:// leetcode-cn.com/problems/liang-ge-lian-biao-de-di-yi-ge-gong-gong-jie-dian-lcof/solution/ji-he-shuang-zhi-zhen-deng-3chong-jie-jue-fang-shi/
// 来源：力扣（LeetCode）著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处
// 。