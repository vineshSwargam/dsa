# Min Stack
# Medium
# Topics
# Company Tags
# Hints

# Design a stack class that supports the push, pop, top, and getMin operations.

# MinStack() initializes the stack object.
# void push(int val) pushes the element val onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.
# Each function should run in 
# O
# (
# 1
# )
# O(1) time.

# Example 1:

# Input: ["MinStack", "push", 1, "push", 2, "push", 0, "getMin", "pop", "top", "getMin"]

# Output: [null,null,null,null,0,null,2,1]

# Explanation:
# MinStack minStack = new MinStack();
# minStack.push(1);
# minStack.push(2);
# minStack.push(0);
# minStack.getMin(); // return 0
# minStack.pop();
# minStack.top();    // return 2
# minStack.getMin(); // return 1
# Constraints:

# -2^31 <= val <= 2^31 - 1.
# pop, top and getMin will always be called on non-empty stacks.
# At most 
# 3
# ∗
# 10
# 4
# 3∗10 
# 4
#   calls will be made to push, pop, top, and getMin.


# Topics

 

# Recommended Time & Space Complexity
# You should aim for a solution with O(1) time for each function call and O(n) space, where n is the maximum number of elements present in the stack.


# Hint 1
# A brute force solution would be to always check for the minimum element in the stack for the getMin() function call. This would be an O(n) approach. Can you think of a better way? Maybe O(n) extra space to store some information.


# Hint 2
# We can use a stack to maintain the elements. But how can we find the minimum element at any given time? Perhaps we should consider a prefix approach.


# Hint 3
# We use an additional stack to maintain the prefix minimum element. When popping elements from the main stack, we should also pop from this extra stack. However, when pushing onto the extra stack, we should push the minimum of the top element of the extra stack and the current element onto this extra stack.


class MinStack:

    def __init__(self):
        self.stack = []
        self.s2 = []
        
    def is_empty(self):
        return len(self.stack) == 0

    def push(self, val: int) -> None:
        curr_min = min(val, self.s2[-1] if len(self.s2) > 0 else val)
        self.stack.append(val)
        self.s2.append(curr_min)
        return self.stack

    def pop(self) -> None:
        if self.is_empty():
            return None
        self.s2.pop()
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        if self.is_empty():
            return None
        return self.s2[-1]
        

sol = MinStack()

print(sol.push(1))
print(sol.push(2))
print(sol.push(0))
print(sol.getMin())
print(sol.pop())
print(sol.top())
print(sol.getMin())
