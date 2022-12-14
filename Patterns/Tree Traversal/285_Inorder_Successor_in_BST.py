# First solution: Without using BST's properties
class Solution1:

    previous = None
    inorder_successor_node = None

    def inorderSuccessor(self, root: "TreeNode", p: "TreeNode") -> "TreeNode":
        # Case 1: We simply need to find the leftmost node in the subtree rooted at p.right.
        if p.right:
            leftmost = p.right
            while leftmost.left:
                leftmost = leftmost.left

            self.inorder_successor_node = leftmost

        # Case 2: We need to perform the standard inorder traversal and keep track of the previous node.
        else:
            self.inorderCase2(root, p)

        return self.inorder_successor_node

    def inorderCase2(self, node: "TreeNode", p: "TreeNode"):
        if not node:
            return

        # Recurse on the left side
        self.inorderCase2(node.left, p)

        # Check if previous is the inorder predecessor of node
        if self.previous == p and not self.inorder_successor_node:
            self.inorder_successor_node = node
            return

        # Keeping previous up-to-date for further recursions
        self.previous = node

        # Recurse on the right side
        self.inorderCase2(node.right, p)


# TC = O(N)
# SC = O(N)


class Solution2:
    def inorderSuccessor(self, root: "TreeNode", p: "TreeNode") -> "TreeNode":
        # if node can be the extreme right node, we need to initialize successor as None
        successor = None

        while root:
            # just go to the right, successor will not be in left subtree neither in the current root
            if p.val >= root.val:
                root = root.right

            # if node is in the left subtree, the current node is a potential candidate (left -> root ->right)
            else:
                successor = root
                root = root.left
        return successor


# SC = O(1)
# TC = O(N)
