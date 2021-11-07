# 234  Palindrome Linked List
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def isPalindrome(head: Optional[ListNode]) -> bool:
    s = ""
    node = head
    while node:
        s += str(node.val)
        node = node.next
    if s == s[::-1]:
        return True
    return False


# using idea of stack
def isPalindrome2(head: Optional[ListNode]) -> bool:
    stack = []
    node = head
    while node:
        stack.append(node.val)
        node = node.next

    while head:
        if head.val != stack.pop():
            return False
        head = head.next
    return True
