# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    resultList = ListNode()
    while l1.next and l2.next:
        resultList.val = min(l1.val, l2.val)
        resultList = resultList.next
        resultList.val = max(l1.val, l2.val)
        resultList = resultList.next

        l1 = l1.next
        l2 = l2.next

    return resultList

