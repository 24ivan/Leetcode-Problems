# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.pList = []
        self.qList = []

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.dfs(p, 1)
        self.dfs(q, 2)
        print(self.pList)
        print(self.qList)
        return self.qList == self.pList
    def dfs(self, node, id):
        if node is None:
            return
        self.dfs(node.left, id)
        
        if id == 1:
            self.pList.append(node.val)
        else:
            self.qList.append(node.val)
        self.dfs(node.right, id)
        
