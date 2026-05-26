from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    #null check
    if not head: return None # if none is passed in
    if head.next is None and n == 1: return None # if there's only onw element and we are removing that

    # remove n th from end --> remove the node at index (all - n), since it's 0 index)
    # remove 2nd from the end, if we have 5 elements -> remove 5-2 = 3
    # 1 2 3 4 5 -> [0] [1] [2] [3] [4] -> [3] = 2nd from end
    # remove xyz[3]
    
    # edge case: the removal was the first or the last
    # how to handle cases when we need to remove the head?
    # use a dummy node 
    # use two pointers, fast and slow, in which they are N elements apart, when the
    # fast exits (end of list, we know the slow must be on the N th node of from the last)
    
    dummy = ListNode(0, head) # set the next of dummy to be our true head node
    fast = dummy 
    counter = n 
    # in case of needing to remove the head,
    # the fast would be on the end before the counter runs out 
    # 1 2 3 4 5, n = 5, counter = 5
    # counter = 5 --> fast = fast.next -> 1, slow = dummy
    # counter = 4 --> fast -> 2, slow = dummy
    # counter = 3 --> fast -> 3, slow = dummy
    # counter = 2 --> fast -> 4, slow = dummy
    # counter = 1 --> fast -> 5, slow = dummy (the node before the node to remove)
    # fast.next is None => slow point the dummy's next to the next of the head

    # for regular cases
    # 1 2 3 4 5, n = 2, counter = 2
    # counter = 2 --> fast -> 1, slow = dummy
    # counter = 1 --> fast -> 2, slow = dummy
    # counter = 0 --> fast -> 3, slow = 1
    # fast.next is not None --> fast -> 4, slow = 2
    # fast.next is not None --> fast -> 5, slow = 3 (the node before the node to remove)
    # fast.next is None --> slow.next = slow.next.next, 
    slow = dummy
    while fast.next is not None:
        if counter > 0: 
            counter -= 1
            fast = fast.next
        else: # slow move now
            slow = slow.next
            fast = fast.next

    # at this point, fast is at the last element
    # slow is at the length - n - 1 node, because when slow = head, we move fast as well
    # so fast is n+1 before slow
    # --> the next node of slow is the node we want to remove
    slow.next = slow.next.next
    return dummy.next # in case the removal was the head itself
 

if __name__ == "__main__":
    #head = [1,2,3,4,5],
    n = 2
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = None

    head = node1

    #Invoke the funtion
    removeNthFromEnd(head, n)

    while head:
        print(head.val)
        head = head.next

