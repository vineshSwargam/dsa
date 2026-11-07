# LRU Cache
# Medium
# Topics
# Company Tags
# Hints

# Implement the Least Recently Used (LRU) cache class LRUCache. The class should support the following operations

# LRUCache(int capacity) Initialize the LRU cache of size capacity.
# int get(int key) Return the value corresponding to the key if the key exists, otherwise return -1.
# void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the introduction of the new pair causes the cache to exceed its capacity, remove the least recently used key.

# A key is considered used if a get or a put operation is called on it.

# Ensure that get and put each run in
# O(1) average time complexity.

# Example 1:

# Input:
# ["LRUCache", [2], "put", [1, 10],  "get", [1], "put", [2, 20], "put", [3, 30], "get", [2], "get", [1]]

# Output:
# [null, null, 10, null, null, 20, -1]

# Explanation:
# LRUCache lRUCache = new LRUCache(2);
# lRUCache.put(1, 10);  // cache: {1=10}
# lRUCache.get(1);      // return 10
# lRUCache.put(2, 20);  // cache: {1=10, 2=20}
# lRUCache.put(3, 30);  // cache: {2=20, 3=30}, key=1 was evicted
# lRUCache.get(2);      // returns 20
# lRUCache.get(1);      // return -1 (not found)

# Constraints:

# 1 <= capacity <= 3000
# 0 <= key <= 10^4
# 0 <= value <= 10^5
# At most 2 * 10^5 calls will be made to get and put.



# Topics

# Hash Table Linked List Design Doubly-Linked List


# Recommended Time & Space Complexity

# You should aim for a solution with O(1) time for each put() and get() function call and an overall space of O(n), where n is the capacity of the LRU cache.



# Hint 1

# Can you think of a data structure for storing data in key-value pairs? Maybe a hash-based data structure with unique keys.



# Hint 2

# We can use a hash map which takes O(1) time to get and put the values. But, how can you deal with the least recently used to be removed criteria as a key is updated by the put() or recently used by the get() functions? Can you think of a data structure to store the order of values?



# Hint 3

# A brute-force solution would involve maintaining the order of key-value pairs in an array list, performing operations by iterating through the list to erase and insert these key-value pairs. However, this would result in an O(n) time complexity. Can you think of a data structure that allows removing and reinserting elements in O(1) time?



# Hint 4

# We can use a doubly-linked list, which allows us to remove a node from the list when we have the address of that node. Can you think of a way to store these addresses so that we can efficiently remove or update a key when needed?



# Hint 5

# We can use a doubly linked list where key-value pairs are stored as nodes, with the least recently used (LRU) node at the head and the most recently used (MRU) node at the tail. Whenever a key is accessed using get() or put(), we remove the corresponding node and reinsert it at the tail. When the cache reaches its capacity, we remove the LRU node from the head of the list. Additionally, we use a hash map to store each key and the corresponding address of its node, enabling efficient operations in O(1) time.



# Company Tags
# Seen this question in a real interview?
# Yes
# No
# Acceptance Rate
# 47.7%

class Node:
    def __init__(self, key, val, prev = None, nxt = None):
        self.key = key
        self.val = val
        self.next = nxt
        self.prev = prev

    # def get(self, key: int) -> int:
    #     pass

    # def put(self, key: int, value: int) -> None:
    #     pass
    
class LRUCache:
    # for getting and putting, hash will do it in O(1) time
    # how to keep track of lru though?

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = None
        self.tail = None

    def add_tail(self, node):
        node.next = None
        node.prev = self.tail
        if self.tail != None:
            self.tail.next = node
        self.tail = node

    def update_key_pos_in_cache(self, key):
        node = self.cache[key]
        prev = node.prev
        nxt = node.next
        if prev == None:
            self.head = nxt
        else:
            prev.next = nxt
        nxt.prev = prev
    
        self.add_tail(node)

    def get(self, key: int) -> int:
        if key in self.cache:
            if self.tail != self.cache[key]:
                self.update_key_pos_in_cache(key)
            return self.cache[key].val
        return -1

    def get_cache_len(self):
        return len(self.cache)

    def is_at_capacity(self):
        if self.get_cache_len() == self.capacity:
            return True
        return False

    def put(self, key: int, value: int) -> None:
        # key already in cache
        if key in self.cache:
            # update key val
            self.cache[key].val = value
            if self.tail != self.cache[key]:
                self.update_key_pos_in_cache(key)

        # key not in cache
        elif key not in self.cache:
            # cache at capacity, so remove head first
            if self.is_at_capacity():
                del self.cache[self.head.key]
                nxt = None
                if self.head.next != None:
                    nxt = self.head.next
                    nxt.prev = None
                
                self.head = nxt
                if self.capacity == 1:
                    self.tail = None

            # add to cache map
            self.cache[key] = Node(key, value)

            # since key not in cache, this would be added at tail
            self.add_tail(self.cache[key])

            # head is either none or a node | None if no keys added yet or cap is 1
            if self.head == None:
                self.head = self.cache[key]
            

        


