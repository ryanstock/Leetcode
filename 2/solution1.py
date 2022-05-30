# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution: 
    
    def linked_lists_to_number(self, list_node: Optional[ListNode]) -> int:
        
        list_str = ''
        while list_node:
            list_str += str(list_node.val)
            if list_node.next is None:
                break
            list_node=list_node.next
        return int(list_str[::-1])
           
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        l1_num = self.linked_lists_to_number(l1)
        l2_num = self.linked_lists_to_number(l2)
        
        sum_num = l1_num + l2_num

        str_num = str(sum_num)        
            
        temp_ListNode = ListNode()
        first_ListNode = temp_ListNode
        for i in range(len(str_num)-1, -1, -1):
            temp_ListNode.val = int(str_num[i]) 

            if i != 0:
                temp_ListNode.next = ListNode()
                temp_ListNode = temp_ListNode.next
                
        return first_ListNode