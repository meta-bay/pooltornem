#!/usr/bin/env python3
"""
Match making module for pool Tornament
"""


class Match:
    """Single match match"""
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.is_leaf = False


class Makematch:
    """Binary tree style match making class"""
    def __init__(self):
        self.root = None
        self.leaf_count = 0

    def insert(self, data):
        if self.leaf_count < 16:
            if self.root is None:
                self.root = Match(data)
                self.root.is_leaf = True
                self.leaf_count += 1
            else:
                self._insert(data, self.root)

    def _insert(self, data, match):
        if match.is_leaf:
            if match.left is None:
                match.left = match(data)
                match.left.is_leaf = True
                self.leaf_count += 1
            elif match.right is None:
                match.right = match(data)
                match.right.is_leaf = True
                self.leaf_count += 1
            else:
                return
        else:
            if match.left:
                self._insert(data, match.left)
            else:
                match.left = match(data)
                match.left.is_leaf = True
                self.leaf_count += 1

            if self.leaf_count < 16 and match.right:
                self._insert(data, match.right)
            elif self.leaf_count < 16:
                match.right = match(data)
                match.right.is_leaf = True
                self.leaf_count += 1

    def inorder_traversal(self, match):
        if match:
            self.inorder_traversal(match.left)
            print(match.data, end=" ")
            self.inorder_traversal(match.right)

    def preorder_traversal(self, match):
        if match:
            print(match.data, end=" ")
            self.preorder_traversal(match.left)
            self.preorder_traversal(match.right)

    def postorder_traversal(self, match):
        if match:
            self.postorder_traversal(match.left)
            self.postorder_traversal(match.right)
            print(match.data, end=" ")

    def print_tree(self, match, level=0):
        if match:
            self.print_tree(match.right, level + 1)
            print("  " * level + str(match.data))
            self.print_tree(match.left, level + 1)

    def get_leaf_matchs(self):
        leaf_matchs = []
        self._get_leaf_matchs(self.root, leaf_matchs)
        return leaf_matchs

    def _get_leaf_matchs(self, match, leaf_matchs):
        if match:
            if match.is_leaf:
                leaf_matchs.append(match)
            else:
                self._get_leaf_matchs(match.left, leaf_matchs)
                self._get_leaf_matchs(match.right, leaf_matchs)
