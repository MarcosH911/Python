class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def height(self):
        if not self:
            return 0
        else:
            return 1 + max(TreeNode.height(self.left), TreeNode.height(self.right))

    def size(self):
        if not self:
            return 0
        else:
            return 1 + TreeNode.size(self.left) + TreeNode.size(self.right)

    def inorder_traversal(self):
        if not self:
            return []
        else:
            return TreeNode.inorder_traversal(self.left) + [self.key] + TreeNode.inorder_traversal(self.right)

    def preorder_traversal(self):
        if not self:
            return []
        else:
            return [self.key] + TreeNode.inorder_traversal(self.right) + TreeNode.inorder_traversal(self.left)

    def postorder_traversal(self):
        if not self:
            return []
        else:
            return TreeNode.inorder_traversal(self.right) + TreeNode.inorder_traversal(self.left) + [self.key]

    def display_keys(self, level=0, space='\t'):
        if not self:
            print(space * level + 'X')
            return

        if not self.right and not self.left:
            print(space * level + str(self.key))
            return

        TreeNode.display_keys(self.right, level + 1)
        print(space * level + str(self.key))
        TreeNode.display_keys(self.left, level + 1)

    def to_tuple(self):
        if not self:
            return None
        if not self.right and not self.left:
            return self.key
        return TreeNode.to_tuple(self.left), self.key, TreeNode.to_tuple(self.right)

    @staticmethod
    def parse_tuple(data):
        if not data:
            node = None

        elif isinstance(data, tuple) and len(data) == 3:
            node = TreeNode(data[1])
            node.left = TreeNode.parse_tuple(data[0])
            node.right = TreeNode.parse_tuple(data[2])

        else:
            node = TreeNode(data)
        return node
