class TreeNode:
    """Definition for a binary tree node."""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTreeDiameter:
    """
    This class provides a solution to find the diameter of a binary tree.
    The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
    """

    def __init__(self):
        self.diameter = 0  # Initialize diameter to zero.

    def diameter_of_binary_tree(self, root: Optional[TreeNode]) -> int:
        """Returns the diameter of the binary tree rooted at 'root'."""

        def depth(node: TreeNode) -> int:
            """Recursively calculates and returns the depth of the tree rooted at 'node'."""
            if not node:  # Base case: If node is None, return depth as 0.
                return 0

            # Recursively calculate depth of left/right subtree.
            left_depth = depth(node.left)
            right_depth = depth(node.right)

            # Update the diameter. The diameter through the current node
            # would be sum of depths of left and right subtrees.
            self.diameter = max(self.diameter, left_depth + right_depth)

            # Return the depth of the tree rooted at current node.
            return max(left_depth, right_depth) + 1

        # Start the depth calculation from the root.
        depth(root)

        # Return the calculated diameter.
        return self.diameter


# Test Cases
def test_diameter():
    btd = BinaryTreeDiameter()

    # Simple binary tree with 3 nodes.
    tree1 = TreeNode(1, TreeNode(2), TreeNode(3))
    assert btd.diameter_of_binary_tree(tree1) == 2  # Diameter passes through root and its two children.

    # More complex binary tree.
    tree2 = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
    assert btd.diameter_of_binary_tree(tree2) == 3  # Diameter passes through nodes 4, 2, and 5.

    # Binary tree with single node.
    tree3 = TreeNode(1)
    assert btd.diameter_of_binary_tree(tree3) == 0  # Diameter is 0 since there's only one node.

    print("All test cases passed!")


if __name__ == "__main__":
    test_diameter()
