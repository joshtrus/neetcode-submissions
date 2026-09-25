# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = []
        node1 = list1
        node2 = list2
        while node1 is not None and node2 is not None:
            if node1.val == node2.val:
                res.append(node1)
                res.append(node2)
                node1 = node1.next
                node2 = node2.next
        
            elif node1.val < node2.val:
                res.append(node1)
                node1 = node1.next
     
            else:
                res.append(node2)
                node2 = node2.next


        if node1 is None:
            while node2 is not None:
                res.append(node2)
                node2 = node2.next
        
        if node2 is None:
            while node1 is not None:
                res.append(node1)
                node1 = node1.next
        
        for i in range(len(res) -1):
            res[i].next = res[i+1]
        
        
        return res[0] if res else None