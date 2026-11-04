# Time Based Key-Value Store
# Medium
# Topics
# Company Tags
# Hints
# Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.

# Implement the TimeMap class:

# TimeMap() Initializes the object of the data structure.
# void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
# String get(String key, int timestamp) Returns a value such that set was called previously, with timestamp_prev <= timestamp. If there are multiple such values, it returns the value associated with the largest timestamp_prev. If there are no values, it returns "".
# Example 1:

# Input:
# ["TimeMap", "set", ["alice", "happy", 1], "get", ["alice", 1], "get", ["alice", 2], "set", ["alice", "sad", 3], "get", ["alice", 3]]

# Output:
# [null, null, "happy", "happy", null, "sad"]

# Explanation:
# TimeMap timeMap = new TimeMap();
# timeMap.set("alice", "happy", 1);  // store the key "alice" and value "happy" along with timestamp = 1.
# timeMap.get("alice", 1);           // return "happy"
# timeMap.get("alice", 2);           // return "happy", there is no value stored for timestamp 2, thus we return the value at timestamp 1.
# timeMap.set("alice", "sad", 3);    // store the key "alice" and value "sad" along with timestamp = 3.
# timeMap.get("alice", 3);           // return "sad"
# Constraints:

# 1 <= key.length, value.length <= 100
# key and value only include lowercase English letters and digits.
# 0 <= timestamp <= 10^7
# All the timestamps of set are strictly increasing.
# At most 2 * 10^5 calls will be made to set and get.


# Topics



# Recommended Time & Space Complexity
# You should aim for a solution with O(1) time for set(), O(logn) time for get(), and O(m * n) space, where n is the total number of values associated with a key, and m is the total number of keys.


# Hint 1
# Can you think of a data structure that is useful for storing key-value pairs? Perhaps a hash-based data structure where we not only store unique elements but also associate additional information with each element?


# Hint 2
# We store key-value pairs in a hash map. In this case, we store the keys as usual, but instead of a single value, we store a list of values, each paired with its corresponding timestamp. This allows us to implement the set() method in O(1). How can you leverage this hash map to implement the get() method?


# Hint 3
# A brute force solution would involve linearly going through every value associated with the key and returning the most recent value with a timestamp less than or equal to the given timestamp. This approach has a time complexity of O(n) for each get() call. Can you think of a better way? Since the timestamps in the value list are sorted in ascending order by default, maybe an efficient searching algorithm could help.


# Hint 4
# We can use binary search because the timestamps in the values list are sorted in ascending order. This makes it straightforward to find the value with the most recent timestamp that is less than or equal to the given timestamp.

from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        def binary_search(arr, target, l, r, fb):
            if l > r:
                return fb

            mid = (l+r)//2
            
            if arr[mid][0] == target:
                return arr[mid][1]

            if arr[mid][0] < target:
                fb = arr[mid][1]

            if arr[mid][0] > target:
                return binary_search(arr, target, l, mid-1, fb)
            return binary_search(arr, target, mid+1, r, fb)

        return binary_search(self.map[key], timestamp, 0, len(self.map[key])-1, '')


fns = ["TimeMap", "set", ["alice", "happy", 1], "get", ["alice", 1], "get", ["alice", 2], "set", ["alice", "sad", 3], "get", ["alice", 3]] # [null, null, "happy", "happy", null, "sad"]

# Constraints
# 1 <= key.length, value.length <= 100
# key and value only include lowercase English letters and digits.
# 0 <= timestamp <= 10^7
# All the timestamps of set are strictly increasing.
# At most 2 * 10^5 calls will be made to set and get.

fns_len = len(fns)
i = 0
res = []
while i < fns_len:
    if fns[i] == 'TimeMap':
        t = TimeMap()
        res.append(None)
        i += 1
    elif fns[i] == 'set':
        print(t.set(*fns[i+1]))
        res.append(None)
        i += 2
    elif fns[i] == 'get':
        val = t.get(*fns[i+1])
        print(val)
        res.append(val)
        i += 2

print('res -', res)



    


        