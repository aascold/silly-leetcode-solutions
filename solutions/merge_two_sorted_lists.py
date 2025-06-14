'''
    My solution for "Merge Two Sorted Lists" problem.
    https://leetcode.com/problems/merge-two-sorted-lists/
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        tmp_node = ListNode(0, None)
        start_node = None
        while not (list1 is None and list2 is None):
            if list2 is None or (not list1 is None and list1.val < list2.val):
                tmp_node.next = ListNode(list1.val)
                list1 = list1.next
            else:
                tmp_node.next = ListNode(list2.val)
                list2 = list2.next
            tmp_node = tmp_node.next
            if start_node is None:
                start_node = tmp_node
        return start_node

        