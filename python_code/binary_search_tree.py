#  Copyright (c) 27-06/04/2024, 16:48.
#  @author Mesfin Haftu

class Tree_Node:
    """Representation of tree node"""
    def __init__(self, value=None):
        self.left = None
        self.right = None
        self.value = value

    def __str__(self):
        return self.value

class BST(Tree_Node):
    """Representation of binary search tree"""
    def __init__(self, value=None):
        Tree_Node.__init__(self, value)
        self.root = None


    def insert(self, value):
        """If value was not in the tree
            inserts the value to the binary tree,
            else do nothing
        """
        new_node = BST(value)
        # If the tree is empty set the new node to root
        if self.is_empty():
            self.root = new_node
            return

        current = self.root
        while value != current.value:
            if value < current.value:
                if current.left:
                    # If left node exits with value, think left as root and call insert() from that.
                    current = current.left
                else:
                    # If left node is None insert the value to the left subtree
                    current.left = new_node
                    return

            # Insert into the right subtree if the value is greater than the root value
            else:
                # If right node exits with value, think right as root and call insert() from that.
                if current.right:
                    current = current.right
                else:
                    # If right node is None insert the value to the right subtree
                    current.right = new_node
                    return


    # @TODO
    def search(self, value):
        """
        Searches for a value in a binary search tree.

        Args:
            value: The value to search for.
        Returns:
            True if found, otherwise None.
        """
        current = self.root
        while current is not None:
            if value == current.value:
                print(f'Yes {value} is in the tree.')
                return True
            elif value < current.value:
                if current.left is None:
                    break
                current = current.left
            else:
                if current.right is None:
                    break
                current = current.right
        print(f'No {value} is in the tree.')
        return None

    def delete(self, value):
        """
        If Value found in the binary tree, it deletes a value from it.
        else do nothing
        Args:
            value: The value to delete.
        Returns:
            The updated root node of the BST.
        """
        parent = self.root
        current = self.root
        is_left_child = False
        if current is None:
            print("Empty Tree")
            return current

        # Search for the node to delete
        while value != current.value:
            parent = current
            if value < current.value:
                is_left_child = True
                current = current.left
            else:
                current = current.right
            if current is None:
                print(value, "not exist in a tree")
                return False

        if current.left is None and current.right is None:
            # Has No children, means it's a leaf node
            if current == self.root:
                # Deletes the root
                self.root = None
            elif is_left_child:
                # Disconnects the left leaf from the branch
                parent.left = None
            else:
                # Disconnects the right leaf from the branch
                parent.right = None

        # if no right child, replace with left subtree
        elif current.left is not None and current.right is None:
            # Has only left child
            if current == self.root:
                # change root of the tree to the left subtree
                self.root = parent.left
            elif is_left_child:
                # Disconnects the left node from the branch
                parent.left = current.left
            else:
                # Disconnects the right node from the branch
                parent.right = current.right

        # if no left child, replace with right subtree
        elif current.right is not None and current.left is None:
            # Has only right branch
            if current == self.root:
                # Deletes the root
                self.root = parent.right
            elif is_left_child:
                # Disconnects the left leaf from the branch
                parent.left = current.right
            else:
                # Disconnects the right leaf from the branch
                parent.right = current.right

        else:
            # Has two (left and right) leaf or branch, so replace with
            # in order successor.
            successor = self._get_successor(current)
            if current == self.root:
                # Deletes the root
                self.root = successor
            elif is_left_child:
                # Disconnects the left leaf from the branch
                parent.left = successor
            else:
                # Disconnects the right leaf from the branch
                parent.right = successor
            successor.left = current.left

        print(value, "is deleted from the tree")
        return True

    def _get_successor(self, del_node):
        successor_parent = del_node
        successor = del_node
        current = del_node.right
        while current is not None:
            successor_parent = successor
            successor = current
            current = current.left

        if successor != del_node.right:
            successor_parent.left = successor.right
            successor.right = del_node.right

        return successor

    def in_order(self, bst, lst=[]):
        if bst is not None:
            self.in_order(bst.left, lst)
            lst.append(bst.value)
            # print(bst.value, end=' ')
            self.in_order(bst.right, lst)
        return

    # TODO
    def pre_order(self, bst, lst=[]):
        if bst is not None:
            # lst.append(bst.value)
            print(bst.value, end=' ')
            self.pre_order(bst.left)
            self.pre_order(bst.right)
        return

    # TODO
    def post_order(self, bst, lst=[]):
        if bst is not None:
            self.post_order(bst.left)
            self.post_order(bst.right)
            # lst += [bst.value]
            print(bst.value, end=' ')
        return

    def get_min(self, current):
        """
        Returns the minimum value from the binary tree.
        """
        if self.is_empty():
            return None
        # current = self.root
        while current.left is not None:
            current = current.left
        print("Minimum: ", current.value)
        return current.value
    def get_max(self, current):
        """
        Returns the maximum value from the binary tree.
        """
        if self.is_empty():
            return None

        # current = self.root
        while current.right is not None:
            current = current.right
        print("Maximum: ", current.value)
        return current
    def is_empty(self):
        """Check if the node is None"""
        if self.root is None:
            return True

if __name__ == '__main__':
    lst = []
    lst_1 = []
    lst_2 = []
    bst = BST()

    bst.insert(10)
    bst.insert(8)
    bst.insert(12)
    bst.insert(10)
    bst.insert(7)
    bst.insert(9)
    bst.insert(11)
    bst.insert(13)

    bst.search(13)
    bst.get_min(bst.root)
    bst.get_max(bst.root)
    print('Before Deleting any element')
    bst.in_order( bst.root, lst)
    print(lst)
    # print(bst.pre_order())
    # print(bst.pre_order())
    # print(bst.post_order())
    bst.delete(10)
    print('After Deleting the above element')
    lst = []
    bst.in_order(bst.root, lst)
    print(lst)
    bst.pre_order(bst)
    bst.in_order(bst)
    bst.post_order(bst)

