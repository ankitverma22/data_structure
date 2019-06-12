class Node:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.value = val


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root == None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, cur_node):
        if value < cur_node.value:
            if cur_node.left == None:
                cur_node.left = Node(value)
            else:
                self._insert(value, cur_node.left)
        if value >= cur_node.value:
            if cur_node.right == None:
                cur_node.right = Node(value)
            else:
                self._insert(value, cur_node.right)

    def PrintTree(self):
        if self.root != None:
            self._print_tree(self.root)

    def _print_tree(self, cur_node):
        if cur_node != None:
            self._print_tree(cur_node.left)
            print(cur_node.value)
            self._print_tree(cur_node.right)


if __name__ == '__main__':
    tree = BinaryTree()
    tree.insert(12)
    tree.insert(10)
    tree.insert(13)
    tree.insert(11)

    tree.PrintTree()
    