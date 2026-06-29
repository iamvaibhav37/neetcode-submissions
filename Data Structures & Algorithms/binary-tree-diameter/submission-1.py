# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0  #self. is bcz we dont want dfs funtion to think is local variable and not usable by dfs functn. 
#self.variable used for creating a global var. which can be used by all the functions in the class. 
        def dfs(curr):

            if not curr:
                return 0

            left = dfs(curr.left) #this updates the curr variable
            right = dfs(curr.right) #this updates the curr variable

            self.res = max(self.res, left+right)
            return 1 + max(left, right)
        dfs(root)  #we start from the root 
        return self.res
