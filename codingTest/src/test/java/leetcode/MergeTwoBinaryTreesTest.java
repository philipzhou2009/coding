package leetcode;

import org.junit.Test;

import static java.lang.Math.pow;

public class MergeTwoBinaryTreesTest {

    @Test
    public void mergeTrees() {

        TreeNode t1 = new TreeNode(1);
        printRightNode(t1.val);

        TreeNode l1left = new TreeNode(3);
        t1.left = l1left;
        printLeftNode(l1left.val);

        t1.right = new TreeNode(2);
        printRightNode(t1.right.val);

        l1left.left = new TreeNode(5);
        printLeftNode(l1left.left.val);


        TreeNode t2 = new TreeNode(2);
        printRightNode(t2.val);
        TreeNode t2l2left = new TreeNode(1);
        printLeftNode(t2l2left.val);
        TreeNode t2l2right = new TreeNode(3);
        printRightNode(t2l2right.val);
        t2.left = t2l2left;
        t2.right = t2l2right;

        TreeNode t2l32 = new TreeNode(4);
        TreeNode t2l34 = new TreeNode(7);

        t2l2left.right = t2l32;
        t2l2right.right = t2l34;


    }

    private void printLeftNode(int val) {
        System.out.print("" + val + "    ");
    }

    private void printRightNode(int val) {
        System.out.println("" + val + "");
    }

    @Test
    public void mergeTrees_withTreeNodeExt() {

        TreeNodeExt t1 = new TreeNodeExt(1, 1, 1);
        TreeNodeExt l1left = new TreeNodeExt(3, 2, 1);
        t1.left = l1left;
        t1.right = new TreeNodeExt(2, 2, 2);
        l1left.left = new TreeNodeExt(5, 3, 1);

        printTree(t1);

        TreeNodeExt t2 = new TreeNodeExt(2, 1, 1);
        TreeNodeExt t2l2left = new TreeNodeExt(1, 2, 1);
        TreeNodeExt t2l2right = new TreeNodeExt(3, 2, 2);
        t2.left = t2l2left;
        t2.right = t2l2right;

        TreeNodeExt t2l32 = new TreeNodeExt(4, 3, 2);
        TreeNodeExt t2l34 = new TreeNodeExt(7, 3, 4);

        t2l2left.right = t2l32;
        t2l2right.right = t2l34;

        printTree(t2);

    }


    private void printTree(TreeNodeExt tree) {

        if (tree != null) {

            System.out.print(tree.val);


            double pow = pow(2, tree.level - 1);
            if (pow == tree.seq) {
                System.out.println("\n");
            } else {
                System.out.println("    ");

            }

            printTree((TreeNodeExt) tree.left);
            printTree((TreeNodeExt) tree.right);

        }
    }
}