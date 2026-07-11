# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        if not list1:
            return list2
        if not list2:
            return list1

        dummy = ListNode(0)
        current = dummy 
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1   
                list1 = list1.next   
            else:
                current.next = list2   
                list2 = list2.next   
            current = current.next   
        if list1:
            current.next = list1
        elif list2:
            current.next = list2

        return dummy.next
