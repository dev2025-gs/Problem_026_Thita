# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        Determines if two binary trees are the same.
        Two binary trees are considered the same if they are structurally identical,
        and the nodes have the same value.

        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        # If both nodes are None, the trees are identical up to this branch
        if p == None and q == None:
            return True
        else:
            # Traverse both trees simultaneously
            while p and q:
                # If both nodes are not None and their values are equal
                if p.val == q.val and p is None and q is None:
                    # Both nodes are leaves and equal
                    return True
                else:
                    # Recursively check left and right subtrees
                    return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        # If one is None and the other is not, or values do not match
        return False