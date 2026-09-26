# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse(self, head):
        node = head
        prev = None

        while node is not None:
            temp = node.next
            node.next = prev
            prev = node
            node = temp
        
        return prev



    def reorderList(self, head: Optional[ListNode]) -> None:

        fast = head
        slow = head

        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next

        
        second_half = slow.next
        slow.next = None

        list2 = self.reverse(second_half)

        node1 = head
        node2 = list2
        i = 0

        while node1 is not None and node2 is not None:
            temp1 = node1.next
            temp2 = node2.next

            node1.next = node2
            node2.next = temp1

            node1 = temp1
            node2 = temp2
        
            
        

            





        














