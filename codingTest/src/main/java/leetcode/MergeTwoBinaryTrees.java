package leetcode;


/**
 * 617. Merge Two Binary Trees
 * Given two binary trees and imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not.
 * <p>
 * You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of new tree.
 * <p>
 * Example 1:
 * Input:
 * Tree 1                     Tree 2
 * 1                         2
 * / \                       / \
 * 3   2                     1   3
 * /                           \   \
 * 5                             4   7
 * Output:
 * Merged tree:
 * 3
 * / \
 * 4   5
 * / \   \
 * 5   4   7
 * Note: The merging process must start from the root nodes of both trees.
 */


/**
 * Definition for a binary tree node.
 * public class TreeNode {
 * int val;
 * TreeNode left;
 * TreeNode right;
 * TreeNode(int x) { val = x; }
 * }
 */
public class MergeTwoBinaryTrees {

    public TreeNode mergeTrees(TreeNode t1, TreeNode t2) {

        TreeNode result = null;

        if (t1 == null && t2 == null) {
            return null;
        }

        int t1val = 0;
        if (t1 != null) {
            t1val = t1.val;
        }

        int t2val = 0;
        if (t2 != null) {
            t2val = t2.val;
        }

        result = new TreeNode(t1val + t2val);

        result.left = mergeTrees(t1.left, t2.left);
        result.right = mergeTrees(t1.right, t2.right);

        return result;
    }

}


class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode(int x) {
        val = x;
    }
}

class TreeNodeExt extends TreeNode {

    int level;
    int seq;

    TreeNodeExt(int val, int level, int seq) {
        super(val);
        this.level = level;
        this.seq = seq;
    }

}