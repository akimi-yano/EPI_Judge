from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def is_balanced_binary_tree(tree: BinaryTreeNode) -> bool:
    # TODO - you fill in here.
    
    ans = True
    def helper(cur):
        nonlocal ans
        if not cur:
            return 0
        left_height = helper(cur.left)
        right_height = helper(cur.right)
        if abs(left_height - right_height) > 1:
            ans = False
        return max(left_height, right_height) + 1
    
    helper(tree)
    return ans

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_balanced.py',
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
