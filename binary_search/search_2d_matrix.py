# Search a 2D Matrix
# Medium
# Topics
# Company Tags
# Hints
# You are given an m x n 2-D integer array matrix and an integer target.

# Each row in matrix is sorted in non-decreasing order.
# The first integer of every row is greater than the last integer of the previous row.
# Return true if target exists within matrix or false otherwise.

# Can you write a solution that runs in O(log(m * n)) time?

# Example 1:



# Input: matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 10

# Output: true
# Example 2:



# Input: matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 15

# Output: false
# Constraints:

# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 100
# -10000 <= matrix[i][j], target <= 10000


# Topics

# Recommended Time & Space Complexity

# Hint 1
# A brute force solution would be to do a linear search on the matrix. This would be an O(m * n) solution. Can you think of a better way? Maybe an efficient searching algorithm, as the given matrix is sorted.


# Hint 2
# We can use binary search, which is particularly effective when we visualize a row as a range of numbers, [x, y] where x is the first cell and y is the last cell of a row. Using this representation, it becomes straightforward to check if the target value falls within the range. How can you use binary search to solve the problem?


# Hint 3
# We perform a binary search on the rows to identify the row in which the target value might fall. This operation takes O(logm) time, where m is the number of rows. Now, when we find the potential row, can you find the best way to search the target in that row? The sorted nature of each row is the hint.


# Hint 4
# Once we identify the potential row where the target might exist, we can perform a binary search on that row which acts as a one dimensional array. It takes O(logn) time, where n is the number of columns in the row.

class Solution:
    def binary_search(self, nums, target: int, l, r) -> int:
        if l > r:
            return False
    
        mid = (l+r)//2
        print(nums, target, mid)
        
        if target == nums[mid]:
            return True
        
        if target < nums[mid]:
            return self.binary_search(nums, target, l, mid-1)

        if target > nums[mid]:
            return self.binary_search(nums, target, mid+1, r)

        return False
        
    def mat_binary_search(self, matrix, target: int, l, r) -> int:
        print(matrix)

        if l>r:
            return False

        print(target, l, r)
        mid_mat = (l+r)//2
        print('mid_mat -', mid_mat)

        if target < matrix[mid_mat][0]:
            return self.mat_binary_search(matrix, target, l, mid_mat-1)
        elif target > matrix[mid_mat][-1]:
            return self.mat_binary_search(matrix, target, mid_mat+1, r)
        else:
            return self.binary_search(matrix[mid_mat], target, 0, len(matrix[mid_mat])-1)


    def search_matrix(self, matrix, target: int) -> int:
        if not matrix[-1][-1] >= target >= matrix[0][0]:
            return False
        return self.mat_binary_search(matrix, target, 0, len(matrix)-1)
        
        

sol = Solution()

m = [[1,2,4,8],[10,11,12,13],[14,20,30,40]]

nums, target = m, 10                 # True  - first element of a middle row
# nums, target = m, 15               # False - gap inside a row (between 14 and 20)
# nums, target = m, 9                # False - gap between rows (after 8, before 10)
# nums, target = m, 1                # True  - very first element
# nums, target = m, 40               # True  - very last element
# nums, target = m, 0                # False - smaller than everything
# nums, target = m, 41               # False - bigger than everything
# nums, target = m, 13               # True  - last element of a middle row
# nums, target = [[5]], 5            # True  - 1x1 matrix
# nums, target = [[5]], 3            # False - 1x1 matrix, missing
# nums, target = [[1,3,5,7]], 7      # True  - single row
# nums, target = [[1],[3],[5]], 3    # True  - single column
# nums, target = [[1],[3],[5]], 4    # False - single column, missing

print(sol.search_matrix(nums, target))