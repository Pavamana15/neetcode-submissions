# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
    
        if not root:
            return res  # Return an empty list if the tree is empty
        
        # Initialize the queue with the root node
        queue = deque([root])
        
        # Loop until there are nodes in the queue
        while queue:
            present_list = []  # List to store values of nodes at the current level
            # Number of nodes at the current level
            level_length = len(queue)
            
            for _ in range(level_length):  # Process all nodes at the current level
                current_node = queue.popleft()  # Dequeue the leftmost node
                present_list.append(current_node.val)  # Add current node's value to present_list
                
                # Enqueue the left child if it exists
                if current_node.left:
                    queue.append(current_node.left)
                
                # Enqueue the right child if it exists
                if current_node.right:
                    queue.append(current_node.right)
            
            # Append the list of values of the current level to the result
            res.append(present_list[-1])
        
        return res