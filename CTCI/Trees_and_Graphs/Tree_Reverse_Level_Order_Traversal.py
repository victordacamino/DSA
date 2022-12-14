# Python program to print REVERSE level order traversal using
# stack and queue

from collections import deque

# A binary tree node
class Node:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Given a binary tree, print its nodes in reverse level order
def reverseLevelOrder(root):
    # we can use a double ended queue which provides O(1) insert at the beginning
    # using the appendleft method
    # we do the regular level order traversal but instead of processing the
    # left child first we process the right child first and the we process the left child
    # of the current Node
    # we can do this One pass reduce the space usage not in terms of complexity but intuitively

    q = deque()
    q.append(root)
    ans = deque()
    while q:
        node = q.popleft()
        if node is None:
            continue

        ans.appendleft(node.data)

        if node.right:
            q.append(node.right)

        if node.left:
            q.append(node.left)

    return ans


# Driver program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print("Level Order traversal of binary tree is")
print(reverseLevelOrder(root))
