# 生成 N (N <= 55) 个 1 到 55 的随机整数，对其中的重复数字，只保留一个，把其余相同的去掉。
# 然后将这些数从小到大排序，完成“排序”和“去重”工作。
import random


class TreeNode:
    def __init__(self, value, left_child=None, right_child=None):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child


def insert(node, value):
    if value < node.value:
        if node.left_child is None:
            node.left_child = TreeNode(value)
        else:
            insert(node.left_child, value)
    elif value > node.value:
        if node.right_child is None:
            node.right_child = TreeNode(value)
        else:
            insert(node.right_child, value)


def print_tree(node):
    if node is None:
        return None
    print_tree(node.left_child)
    print(node.value, end=' ')  
    print_tree(node.right_child)


if __name__ == "__main__":
    root = TreeNode(random.randint(1, 55))
    for _ in range(int(input('input 1 - 55 number:')) - 1):
        insert(root, random.randint(1, 55))
    print_tree(root)
