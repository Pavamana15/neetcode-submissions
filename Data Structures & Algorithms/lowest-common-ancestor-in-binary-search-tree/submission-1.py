# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # Function to search and return the path from root to target node (as TreeNodes)
        def Search(root, val):
            print(f"Searching for value {val}...")  # Debugging line
            path = []
            while root:
                print(f"Visiting node {root.val}")  # Debugging line
                path.append(root)  # Append the TreeNode itself to the path
                if root.val == val:
                    print(f"Found {val}")  # Debugging line
                    return path  # Return the path when the target value is found
                
                # Traverse left or right based on the value
                if val < root.val:
                    root = root.left
                else:
                    root = root.right
            
            print(f"Value {val} not found")  # Debugging line
            return None  # If the target value is not found, return None

        # Function to find the Lowest Common Ancestor (LCA)
        def findLCA(root, p, q):
            print(f"Finding LCA of {p} and {q}...")  # Debugging line
            # Find the paths from root to p and root to q
            path1 = Search(root, p.val)
            path2 = Search(root, q.val)
            
            # Debugging print statements
            print(f"Path to {p}: {[node.val for node in path1] if path1 else 'Not Found'}")
            print(f"Path to {q}: {[node.val for node in path2] if path2 else 'Not Found'}")
            
            # If either path is None, one of the values was not found
            if not path1 or not path2:
                print(f"One of the nodes ({p} or {q}) was not found in the tree.")  # Debugging line
                return None

            # Find the last common node in both paths
            lca = None
            for node1, node2 in zip(path1, path2):
                print(f"Comparing nodes {node1.val} and {node2.val}")  # Debugging line
                if node1 == node2:
                    lca = node1  # Update LCA to the last common node (TreeNode)
                else:
                    break  # Stop when the paths diverge
            
            if lca:
                print(f"LCA found: {lca.val}")  # Debugging line
            else:
                print("LCA not found")  # Debugging line
            return lca  # Return the TreeNode representing the LCA

        return findLCA(root, p, q)
        # def Search(root,val):
        #     parent = []
            
        #     while root:
        #         parent.append(root.val)
        #         if root.val == val:
        #             return root, parent  # Found the target value
                
        #         # Go left if the target value is smaller than the current node's value
        #         if val < root.val:
                    
        #             root = root.left
                    
        #         else:
        #             # Go right if the target value is greater
                    
        #             root = root.right
            
        #     # If we don't find the value, return None
        #     return None

        # Search1, parent1 = Search(root,p)
        # Search2, parent2 = Search(root,q)

        # return min(min(parent1), min(parent2))