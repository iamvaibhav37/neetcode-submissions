"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res = []
#this is iterative Solution
        def dfs(root):

            if not root:
                return 
            for c in root.children: #this part makes a lot of diff, since its postorder it will collect all children before going to parent. 
                dfs(c)
            
            res.append(root.val)
        dfs(root)
        return res