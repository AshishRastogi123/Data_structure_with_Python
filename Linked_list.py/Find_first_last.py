"""
Find where cycle started 
Link :https://leetcode.com/problems/linked-list-cycle-ii/description/

Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.

Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.
"""

from node_creation import Node, Singly_linked_list




p=Singly_linked_list()
p.appends(102)
p.appends(89)
p.appends(12)
p.appends(56)
p.traversal()