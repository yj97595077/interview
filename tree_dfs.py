#!/usr/bin/python

'''
stack LOFI
'''

class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def tree_bfs(root):
    if root.val is None:
        return []

    result = []
    q = [root]
    while q:
        node = q.pop()
        result.append(node.val)
        if node.right is not None:
            q.append(node.right)
        if node.left is not None:
            q.append(node.left)

