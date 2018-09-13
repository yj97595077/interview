#!/usr/bin/python

'''
'''

class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def __init__(self):
        pass

    def inorder_travel(self, root):
        if root.val is None:
            return []

        inorder = []
        inorder += self.inorder_travel(root.left)
        inorder.append(root.val)
        inorder += self.inorder_travel(root.right)

        return inorder

    def is_tree_bst(self, root):
        if root.val is None:
            return False

        inorder = self.inorder_travel(root)
        for i in range(len(inorder)):
            if i == 0:
                continue
            if inorder[i-1] > inorder[i]:
                return False

        return True

