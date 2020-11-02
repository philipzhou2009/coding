# https://leetcode.com/problems/binary-tree-maximum-path-sum/

from typing import List

logger = print if False else lambda *arg: None


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:

        result = getMax(root)

        return result


def getMax(node: TreeNode) -> int:

    logger("node=", node.val)
    vRoot = node.val
    vLeft = float('-inf')
    vRight = float('-inf')
    if node.left != None:
        vLeft = getMax(node.left)

    if node.right != None:
        vRight = getMax(node.right)

    if node.left == None and node.right == None:
        vMax = vRoot
    else:
        vMax = max(
            vRoot + vLeft + vRight, vLeft, vRight, vRoot, vRoot + vLeft, vRoot + vRight
        )

    logger("vMax=", vMax)

    return vMax
