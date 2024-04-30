#  Date & Time 14/04/2024, 21:56.
#  @author Mesfin Haftu

#  Date & Time 14/04/2024, 21:55.
#  @author Mesfin Haftu

#  Date & Time 14/04/2024, 21:54.
#  @author Mesfin Haftu

#  Date & Time (\d+)", 1, "-")14/04/2024, 21:53.
#  @author Mesfin Haftu

class Node:
    """An object to sort a single node of a linked list
    attributes: data
                next_node
    
    """
    data = None
    next_node = None
    
    def __init__(self, data):
        self.data = data
    
    def __str__(self):
        return "<Node data: %d>" % self.data

    def __repr__(self):
        return "<Node data: %d>" % self.data


class Linked_List:
    """
    Single linked list
    """
    head = None

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def size_of_node(self):
        current = self.head
        count = 0

        while current:
            count += 1
            current = current.next_node

        return count

    def add_node(self, data):
        """
        Adds a node at the head of the list
        Points to the former head of the linked list
        new node becomes head of the list
        :param data:
        :return None:
        """
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def search_node(self, key):
        """
        Returns the first node who has the key
        else returns None
        :param key:
        :return:
        """
        current = self.head

        while current:
            if current.data == key:
                return current
            current = current.next_node
        return None

    def insert_node(self, data, index):
        """
        Insert data @ index + 1
        :param data:
        :param index:
        :return:
        """
        if index == 0:
            self.add_node(data)
        elif index == 1:
            node = Node(data)

            old_head = self.head
            self.head = node
            node.next_node = old_head
        else:
            position = index
            node = Node(data)
            current = self.head
            previous_node = None
            while position > 1:
                previous_node = current
                current = current.next_node
                position -= 1

            node.next_node = current
            previous_node.next_node = node

    def remove_node(self, value):
        """
        Removes the node that matches the data value
        :param value:
        :return:
        """
        current = self.head
        found = False

        while current and not found:
            if current.data == value and current == self.head:
                self.head = current.next_node
                found = True
            elif current.data == value:
                previous_node.next_node = current.next_node
                found = True
            else:
                previous_node = current
                current = current.next_node
        return current, "Removed"

    def __str__(self):
        """
        Prints all the elements of the linked list.
        :return:
        """
        node = []
        current = self.head
        while current:
            if current is self.head:
                node.append("[Head: %d]" % current.data)
            elif current.next_node is None:
                node.append("[Tail: %d]" % current.data)
            else:
                node.append("[%d: ]" % current.data)
            current = current.next_node
        return "-> ".join(node)

if __name__ == "__main__":
    try:
        linked_list = Linked_List()
        N1 = Node(10)
        N2 = Node(20)
        N1.next_node = N2
        N3 = Node(30)
        N2.next_node = N3
        N4 = Node(40)
        N3.next_node = N4
        linked_list.head = N1
        linked_list.add_node(9)
        linked_list.add_node(8)
        linked_list.add_node(7)
        linked_list.add_node(6)

        print("Size = ", linked_list.size_of_node())
        print(linked_list)
        # print("Found the item? ", linked_list.search_node(6))
        linked_list.insert_node(50, 1)
        print("Size = ", linked_list.size_of_node())
        print(linked_list)
        print(linked_list.remove_node(50))
        print(linked_list.remove_node(9))
        print(linked_list.remove_node(40))
        print(linked_list)
        print("Size = ", linked_list.size_of_node())
    except Exception as err:
        print(err)
