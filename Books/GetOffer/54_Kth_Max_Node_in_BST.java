/*
给定一棵二叉搜索树，请找出其中第k大的节点。

 

示例 1:

输入: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
输出: 4
示例 2:

输入: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
输出: 4
 

限制：

1 ≤ k ≤ 二叉搜索树元素个数

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-di-kda-jie-dian-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
*/
/**
 * Definition for a binary tree node.
  */


public class TreeNode {
      int val;
      TreeNode left;
      TreeNode right;
      TreeNode(int x) { val = x; }
}

class Solution {
    public int kthLargest(TreeNode root, int k) {
        int right = dfs(root.right);
        if (right >= k){
          return kthLargest(root.right, k);
        }
        else if (right == k - 1){
          return root.val;
        }
        else{
          return kthLargest(root.left, k - right - 1);
        }
    }

    public int dfs(TreeNode node){
      if (node == null){
        return 0;
      }
      int left = dfs(node.left);
      int right = dfs(node.right);
      return 1 + left + right;
    }
}