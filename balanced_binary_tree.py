from typing import Optional


class TreeNode:
    """Definition for a binary tree node."""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BalancedBinaryTree:
    def is_balanced(self, root: Optional[TreeNode]) -> bool:
        """
        Determines if a binary tree is height-balanced.

        A height-balanced binary tree is defined as a binary tree in which the depth of
        the two subtrees of every node never differs by more than 1.
        """

        def get_tree_depth(node: TreeNode) -> int:
            """Returns the depth of the tree rooted at node."""
            if not node:
                return 0
            left_depth = get_tree_depth(node.left)
            right_depth = get_tree_depth(node.right)
            return 1 + max(left_depth, right_depth)

        def check_balance(node: TreeNode) -> bool:
            """
            Checks if the tree rooted at node is balanced and
            the difference between the depths of left and right subtrees is not more than 1.
            """
            if not node:
                return True
            left_depth = get_tree_depth(node.left)
            right_depth = get_tree_depth(node.right)
            return abs(left_depth - right_depth) <= 1 and check_balance(node.left) and check_balance(node.right)

        return check_balance(root)


# Test cases
def test_balanced_binary_tree():
    tree1 = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(3)), TreeNode(2))
    tree2 = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4), TreeNode(4)), TreeNode(3)))

    bbt = BalancedBinaryTree()

    assert bbt.is_balanced(tree1) == True
    assert bbt.is_balanced(tree2) == False

    print("All test cases passed!")


if __name__ == "__main__":
    test_balanced_binary_tree()
