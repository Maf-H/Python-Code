class ListNode:
    """
    Definition for singly-linked list.
    """
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __str__(self):
        return f'[{self.val}] ->{self.next}'
class Solution(ListNode):
    """
    Reverse a singly linked list.
    """
    def reverse_list_recursive(self, head):
        """
        Reverse the given linked list recursively and return its head.
        1 -> 2 -> 3 -> 4 -> 5
        Recursive Call 1:2 -> 3 -> 4 -> 5
        Recursive Call 2:3 -> 4 -> 5
        Recursive Call 3:4 -> 5
        Recursive Call 4:5 (base case)
        Unwinding the Recursion:
        the trick is "  head.next.next = head....this makes 4 is head 4 -> 5 ->4 (both 4 are are the same node)
                        head.next = None"    ....this makes 5 -> 4 -> None                        
        5 -> 4 (reversed)
        5 -> 4 -> 3 (reversed)
        5 -> 4 -> 3 -> 2 (reversed)
        5 -> 4 -> 3 -> 2 -> 1 (reversed)
        Final Result: 5 -> 4 -> 3 -> 2 -> 1ist(head))
        """
        if head is None or head.next is None:
            return head

        node = self.reverse_list_recursive(head.next)

        head.next.next = head
        head.next = None
        return node
    def reverse_list(self, head):
        """
        Reverse the given linked list and return its head.
        """
        curr = head
        prev = None

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev

if __name__ == '__main__':
    s1 = Solution()
    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(3)
    l4 = ListNode(4)
    l5 = ListNode(5)
    head = l1
    l1.next = l2
    l2.next = l3
    l3.next = l4
    l4.next = l5
    print(l1)
    
    # s1.reverse_list_recursive(head)
    # print(l1)
    print(s1.reverse_list_recursive(head))
    # print(s1.reverse_list(head))
    # print(head)
