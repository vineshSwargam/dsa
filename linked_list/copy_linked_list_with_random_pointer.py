# Copy Linked List with Random Pointer
# Medium
# Topics
# Company Tags
# Hints

# You are given the head of a linked list of length n. Unlike a singly linked list, each node contains an additional pointer random, which may point to any node in the list, or null.

# Create a deep copy of the list.

# The deep copy should consist of exactly n new nodes, each including:

# The original value val of the copied node
# A next pointer to the new node corresponding to the next pointer of the original node
# A random pointer to the new node corresponding to the random pointer of the original node

# Note: None of the pointers in the new list should point to nodes in the original list.

# Return the head of the copied linked list.

# In the examples, the linked list is represented as a list of n nodes. Each node is represented as a pair of [val, random_index] where random_index is the index of the node (0-indexed) that the random pointer points to, or null if it does not point to any node.

# Example 1:

# Input: head = [[3,null],[7,3],[4,0],[5,1]]

# Output: [[3,null],[7,3],[4,0],[5,1]]

# Example 2:

# Input: head = [[1,null],[2,2],[3,2]]

# Output: [[1,null],[2,2],[3,2]]

# Constraints:

# 0 <= n <= 100
# -100 <= Node.val <= 100
# Node values are not guaranteed to be unique.
# random is null or is pointing to some node in the linked list.



# Topics

# Hash Table Linked List


# Recommended Time & Space Complexity

# You should aim for a solution as good or better than O(n) time and O(n) space, where n is the length of the given list.



# Hint 1

# There is an extra random pointer for each node, and unlike the next pointer, which points to the next node, the random pointer can point to any random node in the list. A deep copy is meant to create completely separate nodes occupying different memory. Why can't we build a new list while iterating through the original list?



# Hint 2

# Because, while iterating through the list, when we encounter a node and create a copy of it, we can't immediately assign the random pointer's address. This is because the random pointer might point to a node that has not yet been created. To solve this, we can first create copies of all the nodes in one iteration. However, we still can't directly assign the random pointers since we don't have the addresses of the copies of those random pointers. Can you think of a data structure to store this information? Maybe a hash data structure could help.



# Hint 3

# We can use a hash data structure, such as a hash map, which takes O(1) time to retrieve data. This can help by mapping the original nodes to their corresponding copies. This way, we can easily retrieve the copy of any node and assign the random pointers in a subsequent pass after creating copies of all nodes in the first pass.



# Company Tags
# Seen this question in a real interview?
# Yes
# No
# Acceptance Rate
# 71.0%


from utils.linked_list import Node, build_random_list, to_random_list, shares_nodes
from utils.print import print_list
from collections import defaultdict

# Definition for a Node.
class Node:
    def __init__(self, x: int, next, random):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head):
        if not head:
            return None
        
        nmap = defaultdict(Node)
        h = head


    
        while h:
            nmap[h] = Node(h.val, h.next, h.random)
            h = h.next

        print('Mapping -')
        for val in nmap.values():
            print(f'val - {val.val} list -')
            print_list(val)
        
        

        h = head
        while h:
            copy = nmap[h]
            if h.next != None:
                copy.next = nmap[h.next]
            if h.random != None:
                copy.random = nmap[h.random]
                
            h = h.next

        return nmap[head] # This works because neither part of it changes during the loops -
        # head: the loops move h, so head stays on the original first node.
        # nmap[head]: pass 1 stores the first node's copy there, and pass 2 only changes that copy's next and random, without replacing the entry.
        # so head safely points to its deep copy version


sol = Solution()

max_size = [[i, 99 - i] for i in range(100)]


# (head, expected) - each node is [val, random_index]
tests = [
    ([[3,None],[7,3],[4,0],[5,1]], [[3,None],[7,3],[4,0],[5,1]]),  # example 1
    # ([[1,None],[2,2],[3,2]], [[1,None],[2,2],[3,2]]),              # example 2
    # ([], []),                                                      # empty list
    # ([[1,None]], [[1,None]]),                                      # single node, random is null
    # ([[1,0]], [[1,0]]),                                            # single node, random points to itself
    # ([[1,None],[2,None],[3,None]], [[1,None],[2,None],[3,None]]),  # every random is null
    # ([[7,2],[7,0],[7,None]], [[7,2],[7,0],[7,None]]),              # all values equal, randoms differ
    # ([[1,3],[2,3],[3,3],[4,3]], [[1,3],[2,3],[3,3],[4,3]]),        # every random points to the last node
    # ([[1,0],[2,0],[3,1],[4,2]], [[1,0],[2,0],[3,1],[4,2]]),        # randoms point backward or to itself
    # ([[-100,1],[100,0]], [[-100,1],[100,0]]),                      # value limits
    # (max_size, max_size),                                          # max size
]

for vals, expected in tests:
    original = build_random_list(vals)
    copied = sol.copyRandomList(original)
    got = to_random_list(copied)
    deep = not shares_nodes(original, copied)
    status = "PASS" if got == expected and deep else "FAIL"
    note = "" if deep else "  (shares nodes with the original)"
    print(f"{status}  head={vals} -> {got}  expected {expected}{note}")
