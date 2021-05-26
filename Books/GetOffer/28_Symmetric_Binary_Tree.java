import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.List;

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
 * Definition for a binary tree node. 
 */


import java.util.Deque;
import java.util.LinkedList;

public class MainClass {
    public static TreeNode stringToTreeNode(String input) {
        input = input.trim();
        input = input.substring(1, input.length() - 1);
        if (input.length() == 0) {
            return null;
        }

        String[] parts = input.split(",");
        String item = parts[0];
        TreeNode root = new TreeNode(Integer.parseInt(item));
        Queue<TreeNode> nodeQueue = new LinkedList<>();
        nodeQueue.add(root);

        int index = 1;
        while (!nodeQueue.isEmpty()) {
            TreeNode node = nodeQueue.remove();

            if (index == parts.length) {
                break;
            }

            item = parts[index++];
            item = item.trim();
            if (!item.equals("null")) {
                int leftNumber = Integer.parseInt(item);
                node.left = new TreeNode(leftNumber);
                nodeQueue.add(node.left);
            }

            if (index == parts.length) {
                break;
            }

            item = parts[index++];
            item = item.trim();
            if (!item.equals("null")) {
                int rightNumber = Integer.parseInt(item);
                node.right = new TreeNode(rightNumber);
                nodeQueue.add(node.right);
            }
        }
        return root;
    }

    public static String booleanToString(boolean input) {
        return input ? "True" : "False";
    }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        String line;
        while ((line = in.readLine()) != null) {
            TreeNode root = stringToTreeNode(line);

            boolean ret = new Solution().isSymmetric(root);

            String out = booleanToString(ret);

            System.out.print(out);
        }
    }
}

public class TreeNode { 
    int val; 
    TreeNode left; 
    TreeNode right; 
    TreeNode(int x) { val = x; } 
}


public class Solution {

    public boolean isSymmetric(TreeNode root) {
        if (root == null) {
            return true;
        }

        // 实现类不能选用 ArrayDeque，因为该类的 add 方法会对添加的元素做非空检查
        Deque<TreeNode> deque = new LinkedList<>();
        // Deque<TreeNode> deque = new ArrayDeque<>();

        deque.addFirst(root.left);
        deque.addLast(root.right);

        while (!deque.isEmpty()) {
            TreeNode leftNode = deque.removeFirst();
            TreeNode rightNode = deque.removeLast();

            if (leftNode == null && rightNode == null) {
                continue;
            }

            if (leftNode == null || rightNode == null) {
                return false;
            }

            if (leftNode.val != rightNode.val) {
                return false;
            }
            deque.addFirst(leftNode.right);
            deque.addFirst(leftNode.left);
            deque.addLast(rightNode.left);
            deque.addLast(rightNode.right);
        }

        return true;
    }
}

// 作者：liweiwei1419 链接：https:// leetcode-cn.com/problems/dui-cheng-de-er-cha-shu-lcof/solution/di-gui-yu-fei-di-gui-xie-fa-shuang-duan-dui-lie-by/
// 来源：力扣（LeetCode）著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

class Solution {
    private boolean dfs(TreeNode L, TreeNode R){
        if (L == null && R == null) return true;
        if (L == null || R == null) return false;
        if (L.val != R.val) return false;
        return dfs(L.left, R.right) && dfs(L.right, R.left);
    }

    public boolean isSymmetric(TreeNode root) {
        if (root == null) return true;
        return dfs(root.left, root.right);
    }
}
