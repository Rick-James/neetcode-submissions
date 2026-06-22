"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old_node_to_copy = {None: None}

        current = head
        while current:
            copy = Node(current.val)
            old_node_to_copy[current] = copy
            current = current.next

        current = head
        while current:
            copy = old_node_to_copy[current]
            copy.next = old_node_to_copy[current.next]
            copy.random = old_node_to_copy[current.random]
            current = current.next
        return old_node_to_copy[head]