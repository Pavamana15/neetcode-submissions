# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def find_all_paths(root):
            all_paths = []

            def dfs(node, path):
                if not node:
                    return
                
                # Add the current node to the path
                path.append(node.val)
                
                # Append the current path for this node to all_paths
                all_paths.append(path[:])  # Store a copy of the current path
                
                # Recursively explore the left and right subtrees
                if node.left:
                    dfs(node.left, path)
                if node.right:
                    dfs(node.right, path)
                
                # Backtrack: remove the current node from the path
                path.pop()

            # Start DFS from the root
            dfs(root, [])
            
            return all_paths
        
        all_paths = find_all_paths(root)
        print("The all paths are:", all_paths)
        def count_paths_with_last_element_greater(all_paths):
            def is_last_element_greater_or_equal(path):
                last_element = path[-1]  # Get the last element
                # Check if the last element is greater than or equal to all other elements
                return all(last_element >= path[i] for i in range(len(path) - 1))
            
            # Count how many paths have the last element greater than or equal to all other elements
            return sum(1 for path in all_paths if is_last_element_greater_or_equal(path))


        return count_paths_with_last_element_greater(all_paths)
