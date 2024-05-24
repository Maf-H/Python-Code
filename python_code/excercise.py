# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution(object):
    def __str__(self):
        return f"[{self.middleNode()}]"
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        mid = 0
        middle = []
        list_node = ListNode()
        head = list_node
        temp_node = list_node
        while temp_node is not None:
            mid += 1
            temp_node = temp_node.next

        if 1 <= mid <= 50:
            for i in range(mid):
                if 1 <= list_node.val <= 100 and list_node is not None:
                    list_node = list_node.next
            print(list_node)
            return list_node
