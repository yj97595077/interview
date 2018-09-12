r!/usr/bin/python

'''
level
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
    level = [root]
    level_num = 0
    q = [level]
    while q:
        level = q.pop(0)
        result_level = []
        next_level = []
        for node in level:
            if level_num % 2 == 0:
                result_level.append(node.val)
            else:
                result_level.insert(0, node.val)
            if node.left is not None:
                next_level.append(node.left)
            if node.right is not None:
                next_level.append(node.right)
        result.append(result_level)
        if next_level:
            q.append(next_level)
            level_num += 1

