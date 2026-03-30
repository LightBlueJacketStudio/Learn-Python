from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    #null check
    if not head: return [] # if none is passed in
    elif len(head) == 1 and n == 1: return [] # if only on elment and it is removed

    

if __name__ == "__main__":
    head = [1,2,3,4,5], n = 2
    print(removeNthFromEnd(head, n))

