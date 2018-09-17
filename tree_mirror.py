#!/usr/bin/python

'''
https://blog.csdn.net/Lynette_bb/article/details/73413184
'''

class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def tree_mirror(root):
    if root.val is None:
        return None

    tmp = root.left
    root.left = root.right
    root.right = tmp

    tree_mirror(root.left)
    tree_mirror(root.right)

    return root

