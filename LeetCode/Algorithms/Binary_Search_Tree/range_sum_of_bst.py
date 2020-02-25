# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if root == None :
            return 0
        n = 0
        if root.val >= L and root.val <= R :
            n+= root.val    
        if root.val > L:
            n += self.rangeSumBST(root.left, L, R)
        if root.val < R:
            n += self.rangeSumBST(root.right, L, R)
        return n
            
        