#  Date & Time 11/10/2024, 04:27 PM.
#  @author Mesfin Haftu
class LinkedList:
    """
    A simple linked list implementation with append and
    traversal methods.
    """
    def __init__(self, val, head=None):
        self.val = val
        self.head = head
        self.next = None
class CycleDetection(LinkedList):
    """
    Cycle detection and repeated value checking using
    Floyd's Tortoise and Hare algorithm.
    """
    def cycle(llist):
        slow = llist. head
        fast = llist.head
        met = False
        while fast is not None and fast.nxt is not None:
            slow = slow.nxt
            fast = fast.nxt.nxt
            if slow == fast:
                met = True
                break
        if not met:
            return None
        else:
            slow = llist.head
            while slow != fast:
                slow = slow.nxt
                fast = fast.nxt
                return slow