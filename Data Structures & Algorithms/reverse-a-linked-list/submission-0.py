# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lis = []

        while head:
            lis.append(head.val)
            head = head.next
        if not lis:
            return None

        newHead = ListNode(lis.pop())
        new = newHead
        for i in range(len(lis),0,-1):
            new.next = ListNode(lis.pop())
            new = new.next

        return newHead
