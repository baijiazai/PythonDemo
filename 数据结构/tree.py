# 二叉树
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.value = val
        self.left_child = left
        self.right_child = right


def search(val, node):
    if val < node.value:
        return search(val, node.left_child)
    elif val > node.value:
        return search(val, node.right_child)
    else:
        return node


def insert(val, node):
    if val < node.value:
        if node.left_child is None:
            node.left_child = TreeNode(val)
        else:
            insert(val, node.left_child)
    elif val > node.value:
        if node.right_child is None:
            node.right_child = TreeNode(val)
        else:
            insert(val, node.right_child)


def delete(val_to_del, node):
    if node is None:
        return None
    elif val_to_del < node.value:
        node.left_child = delete(val_to_del, node.left_child)
        return node
    elif val_to_del > node.value:
        node.right_child = delete(val_to_del, node.right_child)
        return node
    elif val_to_del == node.value:
        if node.left_child is None:
            return node.right_child
        elif node.right_child is None:
            return node.left_child
        else:
            node.right_child = lift(node.right_child, node)
            return node


def lift(node, node_to_del):
    """
                    root
                    /   \ 
            left_node    right_node(node_to_del)
            /               /     \ 
    left_node       left_node    right_node
                        /
                left_node(lift_node)
                     \ 
                   right_node(child_to_parent)
    """
    # 如果此函数的当前节点有左子节点
    if node.left_child:
        # 则递归调用本函数，从左子树找出后续节点
        node.left_child = lift(node.left_child, node_to_del)
        return node
    else:  # 如果此函数的当前节点无左子节点
        # 则代表当前节点是后续节点，于是将其值设置为被删除节点的新值
        node_to_del.value = node.value
        # 用后续节点的右子节点替代后续节点的父节点的左子节点
        return node.right_child


def traverse_and_print(node):
    if node is None:
        return
    traverse_and_print(node.left_child)
    print(node.value, end=' ')
    traverse_and_print(node.right_child)


# 迭代（非递归）
def traverse_and_print2(node):
    if node is None:
        return None
    stack = []
    while node != None or len(stack):
        if node != None:
            stack.append(node)
            node = node.left_child
        else:
            node = stack.pop()
            print(node.value, end=' ')
            node = node.right_child
