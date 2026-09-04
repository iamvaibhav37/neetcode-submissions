# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        sum1= 0 

        def dfs(node):
            nonlocal sum1 
            if not node:
                return 
            if node.val>=low and node.val<=high:
                sum1 += node.val 
            dfs(node.right)
            dfs(node.left)
            
        dfs(root)
        return sum1