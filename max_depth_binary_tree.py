from typing import Optional


class TreeNode:
    """Definition for a binary tree node."""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTreeMaxDepth:
    """
    This class calculates the maximum depth (or height) of a binary tree.
    The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
    """

    def max_depth(self, root: Optional[TreeNode]) -> int:
        """Returns the maximum depth of the binary tree rooted at 'root'."""

        def depth(node: TreeNode) -> int:
            """Recursively calculates and returns the depth of the tree rooted at 'node'."""
            if not node:
                return 0

            # Recursively calculate depth of left and right subtrees and return the maximum.
            return 1 + max(depth(node.left), depth(node.right))

        return depth(root)


# Test Cases
def test_max_depth():
    btm = BinaryTreeMaxDepth()

    # Simple binary tree with 3 nodes.
    tree1 = TreeNode(1, TreeNode(2), TreeNode(3))
    assert btm.max_depth(tree1) == 2  # Root and two child nodes.

    # More complex binary tree.
    tree2 = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
    assert btm.max_depth(tree2) == 3  # Maximum depth goes through root, node 2 and node 4 or 5.

    # Binary tree with single node.
    tree3 = TreeNode(1)
    assert btm.max_depth(tree3) == 1  # Only the root node is present.

    print("All test cases passed!")


if __name__ == "__main__":
    test_max_depth()
