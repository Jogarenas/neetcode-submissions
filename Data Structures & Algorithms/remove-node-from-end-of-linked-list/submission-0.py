# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        check = head
        listLength = 0

        while check: #COUNT THE LENGTH, SO THEN WE KNOW EXACTLY WHAT NODE TO TAKE OUT
            listLength += 1
            check = check.next
        curLen = 0
        parse = head #CREATE ANOTHER VARIABLE TO TRACK NEXT ITERATION

        if listLength == n: #IF WERE REMOVING LAST VALUE, SIMPLY DO THIS
            return head.next

        while curLen < (listLength - n) - 1: #ITERATE THROUGH LINKEDLIST THROUGH TO INDEX N
            parse = parse.next
            curLen += 1
        #ONCE WE REACH INDEX TO REMOVE, SET THE NODE BEFORE IT TO POINT TO THE NODE AFTER NODE n
        prev = parse
        parse.next = parse.next.next

        return head
            

            