# (capacity, operations, expected) - expected has one result per operation, and put returns None
tests = [
    # example 1
    (2, [("put",1,10), ("get",1), ("put",2,20), ("put",3,30), ("get",2), ("get",1)],
        [None, 10, None, None, 20, -1]),

    # get on an empty cache
    (1, [("get",1)],
        [-1]),

    # capacity 1, the new key evicts the old one
    (1, [("put",1,10), ("put",2,20), ("get",1), ("get",2)],
        [None, None, -1, 20]),

    # capacity 1, updating a key doesn't evict it
    (1, [("put",1,10), ("put",1,20), ("get",1)],
        [None, None, 20]),

    # updating an existing key at capacity evicts nothing
    (2, [("put",1,10), ("put",2,20), ("put",1,11), ("get",1), ("get",2)],
        [None, None, None, 11, 20]),

    # get counts as a use, so 2 is evicted instead of 1
    (2, [("put",1,10), ("put",2,20), ("get",1), ("put",3,30), ("get",2), ("get",1), ("get",3)],
        [None, None, 10, None, -1, 10, 30]),

    # put on an existing key counts as a use, so 2 is evicted instead of 1
    (2, [("put",1,10), ("put",2,20), ("put",1,11), ("put",3,30), ("get",2), ("get",1), ("get",3)],
        [None, None, None, None, -1, 11, 30]),

    # get on a missing key changes nothing, so 1 is still the oldest
    (2, [("put",1,10), ("put",2,20), ("get",9), ("put",3,30), ("get",1), ("get",2), ("get",3)],
        [None, None, -1, None, -1, 20, 30]),

    # key 0 and value 0 are real entries, not "missing"
    (2, [("put",0,0), ("get",0), ("put",1,0), ("get",1)],
        [None, 0, None, 0]),

    # evicted key can be added back
    (1, [("put",1,10), ("put",2,20), ("put",1,11), ("get",1), ("get",2)],
        [None, None, None, 11, -1]),

    # evictions happen oldest first
    (3, [("put",1,10), ("put",2,20), ("put",3,30), ("put",4,40), ("put",5,50), ("get",1), ("get",2), ("get",3), ("get",4), ("get",5)],
        [None, None, None, None, None, -1, -1, 30, 40, 50]),

    # order keeps changing as keys are used
    (2, [("put",1,1), ("put",2,2), ("get",1), ("put",3,3), ("get",2), ("put",4,4), ("get",1), ("get",3), ("get",4)],
        [None, None, 1, None, -1, None, -1, 3, 4]),

    # a node that became head through eviction can still move to the tail, so 3 is evicted instead of 2
    (2, [("put",1,10), ("put",2,20), ("put",3,30), ("get",2), ("put",4,40), ("get",2), ("get",3), ("get",4)],
        [None, None, None, 20, None, 20, -1, 40]),

    # max capacity, keys 0-999 are evicted
    (3000, [("put",i,i) for i in range(4000)] + [("get",999), ("get",1000), ("get",3999)],
        [None]*4000 + [-1, 1000, 3999]),
]

passed = 0
for capacity, operations, expected in tests:
    lru = LRUCache(capacity)
    got = [getattr(lru, op)(*args) for op, *args in operations]
    status = "PASS" if got == expected else "FAIL"
    passed += got == expected
    if len(operations) <= 20:
        print(f"{status}  capacity={capacity} {operations} -> {got}  expected {expected}")
    else:
        print(f"{status}  capacity={capacity} [{len(operations)} operations] -> last 3 {got[-3:]}  expected {expected[-3:]}")

print(f"{passed}/{len(tests)} passed")
